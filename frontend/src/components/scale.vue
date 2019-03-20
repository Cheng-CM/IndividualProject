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
          <li>{{ movies }} / 10</li>
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
      movies: 0,
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
      console.log(this.$session.getAll());
      
      if (this.$session.get("ratecount") >= 10) {
        this.$router.push("/cRating");
      } else {
        const params = {
          userId: this.$session.get("userId"),
          movieId: this.info.data.movieId,
          rating: this.rating,
          timestamp: new Date().getTime()
        };
        await MovieAPI.postRate(params);

        this.loadinfo();

        if (this.$session.has("movieIds")) {
          var mIds = this.$session.get("movieIds");
          this.$session.set("movieIds", mIds + "," + this.info.data.movieId);
        } else {
          this.$session.set("movieIds", this.info.data.movieId);
        }

        var rc = this.$session.get("ratecount");
        this.$session.set("ratecount", ++rc);

        if (this.$session.get("ratecount") >= 10) {
          this.$router.push("/cRating");
        }
      }
    },
    async loadinfo() {
      const res = await MovieAPI.getRandomMovie();
      this.info.data = res.data[0];
      this.resetStar();
      this.movies = this.$session.get("ratecount");
    },
    resetStar() {
      this.rating = 0;
    }
  },
  mounted() {
    if (this.$session.get("ratecount") >= 10) {
      this.$router.push("/cRating");
    }
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
