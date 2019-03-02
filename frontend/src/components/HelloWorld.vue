<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h3>Movie Info</h3>
    <ul>
      <li>{{ info.data.title }}</li>
      <li>{{ info.data.genres }}</li>
      <li>{{ info.data.movieId }}</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import MovieAPI from "@/api/movie"
export default {
  name: "HelloWorld",
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
      await axios
        .get("http://localhost:8000/api/Movies/" + this.$route.params.id)
        .then(response => (this.info = response));
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
