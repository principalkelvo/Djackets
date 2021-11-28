<template>
  <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
            
            <!--table-->
            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            v-bind:key="item.product.id"
                        >
                            <td>{{item.product.name}}</td>
                            <td>${{item.product.price}}</td>
                            <td>{{item.quantity}}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{cartTotalLength}}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>
        </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'Checkout',
    data(){
        return{
            cart:{
                items:[]
            },
            stripe:{},
            card:{},
            first_name:'',
            last_name:'',
            email:'',
            phone:'',
            errors:[]
        }
    },
    mounted(){
        document.title='Checkout | Djackets'
        this.cart= this.$store.state.cart
    },
    methods:{
        getItemTotal(item){
            return item.quantity*item.product.price
        }
    },
    computed:{
        cartTotalLength(){
            return this.cart.items.reduce((acc,curVal)=>{
                return acc+= curVal.quantity
            },0)
        },
        cartTotalPrice(){
            return this.cart.items.reduce((acc,curVal)=>{
                return acc+= curVal.product.price*curVal.quantity
            },0)
        }
    }

}
</script>

<style>

</style>