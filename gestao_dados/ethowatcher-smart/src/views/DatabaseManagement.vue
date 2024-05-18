<template>
  <div id="DataManagement">
    <div id="Info">Welcome to {{ this.exp_docum.nome_banco_experimental }}</div>

    <div id="categoria_id">
      <div class="metadata-menu">

         
          <div class="metadata-menu-item" id="tutor3">
            <h2> Add categories off behavioral catalog</h2>
            <p>
              To start, add categories used in behavioral catalog. 
            </p>
            
            <h2> Add metadata of the experiment</h2>
            <p>In sequence, add some metadata categorie your experiment have (ex. animal sex, animal treatment), after add all the categorie from that created metada (ex. male and female categories form animal sex metadata categorie )
            </p>
            <p> After input all metadata of your experiment click in "Save alterations" button to save the alterations. WARNING, after you save you will not more will be able to update the metadata.</p>
           
               

          </div>
        <div class="metadata-menu-item" id="categorie">
          

          <div v-if="r_exp">
            <Categorie
              v-bind:experimento="this.exp_docum"
              @update-exp_docum="handle_update_document"
            />
          </div>
        </div>

        <div class="metadata-menu-item">
          <div v-if="r_exp">
            <div class="control-menu">
              
              <div class="control-menu-item">
                <h2>Metadata of the experiment</h2>

              <div>
                <input
                  type="text"
                  placeholder="Input the name of the metadata"
                  v-model="this.t_new_metada"
                />
                <input
                  type="button"
                  v-on:click="add_new_metakey()"
                  value="Add new metadata key"
                />
              </div>  
                <div class="control-menu-item"> 
                <h2>Save your metadata</h2>

              <input
                type="button"
                v-on:click="atualiza_bd()"
                value="Save alterations"
              />

              </div>

              </div>
              
                          
            </div>
            
          </div>
        </div>
      </div>

      
    </div>

    <div v-if="r_exp">
<div >
              <ListaMeta
                v-bind:experimento="this.exp_docum"
                @update-exp_docum="handle_update_document"
              />
            </div>
    </div>

    <div id="List_juncoes" v-if="r_exp">
      <ListaJuncoes
        v-bind:experimento="this.exp_docum"
        v-on:update_list="force_update()"
      />
    </div>


  </div>
</template>



<script>
import ListaJuncoes from "../components/DbManagement/ListaJuncoes/ListaJuncoes.vue";
import Categorie from "../components/DbManagement/Categorie.vue";
import ListaMeta from "../components/DbManagement/ListaMetadados.vue";

import { get_url } from '../services/url'

export default {
  components: {
    ListaJuncoes,
    Categorie,
    ListaMeta,
  },
  setup() {},
  mounted() {
    acessando_protegido(this);
  },
  methods: {
    add_new_juncao(){
      // add_new_juncao(this, this.exp_docum['_id'])
    },

    force_update() {
      this.r_exp = false;
      this.r_exp = true;
    },
    delete_categorie(array, index) {
      console.log(index, array);
      array.splice(index, 1);
      console.log(this.exp_docum);
    },
    atualiza_bd() {
      atualiza_documento(this, this.exp_docum);
    },
    handle_update_document(new_exp_document) {
      this.exp_docum = new_exp_document;
      //
    },
    add_new_metakey() {
      let gera_nova_key = (array) => {
        let saida = this.exp_docum.var_inde.map((ind) => {
          return Number(ind["nome"]);
        });
        let max = Math.max(...saida) + 1;
        return max;
      };

      let new_meta = {
        categorias: [],
        nome: gera_nova_key(this.exp_docum.var_inde),
        texto_interface: this.t_new_metada,
      };

      this.exp_docum.var_inde.push(new_meta);
      this.t_new_metada = "";
    },
  },
  data() {
    return {
      r_exp: false,
      exp_docum: {},
      t_new_metada: "",
      modules: [
        {
          id: 1,
          name: "Business",
          checked: true,
        },
        {
          id: 2,
          name: "Business 2",
          checked: false,
        },
      ],
    };
  },
};

// function add_new_juncao(vue, id_experimento) {
//   async function fun_asincrona(vue, id_experimento) {
//     let params = {
//       id_experimento: id_experimento,
//     };

//     let data = localStorage.getItem("access_token");

//     // this = vue_component
//     // vue_component.r_logado = true
//     const res = await fetch("http://localhost:5000/api/create_new_juncao", {
//       method: "POST",
//       // credentials: "include",
//       headers: new Headers({
//         "content-type": "application/json",
//         Authorization: "Bearer " + data,
//       }),
//       body: JSON.stringify({
//         id_experimento: params.id_experimento,
//       }),
//     });
//     const data2 = await res.json();

//     // get_lista_juncao_db(vue, id_experimento);
//   }

//   fun_asincrona(vue, id_experimento);
// }



function atualiza_documento(vue, data) {
  const pega_dados_async = async (vue, data) => {
    let data_e = localStorage.getItem("access_token");
    let j_obc_config = {
      method: "POST",
      // credentials: "include",
      headers: new Headers({
        "content-type": "application/json",
        Authorization: "Bearer " + data_e,
      }),

      body: JSON.stringify(data),
    };

    let res = await fetch( get_url()+ "/api/update_experimento_var",
      j_obc_config
    );

    let data_r = await res.json();
    console.log(data_r);

    acessando_protegido(vue);
    // vue_component.exp_docum = data_r["experimento"]
    // vue_component.r_exp=true
  };

  pega_dados_async(vue, data);
}

function acessando_protegido(vue_component) {
  const pega_dados_async = async (vue_component, as) => {
    let data = localStorage.getItem("access_token");
    let j_obc_config = {
      method: "GET",
      // credentials: "include",
      headers: new Headers({
        // "content-type": "application/json",
        Authorization: "Bearer " + data,
      }),
    };

    let str_params = new URLSearchParams({
      id_experimento: vue_component.$route.params.hash,
    });

    let res = await fetch( get_url()+ "/api/get_experimento_by_hash" + "?" + str_params,
      j_obc_config
    );
    let data_r = await res.json();
    vue_component.exp_docum = data_r["experimento"];
    vue_component.r_exp = true;
    // vue_component.dados_marcar = data_r["experimento"]["list_banco_imagem"]

    // vue_component.$emit("experimento_data", vue_component.exp_docum)
    console.log(data_r);
  };
  pega_dados_async(vue_component, 192);
}
</script>


<style scoped>
#DataManagement{
  margin: 40px;
}
.metadata-menu{
  display: flex;
  justify-content: space-around;
}
#categorie{
  min-height: 30%;
  min-width: 30%;
}

.control-menu{
  display: flex;
  gap: 100px;
}

.metadata-menu-item{
  margin: 40px;
}

h2{
  padding-top: 20px;
}

input {
  min-width: 40px;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

button {
  min-width: 40px;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

ul {
  display: inline-block;
  
}
</style>
