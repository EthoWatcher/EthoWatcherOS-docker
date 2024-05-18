
<template>
  <div id="app"  >
    <b-navbar toggleable="lg" type="dark" variant="info"  id="nav" class="container">
    <div class="item">
      <router-link to="/">Home</router-link> |
      
    </div>
    <div class="item">
      <Login/>
    </div>
    
    </b-navbar>

  <div>
    <router-view/>
  </div>
   
  </div>
</template>

<script>
// @ is an alias to /src
import Login from '@/components/Login.vue'


export default {
  name: 'Home',
  components: {
    Login
  }
}
</script>



<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  text-decoration: none;
}
body {
  font-size: 100%;
  background: linear-gradient( 50deg, #d6d8da 30%, #fe9900ff 80%);

}
p {
  text-align: left;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.container {
	/* max-width: 400px; */
  max-width: 100%;
	margin: 0 auto;
	display: flex;
	border: 1px solid #ccc;
  justify-content: space-between;
}
/* Flex Item */
.item {
	/* O flex: 1; é necessário para que cada item se expanda ocupando o tamanho máximo do container. */
	flex: 1;
	margin: 5px;
	/* background: tomato; */
	text-align: center;
	font-size: 2.2em;
}


</style>


