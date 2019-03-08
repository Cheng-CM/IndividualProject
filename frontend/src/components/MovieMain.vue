<template>
  <div class="hello">
    <div class="container">
      <form class="my-5">
        <h3>Movie Info</h3>
        <div class="container-small" >
        <img src="https://i.pinimg.com/originals/cb/dd/77/cbdd779fc79c158eb30e13a8653c39b8.jpg" style="height: 450px;"/>
        </div>
        <ul>
          <li>{{ info.data.title }}</li>
          <li>{{ info.data.genres }}</li>
        </ul>

        <b-form-group label="Rating">
          <b-input type="number" :min="0" :max="5" v-model="ratingform.rating"/>
        </b-form-group>
        <b-btn variant="primary" @click="rate()">Rate</b-btn>
      </form>
    </div>
  </div>
</template>

<script>
import MovieAPI from "@/api/movie.js";
export default {
  name: "MovieMain",
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
      console.log(res.data[0]);
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
