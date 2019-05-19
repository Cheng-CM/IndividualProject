<template>
  <div class="container">
    <h3>Movie Info</h3>
    <div class="row">
      <div class="col" v-on:click="listRank">
        <vue-slider
          v-model="rating"
          direction="btt"
          :height="1500"
          :process="false"
          :order="false"
          :dotSize="[20,20]"
          :max="50"
          :min="5"
          :marks="marks"
          style="display: inline-block; margin: 30px;"
        >
          <template #tooltip="{ index }">
            <div v-if="index === 0">{{selected[index].movie.title}}</div>
            <div v-else-if="index === 1">{{selected[index].movie.title}}</div>
            <div v-else-if="index === 2">{{selected[index].movie.title}}</div>
            <div v-else-if="index === 3">{{selected[index].movie.title}}</div>
            <div v-else-if="index === 4">{{selected[index].movie.title}}</div>
            <div v-else-if="index === 5">{{selected[index].movie.title}}</div>
            <div v-else-if="index === 6">{{selected[index].movie.title}}</div>
            <div v-else-if="index === 7">{{selected[index].movie.title}}</div>
            <div v-else-if="index === 8">{{selected[index].movie.title}}</div>
            <div v-else-if="index === 9">{{selected[index].movie.title}}</div>
          </template>
        </vue-slider>
      </div>
      <draggable class="col" group="movies" v-bind="dragOptions">
        <transition-group tag="div">
          <div v-for="(element,index) in listing" :key="element.movie.movieId">
            <div>{{ element.movie.title }}</div>
            <div>{{ index }}</div>
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
    </div>
    <button class="btn btn-secondary row" @click="submit">Submit</button>
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
      rating: [50, 45, 40, 35, 30, 25, 20, 15, 10, 5],
      listing: [],
      marks: {
        "50": {
          label: "Best 👍",
          labelStyle: {
            left: "100%",
            margin: "0 0 0 10px",
            top: "50%",
            transform: "translateY(-50%)"
          }
        },
        "5": {
          label: "Worst 👎",
          labelStyle: {
            left: "100%",
            margin: "0 0 0 10px",
            top: "50%",
            transform: "translateY(-50%)"
          }
        }
      }
    };
  },
  methods: {
    listRank() {
      // var sorted = this.rating;
      // let toIndex = sorted.length;
      // while (toIndex > 1) {
      //   toIndex--;
      //   for (let i = 0; i < toIndex; i++) {
      //     if (sorted[i] < sorted[i + 1]) {
      //       let tempValue = sorted[i];
      //       let tempMovie = this.listing[i];

      //       sorted[i] = sorted[i + 1];
      //       this.listing[i] = this.listing[i + 1];

      //       sorted[i + 1] = tempValue;
      //       this.listing[i + 1] = tempMovie;
      //     }
      //   }
      // }
      // for (let i = 0; i < sorted.length; i++) {
      //   const element = sorted;
      //   this.listing[i].rating = element;
      //   this.listing[i];
      // }
      // this.rating.sort();
      // console.log(sorted);
      // console.log(this.listing);
    },
    async submit() {
      var userId = this.$session.get("userId");
      console.log(this.selected);

      for (let i = 0; i < this.selected.length; i++) {
        this.selected[i].compare = this.rating[i] / 10;
      }
      this.$session.set("movies", this.selected);
      console.log(this.selected);
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
      this.listing = this.selected;
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
