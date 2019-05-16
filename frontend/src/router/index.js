import Vue from 'vue'
import VueRouter from 'vue-router'
import scale from '@/components/scale'
import compare from '@/components/compare'
import main from '@/components/main'
import result from '@/components/result'
import end from '@/components/end'
import select from "@/components/select";
Vue.use(VueRouter)

export default new VueRouter({
  mode: 'history',
  routes: [{
    name: "Main",
    path: '/0',
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