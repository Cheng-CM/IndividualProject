<template>
  <div class="hello">
    <div class="container">
      <form class="my-5">
        <h3>Movie Info</h3>
        <draggable v-model="movies" @start="drag=true" @end="drag=false" >
          <div class="container" v-for="(item) in movies" :key="item.id">
            {{item.title}}
            <img
              v-bind:src="'https://image.tmdb.org/t/p/w185/' + img[item.movieId]"
            >
          </div>
        </draggable>
        <ul>
          <li>
            <b-btn variant="primary" @click="rate()">Rate</b-btn>
          </li>
        </ul>
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
      var rating = 5;
      for (let i = 0; i < this.movies.length; i++) {
        const movie = this.movies[i];
        const params = {
          userId: this.$session.get("userId"),
          movieId: movie.movieId,
          rating: rating,
          timestamp: new Date().getTime()
        };
        MovieAPI.postcRate(params);
        rating -= 0.5;
      }
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
        this.img[element] = Imageres.data.posters[0].file_path;
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
