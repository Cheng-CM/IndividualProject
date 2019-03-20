<template>
  <div class="hello">
    <div class="container">
      <form class="my-5">
        <h3>Movie Info</h3>
        <ul>
          <li>{{ info.data1.title }}</li>
          <li>{{ info.data1.genres }}</li>
          <li>
            <b-btn variant="primary" @click="rate(info.data1.movieId)">Rate</b-btn>
          </li>
        </ul>or
        <ul>
          <li>{{ info.data2.title }}</li>
          <li>{{ info.data2.genres }}</li>
          <li>
            <b-btn variant="primary" @click="rate(info.data2.movieId)">Rate</b-btn>
          </li>
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
      count: 0,
      info: {
        data1: {
          id: "",
          movieId: "",
          title: "",
          genres: ""
        },
        data2: {
          id: "",
          movieId: "",
          title: "",
          genres: ""
        }
      }
    };
  },
  methods: {
    async rate(id) {
      console.log(this.$session.getAll());
      if (this.info.data1.movieId == id) {
        this.$session.set(id, this.$session.get(id) + 0.5);
        this.$session.set(
          this.info.data2.movieId,
          this.$session.get(this.info.data2.movieId) - 0.5
        );
        this.$session.set(this.count, id + "," + this.info.data2.movieId);
      } else {
        this.$session.set(id, this.$session.get(id) + 0.5);
        this.$session.set(
          this.info.data1.movieId,
          this.$session.get(this.info.data1.movieId) - 0.5
        );
        this.$session.set(this.count, id + "," + this.info.data1.movieId);
      }
      this.count++;
      
    },
    async getMovies() {}
  },
  async mounted() {
    console.log(this.$session.getAll());

    const movieIds = this.$session.get("movieIds");
    const movieIdsList = movieIds.split(",");
    const res = await MovieAPI.getMovie(movieIdsList[0]);
    const res1 = await MovieAPI.getMovie(movieIdsList[1]);
    this.info.data1 = res.data;
    this.info.data2 = res1.data;
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
