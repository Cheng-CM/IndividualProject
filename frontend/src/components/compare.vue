<template>
  <div class="hello">
    <div class="container">
      <form class="my-5">
        <h3>Movie Info</h3>
        <ul>
        </ul>
        or
        <ul>
        </ul>
      </form>
    </div>
  </div>
</template>

<script>
import MovieAPI from "@/api/movie.js";
export default {
  name: "scale",
  metaInfo: {
    title: "Item Page"
  },
  data() {
    return {
    };
  },
  methods: {
    async rate() {
    },
    async loadinfo() {
    }
  },
  mounted() {
    this.loadinfo();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
