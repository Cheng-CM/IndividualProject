<template>
  <div class="container">
    <h3>Movie Info</h3>
    <div class="container">
      <form>
        <draggable v-model="movies" @start="drag=true" @end="drag=false">
          <div v-for="(item) in movies" :key="item.id">
            <div>{{item.title}}</div>
            <img
              v-if="img[item.movieId]"
              v-bind:src="'https://image.tmdb.org/t/p/w185/' + img[item.movieId]"
            >
          </div>
        </draggable>
        <b-btn variant="primary" @click="rate()">Rate</b-btn>
      </form>
    </div>
  </div>
</template>

<script>
import MovieAPI from "@/api/movie.js";
import draggable from "vuedraggable";
export default {
  components: {
    draggable
  },
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
      movies: [],
      img: []
    };
  },
  methods: {
    rate() {
      var rating = [5,4.5,4,3.5,3.25,2.75,2.5,2,1.5,1];
      for (let i = 0; i < this.movies.length; i++) {
        const movie = this.movies[i];
        const params = {
          userId: this.$session.get("userId"),
          movieId: movie.movieId,
          rating: rating[i],
          timestamp: new Date().getTime()
        };
        MovieAPI.postcRate(params);
      }
      this.$router.push("/result");
    },
    async getMovies() {
      const movieIds = this.$session.get("movieIds");
      const movieIdsList = movieIds.split(",");
      var moviesArray = [];
      for (let i = 0; i < movieIdsList.length; i++) {
        const element = movieIdsList[i];
        const linkres = await MovieAPI.getLink(element);
        var tmdbId = linkres.data.tmdbId;
        const Imageres = await MovieAPI.getMovieImage(tmdbId);
        if (Imageres.data.posters[0] != null) {
          this.img[element] = Imageres.data.posters[0].file_path;
        }
        const res = await MovieAPI.getMovie(element);
        moviesArray[i] = res.data;
      }
      this.movies = moviesArray;
    }
  },
  mounted() {
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
