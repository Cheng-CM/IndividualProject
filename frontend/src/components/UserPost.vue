<template>
  <div class="hello">
    <h3>User rating form</h3>
    <form class="my-5">
      <b-form-group label="Movie ID">
        <b-input v-model="ratingform.movieId"/>
      </b-form-group>
      <b-form-group label="Rating">
        <b-input v-model="ratingform.rating"/>
      </b-form-group>
      <b-btn variant="primary" @click="rate()">Rate</b-btn>
    </form>
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
        userId: 999,
        movieId: "",
        rating: ""
      }
    };
  },
  methods: {
    async rate() {
      const params = {
        username: this.ratingform.userId,
        email: this.ratingform.movieId,
        password: this.ratingform.rating
      };
      const res = await MovieAPI.postRate(params);
      console.log(params);
    }
  },
  mounted() {
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
