import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieMain from '@/components/MovieMain'
import UserPost from '@/components/UserPost'
Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [{
      name: "movie",
      path: '/movie/:id',
      component: MovieMain
    }, {
      name: "5starRate",
      path: '/rating',
      component: UserPost
    },

  ]
})