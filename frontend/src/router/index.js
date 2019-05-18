import Vue from 'vue'
import VueRouter from 'vue-router'
import scale from '@/pages/scale'
import compare from '@/pages/compare'
import main from '@/pages/main'
import result from '@/pages/result'
import end from '@/pages/end'
import select from "@/pages/select";
Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [{
    name: "Main",
    path: '/',
    component: main
  }, {
    name: "Select",
    path: '/1',
    component: select
  }, {
    name: "Scale",
    path: '/2',
    component: scale
  }, {
    name: "Comparsion",
    path: '/3',
    component: compare
  }, {
    name: "Result",
    path: '/4',
    component: result
  }, {
    name: "End",
    path: '/5',
    component: end
  }]
})