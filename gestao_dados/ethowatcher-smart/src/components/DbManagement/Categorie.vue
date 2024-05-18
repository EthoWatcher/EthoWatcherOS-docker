<template>
  <div id="id_registro_categoria">
    <h2>Categories of catalog</h2>

    Add categories of the behavioral catalog
      <div>
        <input type="text" v-model="this.t_categorie" name="categorie" id="categorieNext">
        <input
          type="button"
          v-on:click="add_categorie(this.t_categorie)"
          value="Add new categorie"
        />
      </div>

    <div v-for="(categoria_l, index) in this.exp_docum.var_depend" :key="index">
      <div v-for="(categoria, j) in categoria_l.categorias" :key="j">
        {{ categoria }}
        <input
          type="button"
          v-on:click="delete_categorie(categoria_l.categorias, j)"
          value="Delete Me"
        />
      </div>
      
    </div>

    

  </div>
</template>


<script>
export default {
  props: {
    experimento: {},
  },
  data() {
    return {
      exp_docum: this.experimento,
      t_categorie: ""
    };
  },
  setup() {},
  methods: {
    delete_categorie(array, index) {
      console.log(index, array);
      array.splice(index, 1);
      console.log(this.exp_docum);
    },
    add_categorie(t_categorie){
        this.exp_docum.var_depend[0]["categorias"].push(t_categorie)
        this.t_categorie = ""

        this.$emit("update-exp_docum",this.exp_docum)

        // this.t_categorie = ""
// "exp_docum.var_depend.0.categorias"

        
    }
  },
};
</script>


<style scoped>
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
