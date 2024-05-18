<template>
    <h2>Editing metadata</h2>
    <div v-for="(metadata, index) in this.var_inde" :key="index">
        <h3>Selecione o {{metadata['texto_interface']}}</h3>

        <p v-if="calcula_if(metadata)">{{this.juncao.var_ind[metadata['nome']]}}</p>
        
        <SingleSelect v-else
        v-bind:metadata="metadata"
        v-bind:juncao="this.juncao"
        v-bind:var_inde="this.var_inde"
        v-on:selected_key_metadado="selecionado_key"
        />

        
    </div>

    <input type="button" v-on:click="reset_meta()"  value="Reset metadados">

</template>


<script>

import SingleSelect from "./SingleSelect.vue"

import { get_url } from '../../../services/url'

export default {
    components:{
        SingleSelect

    },
    
    props:{
        juncao: {},
        var_inde : [],
        selected : ""
    },
    data(){
        return{
            juncao: this.juncao,
            n_selecionado: true
        }
    },
    methods:{
        reset_meta(){
            this.juncao.var_ind = {}
            

        },
        calcula_if(metadata){
            let r_ = metadata["nome"] in this.juncao.var_ind

            return r_
        },
        selecionado_key(key){
            // let r_ =  in this.juncao.var_ind
            let lis_key = Object.keys(key)
            
            lis_key.forEach(ele =>{
                this.juncao.var_ind[ele] = key[ele]
                
                // let r_ja_exise =  ele in this.juncao.var_ind
                
                
                // if(r_ja_exise){
                    
                // }
            })
 
            update_junacao(this)
            

            
        }
    },
    setup() {
        
    },
    mounted(){
        console.log('esse componente esta sendo montado')
        let list_keys_juncao = Object.keys(this.juncao.var_ind)
        console.log(list_keys_juncao)
        
        detecta_sobra_categorias_metadata_na_juncao(this, this.juncao, this.var_inde, list_keys_juncao)
        detect_categorias_metadata_excluidas(this, this.juncao, this.var_inde, list_keys_juncao)   

    
    }
}

function update_junacao(vue) {
  async function fun_asincrona(vue) {
    let params = {      
      juncao_hash: vue.juncao['_id'],
      ext: 'metadados',
      xml_text: vue.juncao.var_ind
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




function detecta_sobra_categorias_metadata_na_juncao(vue, juncao, var_inde , list_keys_juncao){
    let list_key_var = var_inde.map( e=> String(e['nome']))
    
    let list_var_juncao = list_keys_juncao.map(e=> String(e))

    let lis_sobrando = []
    list_var_juncao.forEach(element => {
        let r_metadata_categorie_sobrando = list_key_var.findIndex( e => e == element) == -1
        
        if(r_metadata_categorie_sobrando){
            lis_sobrando.push(element)
            // precisa deletar e atualizar a juncao
            console.log("Essa variavel esta sobrando, prvovavelmente foi deletada",element)
        }
    });

    console.log(lis_sobrando)
    lis_sobrando.forEach(e =>{
        delete vue.juncao.var_ind[e]
    })
    
    
    // deleta_sobrando_juncao(vue, lis_sobrando)

}

// falta implementar
function deleta_sobrando_juncao(vue, lis_sobrando){

    lis_sobrando.forEach( element =>{
        delete vue.juncao.var_ind[element]

    });

    console.log("novo juncao var_ind apos retirar sobra",vue.juncao)

}

function detect_categorias_metadata_excluidas(vue, juncao, var_inde, list_keys_juncao){
    let list_key_var = var_inde.map( e=> String(e['nome']))
    
    let list_var_juncao = list_keys_juncao.map(e=> String(e['nome']))


}


</script>

<style scoped>

</style>