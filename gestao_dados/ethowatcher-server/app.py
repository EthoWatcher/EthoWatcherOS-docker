from flask import Flask, render_template
from flask_cors import CORS
import routes.autenticacao as autenticacao
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)




def create_app():
    app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

    CORS(app)
    

    #para o jwt
    app.debug = True
    app.config['JWT_SECRET_KEY'] = 'super-secret' 
    # app.config['SECRET_KEY'] = 'super-secret'
    autenticacao.create_app(app)
    @app.route("/")
    def helloWorld():
        return render_template('index.html')

    @app.route("/teste")
    def teste():
        return render_template('teste.html')
    # home.init_app(app)
    # banco.init_app(app)
    # autentiticacao_usuario.init_app(app)


    return app


# if __name__ == "__main__":
#     create_app().run(debug=True)

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)