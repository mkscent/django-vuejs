import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'

new Vue({
  el: '#app',
  beforeCreate () {
    Vue.prototype.$http = axios
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    axios.defaults.xsrfCookieName = 'csrftoken'
  },
  render: h => h(App)
})
