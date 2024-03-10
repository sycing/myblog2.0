import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import home from /components/home

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: home
    }
  ]
})
