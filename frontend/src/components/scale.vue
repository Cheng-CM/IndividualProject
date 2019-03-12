<template>
  <div class="hello">
    <div class="container">
      <form class="my-5">
        <h3>Movie Info</h3>
        <div class="container"></div>
        <ul>
          <li>{{ info.data.title }}</li>
          <li>{{ info.data.genres }}</li>
          <li>
            <b-form-group label="Rating:" class="col-sm">
              <star-rating
                v-model="rating"
                :glow="5"
                :rounded-corners="true"
                :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"
                :show-rating="false"
              ></star-rating>
            </b-form-group>
          </li>
        </ul>

        <ul>
          <li>
            <b-btn variant="primary" @click="rate()">Rate</b-btn>
          </li>
          <li>
            <b-btn variant="primary" @click="loadinfo()">Have not seen it</b-btn>
          </li>
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
      rating: 0,
      ratingform: {
        userId: 1
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
        rating: this.rating,
        timestamp: new Date().getTime()
      };
      console.log(params);

      await MovieAPI.postRate(params);
      this.loadinfo();
    },
    async loadinfo() {
      const res = await MovieAPI.getRandomMovie();
      this.info.data = res.data[0];
      this.resetStar();
    },
    resetStar(){
      this.rating = 0;
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
