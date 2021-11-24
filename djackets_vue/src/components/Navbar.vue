<template>
  <nav class="navbar is-dark">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item"
        ><strong>Djackets</strong></router-link
      >
      <a
        class="navbar-burger"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbar-menu"
        @click="showMobileMenu = !showMobileMenu"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span
      ></a>
    </div>
    <div
      class="navbar-menu"
      id="navbar-menu"
      v-bind:class="{ 'is-active': showMobileMenu }"
    >

      <!--search button-->
      <div class="navbar-start">
        <div class="navbar-item">
          <form method="get" action="/search">
          <div class="field has-addons">
            <div class="control">
              <input type="text" class="input" placeholder="What are you looking for?" name="query"> 
            </div>
            <div class="control">
              <button class="button is-success">
                <span class="icon">
                  <i class="fas fa-search"></i>
                </span>
              </button>
            </div>
          </div>
          </form>
        </div>
      </div>

      <!--side buttons-->
      <div class="navbar-end">
        <router-link to="/summer" class="navbar-item">Summer</router-link>
        <router-link to="/winter" class="navbar-item">Winter</router-link>
        <div class="navbar-item">
          <div class="buttons">
            <template v-if="!$store.state.isAuthenticated">
            <router-link to="/log-in" class="button is-light"
              >Log In</router-link
            >
            </template>
            <template v-else>
              <router-link to="/myaccount" class="button is-info"
              >My Profile</router-link
            >
            </template>
            <router-link to="/cart" class="button is-success">
              <span class="icon">
                <i class="fas fa-shopping-cart"></i>
              </span>
              <span>Cart ({{cartTotalLength}})</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
    name:'Navbar',
    data(){
    return{
      showMobileMenu: false,
      cart:{
        items:[]
      }
    }
  },
  mounted(){
    this.cart= this.$store.state.cart
  },
  computed:{
    cartTotalLength(){
      let totalLength= 0
      for(let i=0;i<this.cart.items.length;i++){
        totalLength+= this.cart.items[i].quantity
      }
      return totalLength
    } 
}
}
</script>