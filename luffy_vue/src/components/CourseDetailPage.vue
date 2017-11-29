<template>

  <div>
    <h4>{{ temp }}</h4>
    <ul>
      <li v-for="item in courseDetailList">{{ item }}</li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'course',
    data () {
      return {
        temp: "课程详细",
        courseDetailList: {},
      }
    },
    mounted:function () {
      this.showList()
    },
    methods:{
        showList(){
            var that = this
            this.$axios.request({
            url:that.$store.state.apiList.courseDetail+that.$route.params.id+'/',
            method:'GET',

            })
              .then(function (response) {
                  console.log(response.data.data)
                  that.courseDetailList = response.data.data

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
