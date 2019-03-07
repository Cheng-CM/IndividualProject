<template>
  <div id="app">
    <b-button class="mb-4" :to="'/cRating/'">Scale-Rating</b-button>
    <b-button class="mb-4" :to="'/rRating/'">Comparison</b-button>
    <router-view/>
  </div>
</template>


<script>
export default {
  name: "Movie",
  metaInfo: {
    title: "Movie Item Page"
  },
  components: {}
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
