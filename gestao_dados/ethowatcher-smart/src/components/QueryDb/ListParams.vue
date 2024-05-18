<template>
    
<!-- <ul class="object administrator-checkbox-list"> -->

    <div class="depen-menu">
        <div v-for="(module, index) in this.ls_params" :key="index" class="depen-menu-item">
        <label v-bind:for="module.id">
        <input
            type="checkbox"
            v-model="module.checked"
            v-bind:id="module.id"
            v-on:change="this.mudou_estado()"
        />
        <span>{{ module.name }}</span>
        </label>
    </div>

    </div>

<!-- </ul> -->


</template>




<script>


export default {
    props:{
        ls_params : [],
        par_name :"",
        
    },
    data(){
        return{
            ls_params: this.ls_params,
            query_list: {}
        }
    },
    methods:{
        mudou_estado(){
            let ls = this.ls_params.filter(e => e.checked).map(
                e =>{
                    return e['key']

                }
            )
            let  ds = {}
            ds[this.par_name] = ls
            this.query_list = ds
            console.log(this.query_list )


            this.$emit("update_var_de", this.query_list)
            // console.log(d_s)
        }
    },
    data(){

    },
    setup() {
        
    },
}
</script>


<style scoped>
li{
    list-style-type: none;
}

input {
  min-width: 40px;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}

.depen-menu{
    display: flex;
    flex-wrap: wrap;

}
.depen-menu-item{
    min-width: 50px;
}
</style>