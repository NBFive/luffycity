import Vue from 'vue'
import Vuex from 'vuex'
import Cookie from 'vue-cookies'

Vue.use(Vuex)

export default new Vuex.Store({
  // 组建中通过this.$store.state.username调用
  state:{
    username: Cookie.get('user'),
    token:Cookie.get('token'),
    apiList:{
      login: 'http://127.0.0.1:8000/auth/',
      course:'http://127.0.0.1:8000/course/',
      courseDetail:'http://127.0.0.1:8000/course/detail/',
      buy:'http://127.0.0.1:8000/course/buy/',
    }
  },
  mutations:{
    // 组建中通过this.$store.commit(saveToken,参数)
    saveToken:function (state, obj) {
      state.username = obj.user
      Cookie.set("user",obj.user,"20min")
      Cookie.set("token",obj.token,"20min")
    },
    clearToken:function (state) {
      state.username = null
      Cookie.remove('user')
      Cookie.remove('token')
    }
  }
})
