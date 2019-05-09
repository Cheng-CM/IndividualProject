<template>
  <div>
    <!-- <div class="container" v-for="(item) in movies" :key="item.id">
      {{item.title}}
      <img
        v-if="img[item.movieId]"
        v-bind:src="'https://image.tmdb.org/t/p/w185/' + img[item.movieId]"
      >
    </div>-->
  </div>
</template>
<script>
import MovieAPI from "@/api/movie.js";
export default {
  name: "result",
  metaInfo: {
    title: "Result Page"
  },
  data() {
    return {
      cr_list: [],
      cr_image: [],
      sr_list: [],
      sr_image: []
    };
  },
  mounted() {
    if (this.$session.get("ratecount") < 10) {
      this.$router.push("/main");
    }
    this.loadinfo();
  },
  methods: {
    async loadinfo() {
      var res = await MovieAPI.getRecommendResult(this.$session.get("userId"));

      for (let i = 0; i < res.data.Compare.length; i++) {
        const element = res.data.Compare[i][0];
        var movie = await MovieAPI.getMovie(element);
        var link = await MovieAPI.getLink(element);
        var tmdbId = link.data.tmdbId;
        const Imageres = await MovieAPI.getMovieImage(tmdbId);
        if (Imageres.data.posters[0] != null) {
          this.cr_image[element] = Imageres.data.posters[0].file_path;
        }
        this.cr_list[element] = movie.data;
      }
      console.log(this.cr_list);
      console.log(this.cr_image);

      for (let i = 0; i < res.data.Scale.length; i++) {
         const element = res.data.Compare[i][0];
        var movie = await MovieAPI.getMovie(element);
        var link = await MovieAPI.getLink(element);
        var tmdbId = link.data.tmdbId;
        const Imageres = await MovieAPI.getMovieImage(tmdbId);
        if (Imageres.data.posters[0] != null) {
          this.sr_image[element] = Imageres.data.posters[0].file_path;
        }
        this.sr_list[element] = movie.data;
      }
    }
  }
};
</script>
