import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
]

const router = new VueRouter({
  // The following two lines were commented out to disable the vue-router
  // history mode (otherwise the pages would not load).
  // mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
