<template>
  <div id="app">
    <router-view/>
      <b-button class="mb-4" :to="'/rating/'">Rating</b-button>
        <b-button class="mb-4" :to="'/movie/'+'5c7be1ae04f84fef47872c6a'">Movie</b-button>
  </div>
</template>


<script>
export default {
  name: "Movie",
  metaInfo: {
    title: "Movie Item Page"
  },
  components: {
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
