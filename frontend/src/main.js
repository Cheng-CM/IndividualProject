import Vue from 'vue'
import App from './App.vue'
import router from './router'

import StarRating from 'vue-star-rating'


// LightBootstrap plugin
import LightBootstrap from './light-bootstrap-main'
Vue.use(LightBootstrap)

// app.js
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'
import VueAxios from 'vue-axios'


import {
  library
} from '@fortawesome/fontawesome-svg-core'
import {
  faSyncAlt
} from '@fortawesome/free-solid-svg-icons'

import {
  FontAwesomeIcon
} from '@fortawesome/vue-fontawesome'

library.add(faSyncAlt);
Vue.component('font-awesome-icon', FontAwesomeIcon)

import Chartist from "chartist";


import VueSession from 'vue-session'
import draggable from 'vuedraggable'
Vue.use(VueSession)
import VueWait from 'vue-wait'

Vue.use(VueWait)
Vue.component('star-rating', StarRating);

import VueNotify from 'vue-notifyjs'
import 'vue-notifyjs/themes/default.css'
Vue.use(VueNotify)

Vue.use(VueAxios, axios);

import BootstrapVue from 'bootstrap-vue'
Vue.use(BootstrapVue);

Vue.use(router);

Vue.component(draggable);

import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'

Vue.component('VueSlider', VueSlider)

Vue.component('jsx-example', {
  render (h) { // <-- h must be in scope
    return <div id="foo">bar</div>
  }
})

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  data: {
    Chartist: Chartist
  },
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