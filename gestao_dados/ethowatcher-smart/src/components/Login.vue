
<template>
    <div class="login">
        <div v-if = "r_logado ==true" class="container row">
            <div>
                <router-link to="/dashboard">Dashboard</router-link>
            </div>
            <div>
                <button class="item" v-on:click="sair_usuario" variant="success">Leave</button>

            </div>
            
            
            

        </div>
        
        <div v-else-if="r_logado == false" class="container row">
            <h2 class="item">Login</h2>
            <input v-model="login" placeholder="Insert your username" class="item">
            <input v-model="senha" placeholder="Insert your password" type="password" class="item">
            <button v-on:click="fazer_login()" variant="success" class="item">Enter</button>
            
        </div>
        
    </div>
    
</template>



<script>
// import get_url from "../assets/url"
import { get_url } from '../services/url'


export default {
    data() {
        return{
                r_logado:false,
                login: "",
                senha: "",
                nome: ""
        }
       
    },
    mounted() {
        console.log("rodou antes do componeten")
        let data =  localStorage.getItem("access_token");
        let r_exite_toke_logado = data != undefined
        if (r_exite_toke_logado){
            this.r_logado = true
        }
        this.$emit("update_usuario", this.r_logado)

    },

     methods:{
        ir_area_privada(){
            this.$emit("ir_area_privada")
        },
        sair_usuario(){
            localStorage.removeItem("access_token");
            this.r_logado = false

            this.$emit("update_usuario", this.r_logado)

        },
         fazer_login() {
            async function fun_asincrona(vue_component){
                console.log(vue_component)
                // this = vue_component
                // vue_component.r_logado = true
                // console.log(get_url())
                const res = await fetch( get_url() + "/login", {
                method: "POST",
                // credentials: "include",
                headers: new Headers({
                    "content-type": "application/json"
                }),
                body: JSON.stringify({
                    username: vue_component.login,
                    password: vue_component.senha
                })

            })
                const data = await res.json()
                console.log(data)
            if (data['logado']) {
                localStorage.setItem("access_token", data['access_token']);
                vue_component.r_logado = true
                vue_component.$emit("update_usuario", vue_component.r_logado)
                

            }else{
                console.log("algo errado")
                vue_component.r_logado = false
                vue_component.$emit("update_usuario", vue_component.r_logado)
                
                //  console.log(data)
                //  console.log("Oi mundo")
            }

             }
             fun_asincrona(this)
            
            // console.log(this)
            
            // this.nome = "João"
        //    validar_usuario_senha(this.login, this.senha)
            // this.r_logado = true
            // let emit_loco = this.$emit
            // let f_cal_com_contexto = (r_logado) =>{
            //     this.r_logado = r_logado
            //     emit_loco("update_usuario", this.r_logado)
            //     // this.$emit("update_usuario", this.r_logado)
            // }
            
            // const res = fetch("http://127.0.0.1:5000/login", {
            //     method: "POST",
            //     // credentials: "include",
            //     headers: new Headers({
            //         "content-type": "application/json"
            //     }),
            //     body: JSON.stringify({
            //         username: this.login,
            //         password:  this.senha
            //     })

            // }).then((response)=> {
            //     console.log(this)
            //      response.json().then((data) => {
            //      console.log(data)

            //      })

            // })
            // const data = res.json().then(data=>{
            //     console.log(data)
            // })
            
            // .then((response)=> {

            //     if (response.status !== 200){
            //     console.log(response)
            //     }
            //     response.json().then((data) => {
            //         console.log(data)
            //         if (data["error"]){
            //             console.log("algo errado")
            //         }else{
            //             localStorage.setItem("access_token", data["access_token"]);
            //         }
            //         // conect()
                    
                    
            //         // acessando_protegido(data)
            //     })
                

            // }).catch((error) => {
            //     console.log('Request failed', error)
            // });

            // if (data["error"]){
            //     console.log("algo errado")
            //     this.r_logado = false
            //     this.$emit("update_usuario", this.r_logado)
            // }else{
            //     localStorage.setItem("access_token", data["access_token"]);
            //     this.r_logado = true
            //     this.$emit("update_usuario", this.r_logado)
            //     //  console.log(data)
            //     //  console.log("Oi mundo")
            // }

           
           
            


        },
        acessando_protegido(){
            let data =  localStorage.getItem("access_token");
            fetch("/protected", {
                method: "GET",
                // credentials: "include",
                headers: new Headers({
                    // "content-type": "application/json",
                    'Authorization': 'Bearer ' + data
                })
                
                }).then(function(response) {

                if (response.status !== 200){
                    console.log(response)
                }else{
                    response.json().then(data =>{
                    console.log(data)
                })

                }})
        }
    
    }
}

function validar_usuario_senha(usuario,senha){
    // let myHeaders = new Headers();
    // myHeaders.append("Content-Type", "application/json")
    // r_logado = this.r_logado
    fetch("/login", {
        method: "POST",
        // credentials: "include",
        headers: new Headers({
            "content-type": "application/json"
        }),
        body: JSON.stringify({
            username: usuario,
            password: senha
        })
   
    }).then(function(response) {

        if (response.status !== 200){
        console.log(response)
        }
        response.json().then(data =>{
            console.log(data)
            localStorage.setItem("access_token", data["access_token"]);
            
            // acessando_protegido(data)
        })
        

    });
}


</script>

<style scoped>
.login{
    display: flex;
    flex-direction: row;
    
}
.container {
	/* max-width: 400px;
	margin: 0; */
	display: flex;
	border: 1px solid #ccc;
    justify-content: flex-end;
}
.item {
    max-width: 200px;
    font-size: 14px;
}
input{
    width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
}




</style>