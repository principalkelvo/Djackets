<template>
  <div class="home">
    <!--header-->
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">Welcome to Djackets</p>
        <p class="subtitle">The best jacket store online</p>
      </div>
    </section>
    <!--list of produts-->
    <div class="columns is-multiline">
    
        <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">latest products</h2>
        </div>

        <!--later change to component (products)-->
        <div
          class="column is-3"
          v-for="product in latestProducts"
          v-bind:key="product.id"
        >
        <!--a little shadow around-->
        <div class="box">
          
          <!--a little space below-->
          <figure class="image mb-4">
            
            <img v-bind:src="product.get_thumbnail" />
          </figure>
          <h3 class="is-size-4">{{ product.name }}</h3>
          <p class="is-size-6 has-text-grey">${{ product.price }}</p>

          <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View details</router-link>
          
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//connect to the backend
import axios from 'axios'
export default {
  name: "Home",
  data(){
    return{
      latestProducts:[]
    }
  },
  components: {},
  mounted(){
    this.getLatestProducts()
    document.title= 'Home | Djackets'
  },
  methods:{
    async getLatestProducts(){
      this.$store.commit('setIsLoading',true)
      await axios
        .get('/api/v1/latest-products/')
        .then(response=>{
          this.latestProducts= response.data
        })
        .catch(error=>{
          console.log(error)
        })


        this.$store.commit('setIsLoading',false)
    }
  }
};
</script>
<style scoped>
.image{
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
}
</style>