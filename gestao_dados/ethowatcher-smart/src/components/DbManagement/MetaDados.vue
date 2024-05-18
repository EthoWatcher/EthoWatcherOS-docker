<template>
    <div>
        <h2> Metadata categorie: <strong style="color: blue;">{{ var_inde.texto_interface }}</strong></h2>
        <div>
          <h3>Insert a key from this metadata categorie</h3>
            <input type="text" 
            v-model="this.t_novo_meta"
            placeholder="Insert a key from this metadata categorie"
            name="" id="">
          <input type="button" 
          v-on:click="add_new_categoria(var_inde.categorias)"
          value='Add new categorie in the metadata' />
        </div>
        
        <div class="metadata-menu">
          <h3>Keys list</h3>
        <div v-for="(vari, index) in var_inde.categorias" :key="vari" class="metadata-key">
          <p> Key: <strong style="color: blue;"> {{ vari }} </strong></p>
           
          <input
            type="button"
            v-on:click="delete_categorie(var_inde.categorias, index)"
            value="Delete this key"
          />
        </div>
        </div>
        


        

      </div>
</template>


<script>

export default {
    props:{
        var_inde: {},
        index: 0
    },
    data(){
        return{
            t_novo_meta: "",
            var_inde:this.var_inde,
            index: this.index
        }

    },
    methods:{
        delete_categorie(array, index){
          console.log(index, array)
          array.splice(index, 1)
          console.log(this.exp_docum)
          this.$emit("update_metadado", 
          {var_inde: this.var_inde
          ,index: this.index})
        },
        add_new_categoria(array){
            array.push(this.t_novo_meta)
            this.t_novo_meta = ""
        }
        
    },
    setup() {
        
    },
};
</script>


<style scoped>
h2{
  padding-bottom: 10px ;
}
input {
  min-width: 40px;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
.metadata-menu{
  padding-top: 40px;
}

.metadata-key{
  padding-bottom: 10px;
  padding-top: 10px;
}
</style>