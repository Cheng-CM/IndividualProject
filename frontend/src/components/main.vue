 <template>
  <div id="app">
    <div class="container">
      <div class="row">
        <ul>Experiment for movie recommendation system in item comparsion and scale rating</ul>
      </div>
      <div class="row">
        <ul>
          <router-link to="/rRating">
            <b-button class="mb-4" variant="primary" :to="'/rRating/'" @click="start()">Start</b-button>
          </router-link>
        </ul>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "Movie",
  metaInfo: {
    title: "Movie Item Page"
  },
  components: {},
  methods: {}
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