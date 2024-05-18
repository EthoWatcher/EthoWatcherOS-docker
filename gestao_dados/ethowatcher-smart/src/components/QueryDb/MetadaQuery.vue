<template>
  <div class="metaquery">
    

    <div class="page-menu">
        <div class="page-menu-item">
            <h2> Tutorial</h2>
            <p>
                To start make the query in the detabase select key metadatas from every categorie
            </p>
            <p>After select the etograph and tracking descpriptor selecting the box.
               
            </p>
            <p> In sequence click in "Query the database to get the CSV" button to get the correspondent dataset formated in CSV.

            </p>
        </div>


    <div class="page-menu-item">
        <div>
            <h2> Etograph and tracking descriptors and variables</h2>
        </div>

        <div>
            <div class="card-meta-menu">
                
                <div v-for="(metadado, index) in this.exp_docum.var_inde" :key="index" class="card-meta-item">
                <SelectMeta
                    v-bind:metadado="metadado"
                    v-on:mudo_metada="this.gravar_dicionario_meta"
                />
                </div>

            </div>
        </div>
            

        <div>
            
    <div class="dependente-menu">
        <h2> Etograph and tracking descriptors and variables</h2>
     <div class="dependente-menu-item">
      <h2>Select Behavioral categories</h2>
      <ListaParams
        v-bind:ls_params="this.ls_cate"
        v-bind:par_name="'ls_categorias'"
        v-on:update_var_de="this.gravar_d_var_depent"
        class="ls_para"
      />
    </div>

    <div class="dependente-menu-item">
      <h2>Select Behavioral Categorie variable</h2>
      <ListaParams
        v-bind:ls_params="this.ls_var_eto"
        v-bind:par_name="'ls_var_eto'"
        v-on:update_var_de="this.gravar_d_var_depent"
      />
    </div>
    <div class="dependente-menu-item">
      <h2>Select Behavioral Categorie descritor</h2>
      <ListaParams
        v-bind:ls_params="this.ls_descritor_eto"
        v-bind:par_name="'ls_des_cate'"
        v-on:update_var_de="this.gravar_d_var_depent"
      />
    </div>

    <div class="dependente-menu-item">
      <h2>Select Tracking variable</h2>
      <ListaParams
        v-bind:ls_params="this.ls_descritor_trk"
        v-bind:par_name="'ls_des_rast'"
        v-on:update_var_de="this.gravar_d_var_depent"
      />
    </div>

    <div  class="dependente-menu-item">
      <h2>Select Metadata</h2>
      <ListaParams
        v-bind:ls_params="this.ls_juncao"
        v-bind:par_name="'lis_desc_juncao'"
        v-on:update_var_de="this.gravar_d_var_depent"
      />
    </div>



    </div>


    <input
      type="button"
      value="Query the Database to get the CSV"
      v-on:click="get_csv()"
    />

        </div>

    

        </div>
    </div>



  </div>
</template>

<script>
import SelectMeta from "./Select.vue";
import ListaParams from "./ListParams.vue";

import { get_url } from '../../services/url'


