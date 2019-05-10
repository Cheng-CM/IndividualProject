import Vue from 'vue'
import App from './App.vue'
import router from './router'
import StarRating from 'vue-star-rating'
// app.js
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

import BootstrapVue from 'bootstrap-vue'
import VueSession from 'vue-session'
import draggable from 'vuedraggable'
Vue.use(VueSession)
import VueWait from 'vue-wait'

Vue.use(VueWait)
Vue.component('star-rating', StarRating);
Vue.use(VueAxios, axios);
Vue.use(BootstrapVue);
Vue.use(router);


Vue.component(draggable);


Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  wait: new VueWait({
    // Defaults values are following:
    useVuex: false, // Uses Vuex to manage wait state
    vuexModuleName: 'wait', // Vuex module name

    registerComponent: true, // Registers `v-wait` component
    componentName: 'v-wait', // <v-wait> component name, you can set `my-loader` etc.

    registerDirective: true, // Registers `v-wait` directive
    directiveName: 'wait', // <span v-wait /> directive name, you can set `my-loader` etc.

  }),
}).$mount('#app')