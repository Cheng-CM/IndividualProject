import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieMain from '@/components/MovieMain'
Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [
    {
        name: "movie",
        path: '/movie/:id',
        component: MovieMain
    }
  ]
})