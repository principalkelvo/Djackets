<template>
  <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank you</h1>
                <p>Your order will be processed within 48hrs</p>
            </div>
        </div>
  </div>
</template>

<script>
export default {
    name:'Success',
    mounted(){
        document.title='Success | Djackets'
        this.trialLoad()
    },
    methods:{
        trialLoad(){
            if( window.localStorage )
        {
            if( !localStorage.getItem('firstLoad') )
            {
            localStorage['firstLoad'] = true;
            window.location.reload();
            }  
            else
            localStorage.removeItem('firstLoad');
        }
        }
    }
}
</script>

<style>

</style>