import { createRouter, createWebHistory } from 'vue-router'
import AnimeList from '@/views/AnimeList'
import AnimeDetail from '@/views/AnimeDetail'
import Login from '@/views/Login'
import SignUp from '@/views/SignUp'
import Profile from '@/views/Profile'

const routes = [
  {
    path: '/',
    component: AnimeList
  },
  {
    path: '/anime/:slug',
    component: AnimeDetail
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/sign-up',
    component: SignUp
  },
  {
    path: '/profile/:slug',
    component: Profile
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
