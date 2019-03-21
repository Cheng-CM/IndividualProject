<template>
  <div class="hello">
    <div class="container">
      <form class="my-5">
        <h3>Movie Info</h3>
        <ul id="movieList">
          <li>
            <b-btn variant="primary" @click="rate()">Rate</b-btn>
          </li>
        </ul>

        <ul>
          <li v-for="item in movies">{{ item.title }}</li>
        </ul>
      </form>
    </div>
  </div>
</template>

<script>
import MovieAPI from "@/api/movie.js";

export default {
  name: "compare",
  metaInfo: {
    title: "Item Page"
  },
  data() {
    return {
      el: "#movieList",
      data: {
        movies: []
      },
      movies: []
    };
  },
  methods: {
    async rate() {
      const movieIds = this.$session.get("movieIds");
      const movieIdsList = movieIds.split(",");
      for (let i = 0; i < movieIdsList.length; i++) {
        console.log();
      }
    },
    async getMovies() {
      const movieIds = this.$session.get("movieIds");
      const movieIdsList = movieIds.split(",");

      var moviesArray = [];
      for (let i = 0; i < movieIdsList.length; i++) {
        const element = movieIdsList[i];
        const res = await MovieAPI.getMovie(element);
        moviesArray[i] = res.data;
        // this.movies[i] = res.data;
      }
      this.movies = moviesArray;
      console.log(this.movies);
    }
  },
  mounted() {
    // console.log(this.$session.getAll());
    this.getMovies();
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
