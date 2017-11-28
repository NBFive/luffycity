<template>
  <div>

    <p>{{ temp }}</p>

    <div>
      <ul>
        <li>姓名：<input type="text" v-model="username"></li>
        <li>密码：<input type="password" v-model="password"></li>
      </ul>
      <input type="button" value="提交" v-on:click="auth">
    </div>
  </div>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        temp: "欢迎登陆",
        username: '',
        password: '',
      }
    },

    methods: {
      auth(){
        var that = this;
        this.$axios.request({
          url:this.$store.state.apiList.login,
          method:'POST',
          data:{
              username:this.username,
              password:this.password,
          },
        })
          .then(function (response) {
//              console.log(response.data);
              if (response.data.user){
                  var user = response.data.user;
                  var token = response.data.token;
                  that.$store.commit('saveToken',{'user':user,'token':token});
//                  console.log(that.$store.state.token)
                  that.$router.push('/')
              }
              else{
                  that.$router.push('/login')
              }
        })
          .catch(function (error) {
            console.log(error)
          })


      }
    }
  }
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  ul li{
    list-style-type: none;
  }

</style>
