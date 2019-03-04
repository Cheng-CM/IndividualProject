import Vue from 'vue'
import App from './App.vue'
import router from './router'
// app.js
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)

Vue.use(VueAxios, axios)

Vue.config.productionTip = false


new Vue({
  render: h => h(App),
  router
}).$mount('#app')