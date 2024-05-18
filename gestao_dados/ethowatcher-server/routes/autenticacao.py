from flask import Flask, jsonify, request, make_response, render_template

import json

import deposito_watcher.api as api


from bson.objectid import ObjectId
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

def create_app(app):
    jwt = JWTManager(app)


    @app.route('/api/create_user', methods=['POST'])
    def create_user():
        # pass
        req = request.get_json()
        # id_experimento = req["id_experimento"]
        # dict_saida = req["dict_pesquisa"]

        r_ecnotrn = api.create_usuario_by(req)
        if r_ecnotrn:
            
            return jsonify({"msg":"deu certo"}), 200
        else:
            return jsonify({"msg":"algo deu erraod"}),200
    
    @app.route("/api/delete_user")
    @jwt_required()
    def delete_user():
        current_user = json.loads(get_jwt_identity())
        id_user = current_user["id_usuario"]
        # id_exp = request.args.get('id_experimento')
        r_deu_certo = api.deleta_usuario(id_user)
        if r_deu_certo:
            return jsonify({"msg":"deu certo"}),200
        else:
            return jsonify({"msg":"algo deu erraod"}),200


    @app.route('/api/query_db', methods=['POST'])
    @jwt_required()
    def query_db():
    #     # pass
        req = request.get_json()
        id_experimento = req["id_experimento"]
        dic_var_dependente = req["dic_var_dependente"]
        dict_pesquisa = req["dict_pesquisa"]

        def checa_se_tem_1(dict_pesquisa):
            keys = dict_pesquisa.keys()

            for chave in keys:
                ls_or = dict_pesquisa[chave]
                r_so_tem_1 = len(ls_or['$or']) == 1 
                r_so_tem_0 = len(ls_or['$or']) == 0
                if(r_so_tem_1):
                    dict_pesquisa[chave] = ls_or['$or']
                elif(r_so_tem_0):
                    pass #nao sei se esta sendo eficaz
                else:
                    dict_pesquisa[chave] = ls_or

            return dict_pesquisa


        def creat_dict_query(dict_pesquisa, id_experimento):
            keys = dict_pesquisa.keys()
            dic_query = {}
            ls_and = []
            ls_and.append({"id_experimento": ObjectId(id_experimento)})
            for chave in keys:
                # new_dic = {}
                # new_dic[chave] = dict_pesquisa[chave]
                ls_and.append(dict_pesquisa[chave])
            
            dic_query["$and"] = ls_and
            return dic_query
        
        dic_query = creat_dict_query(checa_se_tem_1(dict_pesquisa), id_experimento )
        
        r_ls_cate = "ls_categorias" in dic_var_dependente
        
        r_des_eto = "ls_des_cate" in dic_var_dependente
        r_var_eto = "ls_var_eto" in dic_var_dependente
        r_var_rast = "ls_des_rast" in dic_var_dependente
        r_juncao = "lis_desc_juncao" in dic_var_dependente
        
        if r_ls_cate:
            ls_categorias = dic_var_dependente["ls_categorias"]
        else:
            ls_categorias = []
        
        if r_des_eto:
            ls_des_cate = dic_var_dependente["ls_des_cate"]
        else:
            ls_des_cate = []
        
        if r_var_eto:
            ls_var_eto = dic_var_dependente["ls_var_eto"]
        else:
            ls_var_eto = []

        if r_var_rast:
            ls_des_rast = dic_var_dependente["ls_des_rast"]
        else:
            ls_des_rast = []
        
        if r_juncao:
            lis_desc_juncao = dic_var_dependente["lis_desc_juncao"]
        else:
            lis_desc_juncao = [] 
              
        r_ecnotrn, df = api.query_dados(id_experimento,dic_query, ls_categorias, ls_des_cate, ls_var_eto, ls_des_rast, lis_desc_juncao)
        if r_ecnotrn:
            resp = make_response(df.to_csv())
            resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
            resp.headers["Content-Type"] = "text/csv"
            return resp,200
        else:
            return jsonify({"msg":"algo deu erraod"}),200



    

    @app.route('/api/get_dados_tabela', methods=['POST'])
    @jwt_required()
    def get_dados_tabela():
        # pass
        req = request.get_json()
        id_experimento = req["id_experimento"]
        dict_saida = req["dict_pesquisa"]

        r_ecnotrn, df = api.get_csv_by_query(id_experimento, dict_saida)
        if r_ecnotrn:
            resp = make_response(df.to_csv())
            resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
            resp.headers["Content-Type"] = "text/csv"
            return resp,200
        else:
            return jsonify({"msg":"algo deu erraod"}),200


    @app.route("/api/get_experimento_by_hash")
    @jwt_required()
    def get_experimento_by_hash():
        current_user = json.loads(get_jwt_identity())
        id_user = current_user["id_usuario"]
        id_exp = request.args.get('id_experimento')
        r_deu_certo, documento = api.get_exp_by_hash(id_exp, id_user)
        if r_deu_certo:
            return jsonify({"experimento":documento}),200
        else:
            return jsonify({"msg":"algo deu erraod"}),200


    @app.route("/api/create_new_juncao", methods=['POST'])
    @jwt_required()
    def create_new_juncao():
        current_user = json.loads(get_jwt_identity())
        # FALTA BLOQUEAR OUTROS USUARIOS DE ACESSAR A JUNCAO 
        req = request.get_json()
        experimento_hash = req["id_experimento"]
        r_deu_certo = api.create_juncao(experimento_hash)
        if r_deu_certo:
            return jsonify({"msg": "Algo deu certo"}), 200
        else:
            return jsonify({"msg": "Algo deu errado"}), 400

    @app.route("/api/update_juncao", methods=['POST'])
    @jwt_required()
    def update_juncao():
        current_user = json.loads(get_jwt_identity())
        # FALTA BLOQUEAR OUTROS USUARIOS DE ACESSAR A JUNCAO 
        req = request.get_json()
        juncao_hash = req["juncao_hash"]
        ext = req["ext"]
        xml_text = req["xml_text"]
        r_deu_certo = False

        r_ext_video = ext =="vxml"
        r_ext_eto = ext == "etoxml"
        r_ext_trk = ext == "tkin"
        r_ext_meta = ext == "metadados"

        if(r_ext_video):
            r_deu_certo = api.update_juncao(juncao_hash, xml_text, r_video=True)

        if(r_ext_eto):
            r_deu_certo = api.update_juncao(juncao_hash, xml_text, r_eto=True)
        
        if(r_ext_trk):
            r_deu_certo = api.update_juncao(juncao_hash, xml_text, r_rast=True)
        
        if(r_ext_meta):
            r_deu_certo = api.update_juncao(juncao_hash, xml_text)


        if r_deu_certo:
            return jsonify({"msg": "Algo deu certo"}), 200
        else:
            return jsonify({"msg": "Algo deu errado"}), 400

        
    

    @app.route("/api/delete_juncao", methods=['POST'])
    @jwt_required()
    def delete_juncao():
        current_user = json.loads(get_jwt_identity())
        # FALTA BLOQUEAR OUTROS USUARIOS DE ACESSAR A JUNCAO 
        req = request.get_json()
        juncao_hash = req["id_juncao"]
        r_deu_certo = api.delete_juncao(juncao_hash)
        if r_deu_certo:
            return jsonify({"msg": "Algo deu certo"}), 200
        else:
            return jsonify({"msg": "Algo deu errado"}), 400


    @app.route("/api/get_juncao_by_hash", methods=['POST'])
    @jwt_required()
    def get_juncao_by_hash():
        current_user = json.loads(get_jwt_identity())
        # FALTA BLOQUEAR OUTROS USUARIOS DE ACESSAR A JUNCAO 
        req = request.get_json()
        id_juncao = req["id_juncao"]
        r_deu_certo, documentos = api.get_juncao_by_hash(id_juncao)
        if r_deu_certo:
            return jsonify({"juncoes": documentos}), 200
        else:
            return jsonify({"msg": "Algo deu errado"}), 400
            
    
    @app.route("/api/get_list_juncao", methods=['POST'])
    @jwt_required()
    def get_list_juncao():
        current_user = json.loads(get_jwt_identity())
        # FALTA BLOQUEAR OUTROS USUARIOS DE ACESSAR A JUNCAO 
        req = request.get_json()
        experimento_hash = req["id_experimento"]
        r_deu_certo, documentos = api.get_list_juncao(experimento_hash)
        if r_deu_certo:
            return jsonify({"juncoes": documentos}), 200
        else:
            return jsonify({"msg": "Algo deu errado"}), 400




    @app.route("/api/get_experimentos_user")
    @jwt_required()
    def get_experimentos():
        current_user = json.loads(get_jwt_identity())
        id_user = current_user["id_usuario"]
        r_deu_certo, documentos = api.get_list_experimento(id_user)
        if r_deu_certo:
            return jsonify({"experimentos": documentos}), 200
        else:
            return jsonify({"msg": "Algo deu errado"}), 400

    @app.route("/api/update_experimento_var", methods=['POST'])
    @jwt_required()
    def update_experimento_var():
        current_user = json.loads(get_jwt_identity())
        id_user = current_user["id_usuario"]
        req = request.get_json()
        r_deu_certo = api.atualiza_experimento(req["_id"], req)
        if r_deu_certo:
            return jsonify({"msg": "deu certo"}), 200
        else:
            return jsonify({"msg": "Algo deu errado"}), 400

    @app.route("/api/add_new_experimento", methods=['POST'])
    @jwt_required()
    def add_new_experimento():
        current_user = json.loads(get_jwt_identity())
        id_user = current_user["id_usuario"]
        req = request.get_json()
        # data["nome_banco_experimental"]
        r_deu_certo = api.creat_experimento(id_user, req)

        if r_deu_certo:
            return jsonify({"msg": "Working"}), 200
        else:
            return jsonify({"msg": "Algo deu errado"}), 400

    @app.route("/api/delete_experimento", methods=['POST'])
    @jwt_required()
    def delete_experimento():
        current_user = json.loads(get_jwt_identity())
        id_user = current_user["id_usuario"]
        req = request.get_json()
        # data["nome_banco_experimental"]
        r_deu_certo = api.delete_experimento(req["experimento_hash"])

        if r_deu_certo:
            return jsonify({"msg": "Working"}), 200
        else:
            return jsonify({"msg": "Algo deu errado"}), 400



    @app.route('/login', methods=['POST'])
    def login():
        req = request.get_json()
        print(req)
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username:
            return jsonify({"msg": "Missing username parameter"}), 400
        if not password:
            return jsonify({"msg": "Missing password parameter"}), 400

        # if username != 'test' or password != 'test':
        #     return jsonify({"msg": "Bad username or password"}), 401
        r_usuario_existe, id_usuario, _ = api.get_usuario(username, password)
        
        if(r_usuario_existe):
            
            usuario = {"username": username, "id_usuario":id_usuario}
            json_usuario = json.dumps(usuario)

            # Identity can be any data that is json serializable
            access_token = create_access_token(identity=json_usuario)
            return jsonify(access_token=access_token, logado=True), 200
        else:
            return jsonify({"msg": "Missing password parameter", "error": True}), 400

    
    # Protect a view with jwt_required, which requires a valid access token
    # in the request to access.
    @app.route('/protected', methods=['GET'])
    @jwt_required()
    def protected():
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return current_user, 200

    