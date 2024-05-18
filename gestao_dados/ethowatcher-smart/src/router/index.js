import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Dashboard from "../views/Dashboard.vue"
import DatabaseManagement from '../views/DatabaseManagement.vue'
import QueryDb from "../views/QueryDb.vue"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/gestaoexp/:hash',
    name: 'gestaoexp',
    component: QueryDb
  },
  {
    path: '/db_management/:hash',
    name: 'db_management',
    component: DatabaseManagement
  },
  {
    path: '/about',
    name: 'About',
    
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
