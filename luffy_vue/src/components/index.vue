<template>
  <div>
    <h1>{{ temp }}</h1>
  </div>
</template>

<script>
  export default {
    name: 'HelloWorld',
    data () {
      return {
        temp: "路飞学城",
        arr: [],
      }
    },
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  ul li {
    list-style-type: none;
  }

</style>
