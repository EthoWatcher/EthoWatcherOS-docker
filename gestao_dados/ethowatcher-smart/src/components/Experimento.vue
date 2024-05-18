<template>
  <div class="experimentos">
    <!-- <b-button class="item" v-on:click="pegar_dados" variant="success">Pegar dados</b-button> -->

    <div>
      <div class="item">
        <h2>Add new experiment</h2>
        <p>
          This page you will found your registered databases, to start gathering
          data fill
          <input
            type="text"
            placeholder="Experiment name"
            id="experiment_name"
            v-model="this.new_experiment_text"
          />
          and then click
          <input
            type="button"
            v-on:click="create_new_experiment()"
            value="Create new experiment"
          />
        </p>
      </div>
    </div>
    <div>
      <div class="container">
        <div class="item" v-for="item in lis_experimentos" :key="item.message">
          
          <div class="card-section">
            <h2>The {{ item.nome_banco_experimental }} database</h2>
          <img
            class="img-card"
            src="@/assets/data_image.png"
            alt=""
            srcset=""
          />

          </div>
          <div class="card-section">
            <h2>Manage Database</h2>
          <p>
            Clique no botão
            <router-link
              v-bind:to="{ name: 'db_management', params: { hash: item._id } }"
            >
              <button id="myButton" class="foo bar">
                Manage the database {{ item.nome_banco_experimental }} database
              </button>
            </router-link>
            para acessar a área de gestão dos dados desse experimento, nessa
            sessão é possivel enviar os dados produzidos pelo EthoWatcher OS
            (see how to get one copy), e adicionar informações a respeito dos
            seus metadados (e.g. sexo do animal, tratamento)
          </p>

          </div>
          


          <div class="card-section">
            <h2>Query the Database</h2>
              <p>
                Clique no botão
                <router-link
                  v-bind:to="{ name: 'gestaoexp', params: { hash: item._id } }"
                >
                  <button id="myButton" class="foo bar">
                    Query the {{ item.nome_banco_experimental }} Database
                  </button>
                </router-link>
                para acessar a área de gestão dos dados desse experimento. Nessa
                seção é possivel realizar pesquisas no banco de dado produzido a
                partir das informações registradas (ex. selecionar as durações do
                comportamento de imobilidade dos ratos machos ou fêmeas tratadas com 2.5mg de fluoxetina) 
              </p>

              <input class="warning"
                type="button"
                v-on:click="delete_experimento(item._id)"
                value="Delete Me"
              />
          </div>
          

          <!-- <b-button v-bind:href='"/gestaoexp/"+item._id' variant="primary">{{ item.nome_banco_experimental }}</b-button> -->
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { get_url } from '../services/url'

export default {
  data() {
    return {
      new_experiment_text: "",
      r_logado: false,
      lis_experimentos: [],
    };
  },
  mounted() {
    // console.log("rodou antes do componeten")
    // let data =  localStorage.getItem("access_token");
    // let vue_component = this
    acessando_protegido(this);

    // let r_exite_toke_logado = data != undefined
    // if (r_exite_toke_logado){
    //     this.r_logado = true
    // }
    // this.$emit("update_usuario", this.r_logado)
  },

  methods: {
    create_new_experiment() {
      create_experiment(this);
      this.new_experiment_text = "";
    },
    delete_experimento(experimento_hash) {
      del_experiment(this, experimento_hash);
    },
    pegar_dados() {
      acessando_protegido(this);
    },
  },
};

function create_experiment(vue) {
  async function fun_asincrona(vue) {
    let params = {
      nome_banco_experimental: vue.new_experiment_text,
    };

    let data = localStorage.getItem("access_token");

    // this = vue_component
    // vue_component.r_logado = true
    const res = await fetch(get_url() + "/api/add_new_experimento", {
      method: "POST",
      // credentials: "include",
      headers: new Headers({
        "content-type": "application/json",
        Authorization: "Bearer " + data,
      }),
      body: JSON.stringify({
        nome_banco_experimental: params.nome_banco_experimental,
      }),
    });

    const data2 = await res.json();

    // vue.list_juncoes = data2;

    // console.log(vue.list_juncoes);
    acessando_protegido(vue);
  }

  fun_asincrona(vue);
}

function del_experiment(vue, hash) {
  async function fun_asincrona(vue) {
    let params = {
      hash: hash,
    };

    let data = localStorage.getItem("access_token");

    // this = vue_component
    // vue_component.r_logado = true
    const res = await fetch( get_url()+ "/api/delete_experimento", {
      method: "POST",
      // credentials: "include",
      headers: new Headers({
        "content-type": "application/json",
        Authorization: "Bearer " + data,
      }),
      body: JSON.stringify({
        experimento_hash: params.hash,
      }),
    });

    const data2 = await res.json();

    // vue.list_juncoes = data2;

    // console.log(vue.list_juncoes);
    acessando_protegido(vue);
  }

  fun_asincrona(vue);
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

    let res = await fetch(
      get_url()+ "/api/get_experimentos_user",
      j_obc_config
    );
    let data_r = await res.json();
    vue_component.lis_experimentos = data_r["experimentos"];
    console.log(data_r);
  };
  pega_dados_async(vue_component, 192);
}
</script>


<style scoped>
.img-card {
  max-width: 30%;
}
.container {
  display: flex;
  flex-wrap: wrap;
}
.item {
  font-size: 1.1em;
  margin: 20px;
  border-style: solid;
  border-width: medium;
  padding: 20px;
}
.experimentos {
  margin: 80px;
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

.card-section{
  border-top-style: ridge;
  margin-top: 20px;
  margin-bottom: 20px;
}
.warning{
  background: rgb(255, 105, 130);
}
</style>