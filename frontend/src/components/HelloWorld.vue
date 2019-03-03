<template>
  <div class="hello">
    <h1>{{ this.$route.params.id }}</h1>
    <h3>Movie Info</h3>
    <ul>
      <li>{{ info.data.title }}</li>
      <li>{{ info.data.genres }}</li>
      <li>{{ info.data.movieId }}</li>
    </ul>
  </div>
</template>

<script>
import MovieAPI from "@/api/movie.js";
export default {
  name: "HelloWorld",
  metaInfo: {
    title: "Item Page"
  },
  props: {
    msg: String
  },
  data() {
    return {
      info: {
        data: {
          id: "",
          movieId: "",
          title: "",
          genres: ""
        }
      }
    };
  },
  methods: {
    async loadinfo() {
      const res = await MovieAPI.getMovie(this.$route.params.id);
      // console.log(res.data);
      this.info.data = res.data
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