export default {
  components: {
    SelectMeta,
    ListaParams,
  },
  props: {
    exp_docum: {},
  },
  data() {
    return {
      exp_docum: this.exp_docum,
      ls_cate: this.create_dic(
        this.arruma_list_cat(this.exp_docum.var_depend[0].categorias)
      ),

      ls_juncao: this.create_dic(this.arruma_juncao(this.exp_docum.var_inde)),
      ls_var_eto: this.create_dic([["Categorie Name", "nome"],
                              [ "Marcation number", "trecho"],
                              [ "Beginner behavior frame","q_inicial"],
                              [ "Last behavior frame", "q_final"]]
      ),
            ls_descritor_eto: this.create_dic(
            [["Duration off animal behavior", "duracao"], 
            [ "Latence off animal behavior", "latencia"], 
            ["Frequence off animal behvaior", "frequencia"]]
      ),
        ls_descritor_trk: this.create_dic(
        [ ["Frame", "@f"],
        ["Area off animal (px^2)", "@arP"],
          ["Area off animal (mm^2)", "@arM"],
          ["Animal centroide in X axis (px)", "@ceX"],
          ["Animal centroide in Y axis", "@ceY"],
          ["Animal length (px)", "@altP"],
          ["Animal length (cm)", "altM"],
          ["Animal width (px)", "larP"],
          ["Animal angle refers to X axis(deg)", "@an"],
          ["Variation of animal area by frame (px^2)", "@Var"],
          ["Variation of animal centroide position by frame (px)", "@Vd"],
          ["Variation of animal length  by frame (px)", "@Valt"],
          ["Variation off animal width by frame (px^2)", "@Vlar"]
        ]),
    

      dic_query: {},
      dic_var_d: {}
    };
  },
  methods: {
    gravar_d_var_depent(e){
    let ls_obj = Object.keys(e)
    ls_obj.forEach(ele =>{
        this.dic_var_d[ele] = e[ele]
    })

    console.log("atualizando var depe", this.dic_var_d)

    },
    get_csv() {
      console.log("oi");
      enviando_requisicao(this, this.dic_query)
    },
    gravar_dicionario_meta(e) {
    //   let resp = e;
    //   let rs_so_1_cat = resp.length == 1;
      let key_dic = Object.keys(e);
      key_dic.forEach(key =>{
          this.dic_query[key] = e[key]
      })
    //   this.dic_query[key_dic[0]] = e;

      // console.log("chegou o", e, this.dic_query, rs_so_1_cat)
    //   console.log(this.dic_query, this.dic_query[key_dic[0]]);
      console.log(this.dic_query)
    },
    arruma_juncao(ls_var_ind) {
      let ls = ls_var_ind.map((e) => [
        String(e["texto_interface"]),
        String(e["nome"]),
      ]);

      return ls;
    },
    arruma_list_cat(categorias) {
      var ls_saida = [];
      categorias.forEach((element) => {
        ls_saida.push([String(element), String(element)]);
      });
      return ls_saida;
    },
    create_dic(exp_d) {
      let ls_saida = [];
      let id = 0;
      exp_d.forEach((element) => {
        var [name, key] = element;
        ls_saida.push({ id: id, name: name, key: key, checked: false });
        id = id + 1;
      });

      return ls_saida;
    },
    // arruma_list_categoria(exp_d){
    //     ls_saida =[]
    //     exp_d.var_depend[0].categorias.forEach(element => {
    //         ls_saida.push({"cat_name": element, "select": false})
    //     });
    //     return ls_saida

    // }
  },

  mounted() {},
};

function enviando_requisicao(vue, dic_query) {
   let dict_pesquisa = dic_query; 
    console.log(dict_pesquisa)



  let data = localStorage.getItem("access_token");
  console.log(vue.exp_docum);
    fetch( get_url() + "/api/query_db", {
    method: "POST",
    // credentials: "include",
    headers: new Headers({
      "content-type": "application/json",
      Authorization: "Bearer " + data,
    }),
    body: JSON.stringify({
      dic_var_dependente: vue.dic_var_d,
      dict_pesquisa: dict_pesquisa,
      id_experimento: vue.exp_docum["_id"],
    }),
  }).then((response) => {
    console.log(response);
    response.text().then((data) => {
      var text = "hello world",
        blob = new Blob([data], { type: "text/plain" }),
        anchor = document.createElement("a");

      anchor.download = "hello.csv";
      anchor.href = (window.webkitURL || window.URL).createObjectURL(blob);
      anchor.dataset.downloadurl = [
        "text/plain",
        anchor.download,
        anchor.href,
      ].join(":");
      anchor.click();
      // document.getElementById("result").innerHTML = data
      // let blob = new Blob(["12312 123123"], {type: "text/plain; charset=utf-8"})
      // saveAs(blob, "joao.txt")

      // console.log(data)
    });
  });
}
</script>


<style scoped>
.metaquery{
    margin: 50px;
}
input {
  min-width: 40px;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
.card-meta-menu{
    display: flex;
}
.card-meta-item{
    margin: 10px;
}
.dependente-menu{
    display: flex;
    flex-direction: column;
    /* flex-wrap: wrap; */
    align-items: center;
    flex-flow: center;
    gap: 30px;
    margin: 30px;
}
.dependente-menu-item{
    margin-right: auto;
}
h2{
    float: left;
    margin-right: 20px;

}
.ls_para{
    margin-left: 10px;
}

.page-menu{
    display: flex;
    justify-content: center;
    
    }
.page-menu-item{
    display: flex;
    flex-direction: column;
    flex: 1 1 0px;
}
p{
    padding-top: 20px;
}
</style>