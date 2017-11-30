import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import index from '@/components/index'
import course from '@/components/course'
import courseX from '@/components/courseX'
import login from '@/components/login'
import CourseDetailPage from '@/components/CourseDetailPage'
import cart from '@/components/cart'
import buy from '@/components/buy'

// Vue.use(axios);

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/index',
      component: index
    },
    {
      path: '/course',
      name: 'course',
      component: course
    },
	  {
		  path: '/course/detail/:id/',
		  name: 'course_detail',
		  component: CourseDetailPage
		},
    {
      path: '/courseX',
      name: 'courseX',
      component: courseX
    },
    {
      path: '/cart',
      name: 'cart',
      component: cart
    },
    {
      path: '/course/buy',
      name: 'buy',
      component: buy
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
  ]
})
