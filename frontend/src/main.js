import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Donut from 'vue-css-donut-chart';
import 'vue-css-donut-chart/dist/vcdonut.css';


import SequentialEntrance from 'vue-sequential-entrance'
import 'vue-sequential-entrance/vue-sequential-entrance.css'
Vue.use(SequentialEntrance);


import { BSpinner } from 'bootstrap-vue'
Vue.component('b-spinner', BSpinner)

Vue.use(BootstrapVue)
Vue.config.productionTip = false;

Vue.use(Donut);


new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
