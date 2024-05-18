<template>
    
        <select v-model="this.selected" @change="change_cate" >
            <option disabled value="">Please select one {{this.metadado['texto_interface']}}</option>
            <option v-for="(categoria, index) in this.metadado['categorias']" 
            :key="index"
            v-bind:value="{'cat': categoria}"
            >
            {{categoria}}
            </option>
            <option value="{'cat':'all'}"> All</option>
            
        </select>
        <!-- <span ref='someRef'>Selected: {{ this.selected }}</span> -->
</template>


<script>


export default {
    props:{
        metadado:{},
        index: 0
    },
    data(){
        return{
            selected:{},
            query:{}
        }
        
    },
    setup() {
        
    },
    methods:{
        change_cate(){
            let r_all = this.selected['cat'] == 'all'
            let saida = {}
            if(r_all){

            }else{
                
            let str = "var_ind." + this.metadado["nome"] //{"var_ind.dosagem": "flx2.5mg"}
            saida[str] = this.selected['cat']
            console.log(saida)

            this.$emit("mudo_metada", saida, this.index)

            }
            
        }
    }

}
</script>


<style scoped>
select {
  min-width: 40px;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
</style>