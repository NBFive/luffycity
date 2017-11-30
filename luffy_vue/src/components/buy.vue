<template>
  <div>
    <h4>{{temp}}</h4>
    <ul v-for="item in buyDict">
      <li></li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'buy',
    data() {
      return {
        temp: "结算页面",
        buyDict: {},
      }
    },
    mounted: function () {
      this.showList()
    },
    methods: {
      showList() {
        let that = this
        this.$axios.request({
          url: that.$store.state.apiList.buy,
          method: 'GET',
        })
          .then(function (response) {
            console.log(response.data)
          })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  ul li {
    list-style-type: none;
  }
</style>
