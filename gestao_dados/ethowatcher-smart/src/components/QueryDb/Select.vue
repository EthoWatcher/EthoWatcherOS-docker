<template>
    <div>
        <h2>Metadata categorie: {{this.metadado.texto_interface}}</h2>
        
        <div v-for="(s, index) in this.ls_or" :key="index"> 
            <DropMenu :metadado="s['metadado']" v-bind:index="index" v-on:mudo_metada="mudo_metada"/>
            
        </div>
        <input type="button" v-on:click="add_new_categorie" value="Add an or in this categorie metada">
        <input type="button" v-on:click="delete_categorie(0)" value="Delete last or menu">
        

    </div>
    

</template>


<script>
import DropMenu  from "./DropMenu.vue";

export default {
    components:{
        DropMenu
    },
    props:{
        metadado:{}
    },
    data(){
        return{
            selected:{},
            query:{},
            ls_or: []
        }
        
    },
    mounted(){
        // this.ls_or.push(this.metadado)
    },
    setup() {
        
    },
    methods:{
        mudo_metada(query, index){
            console.log(query, index)
            this.ls_or[index]["meta_selected"] = query
            console.log(this.ls_or)
            let keys = Object.keys(query)

            keys.forEach(chave =>{
                let r_tem_mais_q_1 = this.ls_or.length > 1
                let arruma_lista = this.ls_or.map(e => e["meta_selected"]) 
                let di_saida = {}
                if(r_tem_mais_q_1){
                    di_saida[chave] = {"$or": arruma_lista}
                
                    console.log("qnd_muit", di_saida)

                }else{
                    di_saida[chave] = {"$or": arruma_lista[0]}

                    
                }
                this.$emit("mudo_metada", di_saida)

            })

            

        },
        delete_categorie(index){
            // this.ls_or.splice(index, 1)
            this.ls_or.pop()
        },
        add_new_categorie(){
            this.ls_or.push({"metadado": this.metadado, "meta_selected":{}})
            // this.$emit("mudo_metada", saida)
        
            }
    
        }
    }

</script>


<style scoped>
input {
  min-width: 40px;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
</style>