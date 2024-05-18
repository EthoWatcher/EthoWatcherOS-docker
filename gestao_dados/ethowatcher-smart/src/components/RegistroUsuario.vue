<template>
    <div id="RegistroUsuario">
        <h2> Register new user</h2>
        To start using the program you will need a user, fill the follow form and then click in "Register new user" button. After your registration to to dashboard area to start gathering your data.
        <div id="FormUser">
            <div>
                <input v-model="user_data['nome']" placeholder="Name">
            </div>
            <div>
                <input v-model="user_data['lab']" placeholder="Laboratory">
            </div>
            <div>
                <input v-model="user_data['login']" placeholder="Username">
            </div>
            <div>
                <input v-model="user_data['senha']" placeholder="Password">
            </div>
            <div>
                <input type="button" v-on:click="register_new_user()" value="Register new user">
            </div>
            

        </div>
    </div>
    

</template>


<script>
import { get_url } from '../services/url'

export default({
    data(){
        return{
            r_registrado:false,
            user_data:{"login": "", 
                        "lab": "", 
                        "nome": "",
                        "senha": ""}
        };
    },
    setup() {
        
    },
    methods:{
        register_new_user(){
            privada(this)
            this.user_data = {"login": "", 
                        "lab": "", 
                        "nome": "",
                        "senha": ""}

            
        }
    }
})


function privada(vue) {
  async function fun_asincrona(vue) {
    // let params = {
    //   id_experimento: id_experimento,
    // };
    let params = vue.user_data
    // let data = localStorage.getItem("access_token");

    // this = vue_component
    // vue_component.r_logado = true
    const res = await fetch(get_url () + "/api/create_user", {
      method: "POST",
      // credentials: "include",
      headers: new Headers({
        "content-type": "application/json",
        // Authorization: "Bearer " + data,
      }),
      body: JSON.stringify(params),
    });
    const data2 = await res.json();
    console.log(data2)

  }

  fun_asincrona(vue);
}
</script>

<style scoped>
input{
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}
</style>