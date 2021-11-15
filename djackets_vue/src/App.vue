<template>
  <div id="wrapper">
    <Navbar/>
    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading':$store.state.isLoading}">
      <div class="skewloader">
        <div class="skewloader_mask">Loading</div>
        <div class="skewloader_mask">Loading</div>
        <div class="skewloader_mask">Loading</div>
        <div class="skewloader_mask">Loading</div>
        <div class="skewloader_mask">Loading</div>
        <div class="skewloader_mask">Loading</div>
        <div class="skewloader_mask">Loading</div>
        <div class="skewloader_mask">Loading</div>
        <div class="skewloader_mask">Loading</div>
        <div class="skewloader_mask">Loading</div>
      </div>
    </div>
    <section class="section">
      <router-view/>
    </section>
    <Footer/>
  </div>
</template>
<script>
import axios from 'axios'

import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
export default {
  name: 'App',
  
  components:{
    Navbar,
    Footer
  },
  beforeCreate(){
    this.$store.commit('initializeStore')
    
    const token= this.$store.state.token

    //check if token exists
    if(token){
      axios.defaults.headers.common['Authorization']= "Token "+ token
    }
    //if you are not authenticated
    else{
      axios.defaults.headers.common['Authorization']= " "
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

$baseColor: rgba(30, 40, 50, 1);

.is-loading-bar {
  background: white;
  height: 100vh;
  overflow: hidden;
  display: flex;
  font-family: 'Anton', sans-serif;
  justify-content: center;
  align-items: center;
  color: #fff;
  font-size: 2.375rem;
}

.skewloader {
  &_mask {
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 125px;
    height: 125px;
    position: absolute;
    transform: translate(-50%, -50%);

    background: $baseColor;
    
    &::before {
      // content: '';
      position: absolute;
      height: 0;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.99);
      border-radius: 100%;
      background: $baseColor;
    }
    
    @for $i from 1 through 10 {
      &:nth-child(#{$i}) {
        z-index: 11 - $i;
        clip-path: circle(($i * 10 / 2) + 0%);
        animation: rotate 3000ms $i * 150ms ease-in-out infinite;
        
        &::before {
          width: ($i - 1) * 10%;
          padding-top: ($i - 1) * 10%;
        }
      }
    }
  }
}

@keyframes rotate {
  0% {
    transform: translate(-50%, -50%) rotateZ(0deg);
  }
  
  50% {
    transform: translate(-50%, -50%) rotateZ(360deg);
  }
  
  100% {
    transform: translate(-50%, -50%) rotateZ(360deg);
  }
}

.is-loading-bar{
    height:0px;
    overflow: hidden;
    -webkit-transition: all 1.3s;
    transition: all 1.3s;
    opacity:0;
    
      &.is-loading{

        height: 130px;
        opacity:100%;
      }
}
</style>
