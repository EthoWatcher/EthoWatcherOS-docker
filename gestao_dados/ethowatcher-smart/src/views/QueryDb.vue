<template>
    <div class="gestaoexp">
        
        <!-- <p>Experiment {{this.id_experiment}}</p> -->
    
        <MetaQuery v-bind:exp_docum="this.exp_docum" v-if="r_exp"/>

    </div>
</template>


<script>

import MetaQuery from "../components/QueryDb/MetadaQuery.vue"

import {get_url} from "../services/url"

export default {
    components:{
        MetaQuery
    },
      data() {
        return{
                r_logado: true,
                id_experiment: this.$route.params.hash,
                exp_docum: {},
                r_exp: false,
                dados_marcar:[],
                
        }
       
    },
    methods:{},

    mounted(){
        console.log(this.id_experiment)
        
        // const ComponentConectro = Vue.extend(Buscador_dados)
        // const ComponentInstance = new ComponentConectro(
        //     {propsData:{
        //         name:"jao"
        //     }}
        // )
        // ComponentInstance.$mount("#buscador")

        acessando_protegido(this)
        this.name = "!23123"
        // this.experimento_data()
        // this.$emit("experimento_data", "123123")
    }
}


function acessando_protegido(vue_component){
            const  pega_dados_async = async (vue_component, as) =>{
            let data =  localStorage.getItem("access_token");
            let j_obc_config ={
                    method: "GET",
                    // credentials: "include",
                    headers: new Headers({
                        // "content-type": "application/json",
                        'Authorization': 'Bearer ' + data
                    })
                }

            let str_params = new URLSearchParams({
                                    id_experimento: vue_component.$route.params.hash
                                    })

            let res = await fetch( get_url() + "/api/get_experimento_by_hash"+ "?" + str_params , j_obc_config);
            let data_r = await res.json()
            vue_component.exp_docum = data_r["experimento"]
            vue_component.r_exp = true
            // vue_component.dados_marcar = data_r["experimento"]["list_banco_imagem"]

            // vue_component.$emit("experimento_data", vue_component.exp_docum)
            console.log(data_r)

            }
            pega_dados_async(vue_component, 192)
        }
    
</script>


<style scoped>
.gestaoexp{
     display: flex;
     align-items: center;
     justify-content:center;
     
}
</style>