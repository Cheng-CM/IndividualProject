<template>
  <div class="container">
    <h3>Movie Info</h3>
    <v-wait for="movieData">
      <template slot="waiting">
        <div>Loading the list...</div>
      </template>
      <div class="row">
        <div class="col">
          <div v-for="(item) in cr_list" :key="item.movie.data.movieId">
            <div>{{item.movie.data.title}}</div>
            <img v-if="item.poster" v-bind:src="'https://image.tmdb.org/t/p/w92/' + item.poster">
          </div>
          <b-btn variant="primary" @click="rate(0)">Rate</b-btn>
        </div>
        <div class="col">
          <div v-for="(item) in sr_list" :key="item.movieId">
            <div>{{item.movie.data.title}}</div>
            <img v-if="item.poster" v-bind:src="'https://image.tmdb.org/t/p/w92/' + item.poster">
          </div>
          <b-btn variant="primary" @click="rate(1)">Rate</b-btn>
        </div>
      </div>
    </v-wait>
  </div>
</template>
<script>
import MovieAPI from "@/api/movie.js";
import chunk from "chunk";
export default {
  name: "result",
  metaInfo: {
    title: "Result Page"
  },
  computed: {
    chunkedCompare() {
      return chunk(this.cr_list, 5);
    },
    chunkedScale() {
      return chunk(this.sr_list, 5);
    }
  },
  data() {
    return { cr_list: [], sr_list: [] };
  },
  mounted() {
    // if (this.$session.get("ratecount") < 10) {
    //   this.$router.push("/main");
    // }
    this.loadinfo();
  },
  methods: {
    async loadinfo() {
      console.log(this.$session.get("userId"));
      var userId = this.$session.get("userId");
      this.$wait.start("movieData");
      const res = await MovieAPI.getRecommendResult(userId);

      for (let i = 0; i < res.data.Compare.length; i++) {
        const compare = res.data.Compare[i][0];
        const scale = res.data.Scale[i][0];
        var movie = await this.populate(compare);
        this.$set(this.cr_list, i, movie);
        movie = await this.populate(scale);
        this.$set(this.sr_list, i, movie);
      }
      this.$wait.end("movieData");
    },
    async populate(element) {
      var link = await MovieAPI.getLink(element);
      var movie = await MovieAPI.getMovie(element);
      const Imageres = await MovieAPI.getMovieImage(link.data.tmdbId);
      var poster = null;
      if (Imageres.data.posters[0] != null) {
        poster = Imageres.data.posters[0].file_path;
      }
      var result = {
        movie: movie,
        poster: poster
      };
      console.log(result);
      return result;
    },
    async rate(vote) {
      var res = await MovieAPI.getRecommendResult(this.$session.get("userId"));
      if (vote == 0) {
        console.log("Compare");
        const params = {
          result: "Compare",
          content: res
        };
        var message = await MovieAPI.postResult(params);
      } else {
        console.log("Scale");
        const params = {
          result: "Scale",
          content: res
        };
        var message = await MovieAPI.postResult(params);
      }
      console.log(message);
      this.$router.push("/5");
    }
  }
};
</script>
