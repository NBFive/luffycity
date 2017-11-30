<template>
  <div>
    <h4>{{ temp }}</h4>
    <ul v-for="item in cartDict">
      <li>
        <span>{{item.name}}</span>
        <span>{{item.selected_policy_id}}</span>
        <span>
          <select name="" id="">
            <option value="" v-for="se in item.policy_list">{{se}}</option>
          </select>
        </span>
      </li>
      <hr>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'cart',
    data() {
      return {
        temp: "购物车",
        cartDict: {},

      }
    },
    mounted: function () {
      this.showList()
    },
    methods: {
      showList() {
        var that = this
        this.$axios.request({
          url: that.$store.state.apiList.cart,
          method: 'GET',
        })
          .then(function (response) {
            that.cartDict = response.data
          })
      },
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  ul li {
    list-style-type: none;
  }
</style>
