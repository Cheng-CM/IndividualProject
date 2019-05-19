 <template>
  <div id="app">
    <div class="container">
      <div class="row">
        <ul>Experiment for movie recommendation system in item comparsion and scale rating</ul>
      </div>
      <b-btn variant="primary" @click="next">Start</b-btn>
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
    next(){
      this.$router.push("1");
    },
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
      }
    }
  },
  mounted() {
    this.loadId();
  }
};
</script>

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