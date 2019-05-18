<template>
  <div>
    <div class="container border rounded w-75">
      <form>
        <h3>Movie Info</h3>

        <div>{{ selected[page].movie.title }}</div>
        <img
          v-if=" selected[page].poster"
          v-bind:src="'https://image.tmdb.org/t/p/w154/' +  selected[page].poster"
        >
        <div>
          <star-rating
            v-model="rating[page]"
            :glow="5"
            :increment="0.5"
            :rounded-corners="true"
            :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"
            :show-rating="false"
          ></star-rating>
        </div>

        <b-btn variant="primary" @click="move(page--)">Previous</b-btn>
        {{page+1}}
        <b-btn variant="primary" @click="move(page++)">Next</b-btn>

        <b-btn variant="primary" @click="submit()">Submit</b-btn>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "scale",
  metaInfo: {
    title: "Item Page"
  },
  data() {
    return {
      rating: [],
      selected: [],
      page: 0,
      message: ''
    };
  },
  methods: {
    async rate() {},
    async loadinfo() {
      this.selected = this.$session.get("movies");
    },
    move() {
      if (this.page <= -1) {
        this.page = 9;
      } else if (this.page >= 10) {
        this.page = 0;
      }
    },
    submit() {
      var length = 0;
      this.rating.forEach(element => {
        element;
        length++;
      });

      if (length == 10) {
        for (let i = 0; i < this.selected.length; i++) {
          this.selected[i].scale = this.rating[i];
        }
        this.$session.set("movies", this.selected);
        this.$router.push("/3");
      }else{
        this.message = "Rating not completed. Please rate all the movies."
      }
    }
  },
  mounted() {
    if (this.$session.get("movies")) {
      this.loadinfo();
    } else {
      this.$router.push("/1");
    }
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
