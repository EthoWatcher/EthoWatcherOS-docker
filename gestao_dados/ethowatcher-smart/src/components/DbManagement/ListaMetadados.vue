<template>

<div id="listajuncao">
  <h2>Metadata list</h2>
  <div class="metada-list">
    <div class="metada-list-item"
      v-for="(var_inde, j) in this.exp_docum.var_inde"
      :key="j"
      
    >
      
        <MetaDados
          @update_metadado="handle_update_metadado"
          v-bind:var_inde="var_inde"
        />

        <h3>Delete this metadata categorie</h3>
        <input
          type="button"
          v-on:click="delete_categorie(this.exp_docum.var_inde, j)"
          value="Delete metadado categorie"
        />
    </div>
  </div>
</div>
</template>


<script>
import MetaDados from "../DbManagement/MetaDados.vue";
export default {
  components: {
    MetaDados,
  },
  props: {
    experimento: {},
  },
  data() {
    return {
      exp_docum: this.experimento,
    };
  },
  methods: {
    handle_update_metadado(metadado) {
      this.exp_docum.var_inde[metadado["index"]] = metadado["var_inde"];
    },

    delete_categorie(array, index) {
      array.splice(index, 1);
    },
  },
  setup() {},
};
</script>


<style scoped>
.metada-list{
  display: flex;
  flex-wrap: wrap;
  margin: 20px;
  justify-content: space-evenly;
  /* background: red; */
  border-style: ridge;
}
input {
  min-width: 40px;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

.metada-list-item{
  margin: 20px;
  /* background: firebrick; */
  border-style: ridge;
}
</style>
