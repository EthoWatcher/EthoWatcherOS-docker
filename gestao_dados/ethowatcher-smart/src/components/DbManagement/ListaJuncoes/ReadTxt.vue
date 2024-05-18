<template>
  <div>
    <div v-if="this.id_elemnto_juncao == '' ">
      <input
      ref="someName"
      type="file"
      name="name"
      style="display: none"/>
    <button v-on:click="get_arquivo_xml()">Upload</button>
    </div>

    <div v-else>
      <!-- <p>{{ this.ext }}</p> -->
      <p>{{this.id_juncao}}</p>
    </div>

    

    <!-- <p> {{this.text}}</p> -->
  </div>
</template>



<script>

import { get_url } from '../../../services/url'
export default {
  props: {
    id_juncao: "",
    tipe_name: "",
    id_elemnto_juncao :"",
    ext_certa:""
    
  },
  data() {
    return {
      id_juncao: this.id_juncao,
      id_experimento: this.id_experimento,
      id_elemnto_juncao: this.id_elemnto_juncao,
      tipe_name: this.tipe_name,
      text: "",
      name_ext: "",
      file_ext:""
    };
  },
  methods: {
    get_arquivo_xml() {
      var input = this.$refs.someName;
      input.type = "file";

      input.onchange = (e) => {
        // getting a hold of the file reference
        var file = e.target.files[0];
        this.ext = file.name;
        this.file_ext = this.ext.split(/\.(?=[^\.]+$)/);
        let r_ext_certa = this.file_ext[1] == this.ext_certa
        console.log(r_ext_certa)

        if(r_ext_certa){
          var reader = new FileReader();
          reader.readAsText(file, "UTF-8");

          // here we tell the reader what to do when it's done reading...
          reader.onload = (readerEvent) => {
            var content = readerEvent.target.result; // this is the content!
            this.text = content;

            update_junacao(this)
            };

        }
        // setting up the reader

      };

      input.click();

      // this.$refs.someName.onchange = e =>{
      //     var file = e.target.files[0];
      //     var reader = new FileReader();
      //     reader.readAsText(file,'UTF-8');

      //     // here we tell the reader what to do when it's done reading...
      //     reader.onload = readerEvent => {
      //     var content = readerEvent.target.result; // this is the content!
      //     console.log( content );
      //   }
      // }

      // this.$refs.someName.click();
    },
  },
  setup() {},
};


function update_junacao(vue) {
  async function fun_asincrona(vue) {
    let params = {      
      juncao_hash: vue.id_juncao,
      ext: vue.ext_certa,
      xml_text: vue.text
    };

    let data = localStorage.getItem("access_token");

    // this = vue_component
    // vue_component.r_logado = true
    const res = await fetch( get_url() + "/api/update_juncao", {
      method: "POST",
      // credentials: "include",
      headers: new Headers({
        "content-type": "application/json",
        Authorization: "Bearer " + data,
      }),
      body: JSON.stringify(params),
    });

    const data2 = await res.json();
    console.log(data2)

    vue.$emit("update-juncao")

  }

  fun_asincrona(vue);
}
</script>


<style scoped>

button {
  min-width: 40px;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
</style>