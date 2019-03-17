<template>
  <div class="hello">
    <div class="container">
      <form class="my-5">
        <h3>Movie Info</h3>
        <ul>
          <li>{{ info.data.title }}</li>
          <li>{{ info.data.genres }}</li>
          <li><b-btn variant="primary" @click="rate()">Choose</b-btn></li>
        </ul>
        or
        <ul>
          <li>{{ info.data2.title }}</li>
          <li>{{ info.data2.genres }}</li>
          <li><b-btn variant="primary" @click="rate()">Choose</b-btn></li>
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
      ratingform: {
        userId: 999
      },
      info: {
        data: {
          id: "",
          movieId: "",
          title: "",
          genres: ""
        },data2: {
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
       const res2 = await MovieAPI.getRandomMovie();
      console.log(res.data[0]);
      this.info.data = res.data[0];
            this.info.data2 = res2.data[0];
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
