import Vue from 'vue'
import VueRouter from 'vue-router'
import scale from '@/components/scale'
import compare from '@/components/compare'
import main from '@/components/main'
import result from '@/components/result'
import end from '@/components/end'
Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [{
    name: "Scale",
    path: '/rRating',
    component: scale
  }, {
    name: "Comparsion",
    path: '/cRating',
    component: compare
  },
  {
    name: "Main",
    path: '/main',
    component: main
  }, 
  {
    name: "Result",
    path: '/result',
    component: result
  },
  {
    name: "End",
    path: '/end',
    component: end
  },

  ]
})