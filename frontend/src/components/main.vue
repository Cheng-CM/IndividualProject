 <template>
  <div id="app">
    <div class="container">
      <div class="row">
        <ul>Experiment for movie recommendation system in item comparsion and scale rating</ul>
      </div>
      <div class="row">
        <ul>
          <b-button class="mb-4" variant="primary" to="rRating">Start</b-button>
        </ul>
      </div>
    </div>
  </div>
</template>


<script>
import MovieAPI from "@/api/movie.js";
export default {
  name: "Main",
  metaInfo: {
    title: "Movie Item Page"
  },
  components: {},
  methods: {
    async loadId() {
      var userId = 1000;
      const res = await MovieAPI.getgtUserid();
      if (!this.$session.has("userId")) {
        if (res.data[0] === undefined) {
          this.$session.set("userId", userId);
        } else {
          if (res.data[0].userId >= userId) {
            userId = res.data[0].userId + 1;
          }
          this.$session.set("userId", userId);
        }
        this.$session.set("ratecount", 0);
      }
    }
  },
  mounted() {
    this.loadId();
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>