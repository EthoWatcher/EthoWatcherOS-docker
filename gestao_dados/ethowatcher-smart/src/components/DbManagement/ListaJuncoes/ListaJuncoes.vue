<template>
  <div id="ListaDeJuncoes">


    <div>
      <h2> Update the EthoWatcher OS files</h2>
    <p> Click 
        <input
        type="button"
        v-on:click="add_new_juncao()"
        value="Attach etografie and tracking from the video"
      /> to Attach your files from Ethowatcher OS, and afterwards:
      </p>
      <ul>
        <li>1- Upload the video file (.vxml) </li>
        <li>2- Upoload the etographic file related to register video uploaded (.etoxml) </li>
        <li>3- Upload your tracking file related to registered video upoloadde (.tracking) </li>
        <li>4- Select the metadatas from the register video uploaded </li>
        <li>5- repeat </li>
      </ul>
      
    </div>
    
    <div v-for="(juncoes, index) in this.list_juncoes['juncoes']" :key="index">
      <div class="juncao-menu">
        <Juncao 
        v-bind:juncoes="juncoes"
        v-bind:experimento="this.experimento"
        v-on:delete_juncao="update_juncao()"
        v-if="renderComponent"
         />
      </div>
    </div>
    <br />
  </div>
</template>


<script>
import Juncao from "./Juncao.vue";
import { get_url } from '../../../services/url'

export default {
  components: {
    Juncao,
  },
  props: {
    experimento: {},
  },
  setup() {},
  data() {
    return {
      list_juncoes: [],
      experimento: this.experimento,
      var_ind: this.experimento.var_inde,
      renderComponent: true
    };
  },
  methods: {
    add_new_juncao() {
      console.log(this.experimento["_id"]);
      add_new_juncao(this, this.experimento["_id"]);
    },
    update_juncao() {
      this.renderComponent = false;
      get_lista_juncao_db(this, this.experimento["_id"]);
      this.$emit("update_list")

    }
  },
  mounted() {
    this.update_juncao()
    this.renderComponent =false
    this.renderComponent = true
  },
};

function add_new_juncao(vue, id_experimento) {
  async function fun_asincrona(vue, id_experimento) {
    let params = {
      id_experimento: id_experimento,
    };

    let data = localStorage.getItem("access_token");

    // this = vue_component
    // vue_component.r_logado = true
    const res = await fetch( get_url()+ "/api/create_new_juncao", {
      method: "POST",
      // credentials: "include",
      headers: new Headers({
        "content-type": "application/json",
        Authorization: "Bearer " + data,
      }),
      body: JSON.stringify({
        id_experimento: params.id_experimento,
      }),
    });
    const data2 = await res.json();

    get_lista_juncao_db(vue, id_experimento);
  }

  fun_asincrona(vue, id_experimento);
}

function get_lista_juncao_db(vue, id_experimento) {
  async function fun_asincrona(vue, id_experimento) {
    let params = {
      id_experimento: id_experimento,
    };

    let data = localStorage.getItem("access_token");

    // this = vue_component
    // vue_component.r_logado = true
    const res = await fetch( get_url() + "/api/get_list_juncao", {
      method: "POST",
      // credentials: "include",
      headers: new Headers({
        "content-type": "application/json",
        Authorization: "Bearer " + data,
      }),
      body: JSON.stringify({
        id_experimento: params.id_experimento,
      }),
    });
    const data2 = await res.json();

    vue.list_juncoes = data2;
    
    vue.renderComponent = true;
    console.log(vue.list_juncoes);
  }

  fun_asincrona(vue, id_experimento);
}
</script>


<style scoped>
.juncao-menu {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
  border-top-style: ridge;
  
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
</style>