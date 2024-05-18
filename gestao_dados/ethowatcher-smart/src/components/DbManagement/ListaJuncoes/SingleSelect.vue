<template>
    
    <div>
        
        <select v-model="this.selected" @change="change_cate" >
            <option disabled value="">Please select one {{this.metadata['texto_interface']}}</option>
            <option v-for="(categoria, index) in this.metadata['categorias']" 
            :key="index"
            v-bind:value="{'cat': categoria}"
             >
            {{categoria}}
            </option>
        </select>
        <!-- <span ref='someRef'>Selected: {{ this.selected }}</span> -->
    </div>
    
</template>


<script>


export default {
    props:{
        metadata: [],
        var_inde: {},
        juncao: {}
    },
    methods:{
        change_cate(){
            console.log(this.selected)
            console.log(this.selected)

            let saida = {}
            saida[String(this.metadata['nome'])] = this.selected["cat"]

            // this.r_ja_selecionado = String(this.metadata['nome']) in this.juncao.var_ind
            this.$emit("selected_key_metadado", saida)


        }
    },
    data(){
        return{
            selected: {},
            r_selecionado_metadado: false,
            r_ja_selecionado: false
            
        }
    },

    setup() {
        
    },
    mounted(){

        let lis_keys =  Object.keys(this.var_inde)
        // let lis_keys_str = lis_keys.map( e=> String(e))
        let key_metadata =  String(this.metadata['nome'])
        let ja_selecionado = lis_keys.findIndex( e=> e == key_metadata) != -1
        this.r_ja_selecionado = ja_selecionado
        console.log(this.r_ja_selecionado)

        // this.r_ja_selecionado = String(this.metadata['nome']) in this.juncao.var_ind
        // console.log(this.r_ja_selecionado)

    },
    computed(){
        // let lis_keys =  Object.keys(this.var_inde)
        // let lis_keys_str = lis_keys.map( e=> String(e))
        // let key_metadata =  String(this.metadata['nome'])
        // this.r_selecionado_metadado = lis_keys_str.findIndex(key_metadata) != -1
    
        

    
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