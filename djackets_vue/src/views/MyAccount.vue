<template>
  <div class="container">
      <div class="columns is-multiline">
          <div class="column is-12">
              <h1 class="title">My Profile</h1>
          </div>
          <button @click="logout()" class="button is-danger">Log out</button>check logout method thwn delete this
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'MyAccount',
    mounted(){
        document.title='Profile | Djackets'
    },
    methods:{
        async logout(){
            this.$store.commit('setIsLoading',true)
            await axios
                .post('/api/v1/token/logout/')
                .then(response=>{
                    console.log('logged out')
                })
                .catch(error=>{
                    console.log(JSON.stringify(error))
                })
                axios.defaults.headers.common['Authorization']=''
                localStorage.removeItem('token')
                this.$store.commit('removeToken')
                this.$router.push('/')

                this.$store.commit('setIsLoading',false)
        }

    }
}
</script>

<style>

</style>