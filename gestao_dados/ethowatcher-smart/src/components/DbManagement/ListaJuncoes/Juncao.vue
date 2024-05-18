<template>


 <!-- <div class="juncao-menu-item">
   {{juncoes._id}}
 </div> -->

  <div class="juncao-menu-item">
    <h2> Video file</h2>
    <div v-if="juncoes.id_video != ''">
      {{ juncoes["video_data"]["cadastroVideo"]["dadoOriginal"]["nomeOpencv"] }}
    </div>
    <div v-else>
        <p> Send register video file (.vxml)</p>
      <ReadTxt
        v-bind:tipe_name="'id_video'"
        v-bind:id_juncao="juncoes._id"
        v-bind:id_elemnto_juncao="juncoes.id_video"
        v-bind:ext_certa="'vxml'"
        v-on:update-juncao="update_juncao()"
      />

    </div>
  </div>

  <div class="juncao-menu-item">
    <h2> Etograph file</h2>
    <div v-if="juncoes.id_eto != ''">
      {{ juncoes.id_eto }}
    </div>
    <div v-else>
        <p> Send etograph from selected video (Etograph)</p>
    <ReadTxt
        v-bind:tipe_name="'id_eto'"
        v-bind:id_juncao="juncoes._id"
        v-bind:id_elemnto_juncao="juncoes.id_eto"
        v-bind:ext_certa="'etoxml'"
        v-on:update-juncao="update_juncao()"
      />

    </div>
  </div>

  <div class="juncao-menu-item">
    <h2> Tracking file</h2>
    <div v-if="juncoes.id_tra != ''">
      {{ juncoes.id_tra }}
    </div>
    <div v-else>
        <p>Upload the tracking file (.tracking) of the selected video </p>
        <ReadTxt
        v-bind:tipe_name="'id_tra'"
        v-bind:id_juncao="juncoes._id"
        v-bind:id_elemnto_juncao="juncoes.id_tra"
        v-bind:ext_certa="'tkin'"
        v-on:update-juncao="update_juncao()"
      />
    </div>
  </div>

  <div class="juncao-menu-item">
  
    <EditMetadado 
    v-bind:juncao="this.juncoes"
    v-bind:var_inde="this.var_inde"
    />
  </div>

  <div class="juncao-menu-item">
    <input
      type="button"
      v-on:click="delete_juncao(juncoes._id)"
      value="Delete junção"
    />
  </div>
</template>


<script>
import ReadTxt from "./ReadTxt.vue";
import EditMetadado from "./EditMetadado.vue";

import { get_url } from '../../../services/url'


export default {
  components: {
    ReadTxt,
    EditMetadado,
  },
  props: {
    juncoes: {},
    experimento: {},
  },
  data() {
    return {
      juncoes: this.juncoes,
      var_inde:  this.experimento.var_inde
    };
  },
  methods: {

    delete_juncao(id_juncao) {
      deleta_juncao_by_hash(this, id_juncao);

    },
    update_juncao(){
      get_juncao_by_hash(this)
      // this.$emit("updateJuncaoA")
    }
  },
  setup() {},
};


function get_juncao_by_hash(vue) {
  async function fun_asincrona(vue) {

    let data = localStorage.getItem("access_token");

    // this = vue_component
    // vue_component.r_logado = true
    const res = await fetch(get_url() + "/api/get_juncao_by_hash", {
      method: "POST",
      // credentials: "include",
      headers: new Headers({
        "content-type": "application/json",
        Authorization: "Bearer " + data,
      }),
      body: JSON.stringify({id_juncao: vue.juncoes._id}),
    });
    const data2 = await res.json();
    vue.juncoes = data2["juncoes"]
    
    console.log(data2);
  }

  fun_asincrona(vue);
}


function deleta_juncao_by_hash(vue, id_juncao) {
  async function fun_asincrona(vue, id_juncao) {

    let data = localStorage.getItem("access_token");

    // this = vue_component
    // vue_component.r_logado = true
    const res = await fetch( get_url()+ "/api/delete_juncao", {
      method: "POST",
      // credentials: "include",
      headers: new Headers({
        "content-type": "application/json",
        Authorization: "Bearer " + data,
      }),
      body: JSON.stringify({id_juncao: id_juncao}),
    });
    const data2 = await res.json();

    vue.$emit("delete_juncao", {})

    console.log(data2);
  }

  fun_asincrona(vue, id_juncao);
}
</script>


<style scoped>
.juncao-menu {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}
.juncao-menu-item {
  /* background-color: red; */
  border-left-style: ridge;
  margin: auto;
 

}


input {
  min-width: 40px;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

</style>