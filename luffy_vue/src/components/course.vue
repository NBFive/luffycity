<template>

  <div>
    <h1>{{ temp }}</h1>
    <router-link :to="{'path':'/course/detail/'+item.id }" v-for="item in courseList" :key="item.id">
      <h4 class="course-tit">{{item.name}}</h4>
      <p class="course-dec">{{item.brief}}</p>
      <span class="course-lever">难度：{{item.level}}</span>
    </router-link>
  </div>
</template>

<script>
  export default {
    name: 'course',
    data () {
      return {
        temp: "课程列表",
        courseList: {},
      }
    },
    mounted: function () {
      this.showList()
    },
    methods: {
      showList(){
        var that = this
        this.$axios.request({
          url: this.$store.state.apiList.course,
          method: 'GET',
        })
          .then(function (response) {
            console.log(response.data.data)
            that.courseList = response.data.data

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
