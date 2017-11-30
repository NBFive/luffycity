<template>
  <div>
    <h4>{{temp}}</h4>
    <div v-for="(item,key) in buyDict">
      <p>{{item.course.img}}</p>
      <p>{{item.course.name}}</p>
      <p>{{item.name}}</p>
      <p>{{item.price}}</p>
      <div>折后价：<p class="single_price">{{item.price}}</p></div>
    </div>
    <div>总价：
      <div id="total_price">{{total_amount}}</div>
    </div>
    <button v-on:click="pay">确认支付</button>
  </div>
</template>

<script>
  export default {
    name: 'buy',
    data() {
      return {
        temp: "结算页面",
        buyDict: {},
        total_amount: 0,
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
            that.buyDict = response.data
            console.log(that.buyDict)
            for (let i in that.buyDict) {
              console.log(that.buyDict[i])
              that.total_amount += that.buyDict[i]['price']
            }
            that.total_amount = that.total_amount.toFixed(2)
          })
      },
      pay() {
        let that = this
        this.$axios.request({
          url: that.$store.state.apiList.pay,
          method: 'POST',
//          headers: {
//            'Content-Type': 'multipart/form-data'
//          },
//          contentType:'multipart/form-data',
          data: {
            subject: '模拟订单1',
            out_trade_no: '自定义订单号1',
            money: that.total_amount,
          }
        }).then(function (response) {
          location.href = response.data.url
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
