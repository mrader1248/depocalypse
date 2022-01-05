import Vue from 'vue'
import VueRouter from 'vue-router'
import Inventory from '../views/Inventory.vue'
import Outlook from '../views/Outlook.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Inventory',
    component: Inventory
  },
  {
    path: '/outlook',
    name: 'Outlook',
    component: Outlook
  }
]

const router = new VueRouter({
  // The following two lines were commented out to disable the vue-router 
  // history mode (otherwise the pages would not load).
  // mode: 'history',
  // base: process.env.BASE_URL,
  routes
})

export default router
