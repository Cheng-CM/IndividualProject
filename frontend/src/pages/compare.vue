<template>
  <div>
    <h3>Movie Info</h3>
    <div>
      <draggable class="col" group="movies" v-bind="dragOptions">
        <transition-group tag="div">
          <div v-for="(element) in selected" :key="element.movie.movieId">
            <div>{{ element.movie.title }}</div>
            <img
              v-if="element.poster"
              v-bind:src="'https://image.tmdb.org/t/p/w92/' + element.poster"
            >
          </div>
        </transition-group>
      </draggable>
      <!-- <draggable class="col" :list="compare" group="movies" v-bind="dragOptions">
        <transition-group tag="div">
          <div v-for="index in 45" :key="index">
            <div>{{index}}</div>
          </div>
        </transition-group>
      </draggable>-->
      <button class="btn btn-secondary" @click="submit">Submit</button>
    </div>
  </div>
</template>

<script>
import MovieAPI from "@/api/movie.js";
import draggable from "vuedraggable";
export default {
  components: {
    draggable
  },
  name: "compare",
  metaInfo: {
    title: "Item Page"
  },
  computed: {
    dragOptions() {
      return {
        animation: 200,
        group: "description",
        disabled: false,
        ghostClass: "ghost"
      };
    }
  },
  data() {
    return {
      selected: [],
      compare: [],
      sliders: {
        slider2: [150, 400]
      }
    };
  },
  methods: {
    async submit() {
      var userId = this.$session.get("userId");
      var rating = [5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5];
      for (let i = 0; i < this.selected.length; i++) {
        this.selected[i].compare = rating[i];
      }
      this.$session.set("movies", this.selected);

      for (let i = 0; i < this.selected.length; i++) {
        const movie = this.selected[i];

        const compareParams = {
          userId: userId,
          movieId: movie.movie.movieId,
          rating: movie.compare,
          timestamp: new Date().getTime()
        };

        await MovieAPI.postcRate(compareParams);

        const scaleParams = {
          userId: userId,
          movieId: movie.movie.movieId,
          rating: movie.scale,
          timestamp: new Date().getTime()
        };
        await MovieAPI.postsRate(scaleParams);
      }

      this.$router.push("/4");
    },
    loadinfo() {
      this.selected = this.$session.get("movies");
    }
  },
  mounted() {
    if (!this.$session.has("userId")) {
      this.$router.push("/");
    }
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
.list-group {
  min-height: 20px;
}
.list-group-item {
  cursor: move;
}
.list-group-item i {
  cursor: pointer;
}
.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}
</style>
