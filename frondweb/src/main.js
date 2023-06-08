// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// import router from './router/HelloWorld'
import 'element-ui/lib/theme-chalk/index.css'

import VueRouter from 'vue-router'
import ElementUI from 'element-ui'

import movie from './components/home.vue'
import novel from './components/articlelist.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)
Vue.use(ElementUI)

const routes = [
  // { path: '/movie', component: movie },
  { path: '/novel', component: novel }
]

const router = new VueRouter({
  mode: 'history',
  routes 
})

/* eslint-disable no-new */
// new Vue({
//   el: '#app',
//   router,
//   components: { App },
//   template: '<App/>'
// })

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
