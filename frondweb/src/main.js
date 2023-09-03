// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// import router from './router/HelloWorld'
import 'element-ui/lib/theme-chalk/index.css'

import VueRouter from 'vue-router'
import ElementUI from 'element-ui'

import homeCm from './pages/home'
import articleCm from './pages/article'
import aboutCm from './pages/about'
import detailCm from './pages/detail'
// import axios from 'axios'

Vue.config.productionTip = false
// axios.defaults.baseURL = process.env.VUE_APP_API

Vue.use(VueRouter)
Vue.use(ElementUI)

const routes = [
  { path: '/home', component: homeCm },
  { path: '/article', component: articleCm,
    // children:
    //   [
    //     {
    //     path: "detail",
    //     name: 'detailname',
    //     component: detailCm
    //     }
    //   ]
  },
  { path: '/about', component: aboutCm },
  { 
    path: '/detail/:id',
    name: 'detailname',
    component: detailCm
}

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
