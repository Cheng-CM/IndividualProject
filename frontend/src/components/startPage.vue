<template>
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
      ratingform: {
        userId: "Test"
      },
      info: {
        data: {
          id: "",
          title: "",
          genres: ""
        }
      }
    };
  },
  methods: {
    async rate() {
      const params = {
        userId: this.ratingform.userId,
        movieId: this.info.data.movieId,
        rating: this.ratingform.rating,
        timestamp: new Date().getTime()
      };
      await MovieAPI.postRate(params);
    },
    async loadinfo() {
      const res = await MovieAPI.getRandomMovie();
      this.info.data = res.data[0];
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
