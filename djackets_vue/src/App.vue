<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Djackets</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu=!showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span></a>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/summer" class="navbar-item">Summer</router-link>
          <router-link to="/winter" class="navbar-item">Winter</router-link>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Log In</router-link>
              <router-link to="/cart" class="button is-success">
              <span class="icon">
                <i class="fas fa-shopping-cart"></i>
              </span>
              <span>cart</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view/>
    </section>
    <footer class="footer">
      <p class="has-text-centered">Copyright <i class="fa fa-copyright" aria-hidden="true"></i> 2021</p>
    </footer>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  data(){
    return{
      showMobileMenu: false,
    }
  },
  beforeCreate(){
    this.$store.commit('initializeStore')

    //check if token exists
    if(this.$store.state.token){
      axios.defaults.headers.common['Authorization']= "Token "+ this.$store.state.token
    }
    //if you are not authenticated
    else{
      axios.defaults.headers.common['Authorization']= ""
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
