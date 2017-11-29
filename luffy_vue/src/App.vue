<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <router-link to="/index">首页</router-link>
    <router-link to="/course">课程</router-link>
    <router-link to="/courseX">luffyX</router-link>
    <router-link to="/deeptech">深科技</router-link>
    <router-link to="/login">登录</router-link>

    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
