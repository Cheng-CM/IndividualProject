import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [
    {
        name: "movie",
        path: '/movie/:id',
        component: HelloWorld
    }
  ]
})