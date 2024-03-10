import { createRouter, createWebHistory } from 'vue-router'
import PageIndex from '../components/PageIndex.vue'
import PageTest from '../components/PageTest.vue'
import IndexChildPreProcess from '../views/IndexChildPreProcess.vue'
import IndexChildFaceDetection from '../views/IndexChildFaceDetection.vue'
import IndexChildPoseEstimation from '../views/IndexChildPoseEstimation.vue'
import IndexChildDockerDispatch from '../views/IndexChildDockerDispatch.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      redirect:'/index'
    },
    {
      path: '/index',
      name: 'index',
      component: PageIndex,
      children:[
        {
            path: '/test',
            name:'test',
            component:PageTest,
        },
        {
            path: '/preprocess',
            name:'preprocess',
            component:IndexChildPreProcess,
        },
        {
            path: '/detection',
            name:'detection',
            component:IndexChildFaceDetection,
        },
        {
            path: '/estimation',
            name:'estimation',
            component:IndexChildPoseEstimation,
        },
        {
            path: '/dispatch',
            name:'dispatch',
            component:IndexChildDockerDispatch,
        },
      ]
    },
  ]
}
)

export default router
