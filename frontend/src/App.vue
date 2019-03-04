<template>
  <div id="app">
    <!-- <MovieMain/> -->
    <UserPost/>
  </div>
</template>


<script>
// import MovieMain from "./components/MovieMain.vue";
import UserPost from "./components/UserPost.vue";
export default {
  name: "Movie",
  metaInfo: {
    title: "Movie Item Page"
  },
  components: {
    // MovieMain,
    UserPost
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
