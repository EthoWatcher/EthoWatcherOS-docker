<template>
  <div class="oi">
    <h2>Welcome to the Ewthowatcher smart</h2>
    <div class="content-main">
      <div class="content-main-item">
        <p>
          Here you will gathering your behavioral data (categorical and morpho-kinecic data) to make smaller datasets to be use in
          explore the data, make statistical models and to train machine learning models.
        </p>
        <p>
          This software (include this website) you can run one copy on your lab
          internal network (see how)
        </p>

        
        <p>This swoftware was make by João A. Marcolan as part off your doctoral studies under the supervision of José Marino Neto 
          in <a href="http://www.ieb.ufsc.br/?page_id=139">Instituto de Engenharia Biomédica</a> 
        </p>
        <p>
           To refear about this work, and find more information about, use:

        </p>

        <RegistroUsuario />

      </div>

      <div class="content-main-item">
        <p>
          To start using do you will need to register behavioral data in
          EthoWatcher OS <a href="https://github.com/EthoWatcher/ethowatcher/wiki">(dowload a copy here).</a>
        </p>
        <p> If do you have some questions, <a href="https://github.com/EthoWatcher/ethowatcher/issues"> use our forum to ask questions.</a> </p>
        <img src="@/assets/etowatcheros.png" alt="" srcset="">
        

        
        

      </div>
    </div>

    
  </div>
</template>


<script>
import RegistroUsuario from "../components/RegistroUsuario.vue";

export default {
  components: {
    RegistroUsuario,
  },
  setup() {},
};
</script>


<style scoped>
.content-main{
  display: flex;
  margin: 80px;

  justify-content: space-around;
}

p{
  margin: 10px;
}

img {
  display: block;
  max-width:800px;
  max-height:800px;
  width: auto;
  height: auto;
  margin: 40px;
}
</style>