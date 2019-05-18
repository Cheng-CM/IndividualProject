<template>
  <div>
    <md-card class="container">
      <div class="container">
        <h3 class="row">Movies</h3>
        <button class="btn btn-secondary" @click="get10NewMovies">
          <font-awesome-icon icon="sync-alt"/>
        </button>
      </div>
      <draggable :list="movies" group="movies" v-bind="dragOptions" @change="pushMovie">
        <transition-group tag="div" class="grid" name="grid">
          <div class="md-layout-item" v-for="(element) in movies" :key="element.movie.movieId">
            <!-- <md-tooltip md-direction="top">on top</md-tooltip> -->
            <md-card class="md-card">

              <md-card-media-cover md-text-scrim>
                <md-card-media >
                  <img class="img" v-bind:src="'https://image.tmdb.org/t/p/w154/' + element.poster">
                </md-card-media>

                <md-card-area>
                  <md-card-header>
                    <span class="card-title">{{ element.movie.title }}</span>
                  </md-card-header>
                </md-card-area>
              </md-card-media-cover>

             
              <md-card-content>
                
              </md-card-content>
            </md-card>
          </div>
        </transition-group>
      </draggable>
    </md-card>

    <md-card class="container">
      <h3>Selected</h3>
      <draggable :list="selected" group="movies" v-bind="dragOptions">
        <transition-group tag="div" class="grid" name="grid">
          <div class="md-layout-item" v-for="(element) in selected" :key="element.movie.movieId">
            <md-card class="md-card">
              <img class="img" v-bind:src="'https://image.tmdb.org/t/p/w154/' + element.poster">
              <md-card-content>
                <div class="card-title">{{ element.movie.title }}</div>
              </md-card-content>
            </md-card>
          </div>
        </transition-group>
      </draggable>
      <div>
        <button class="btn btn-secondary" v-if="selected.length == 10" @click="submit">Submit</button>
      </div>
    </md-card>
  </div>
</template>
<script>
import MovieAPI from "@/api/movie.js";
import draggable from "vuedraggable";
import {
  StatsCard,
  ChartCard,
  NavTabsCard,
  NavTabsTable,
  OrderedTable
} from "@/components";
export default {
  components: {
    draggable,
    StatsCard,
    ChartCard,
    NavTabsCard,
    NavTabsTable,
    OrderedTable
  },
  name: "Selection",
  metaInfo: {
    title: "Movies Page"
  },
  data() {
    return {
      movies: [],
      selected: []
    };
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
  methods: {
    async get10NewMovies() {
      this.movies = [];
      for (let i = 0; i < 10; i++) {
        var poster = null,
          movie;
        while (poster == null) {
          movie = await this.randomMovie();
          poster = await this.getPoster(movie.movieId);
        }
        movie = {
          movie,
          poster
        };
        this.$set(this.movies, i, movie);
      }
    },
    async pushMovie() {
      if (this.movies.length < 10) {
        var poster = null,
          movie;
        while (poster == null) {
          movie = await this.randomMovie();
          poster = await this.getPoster(movie.movieId);
        }
        movie = {
          movie,
          poster
        };
        this.movies.push(movie);
      }
    },
    async randomMovie() {
      const res = await MovieAPI.getRandomMovie();
      var movie = res.data[0];
      return movie;
    },
    async getPoster(movieid) {
      const linkres = await MovieAPI.getLink(movieid);
      var tmdbId = linkres.data.tmdbId;
      const Imageres = await MovieAPI.getMovieImage(tmdbId);
      if (Imageres.data.posters[0] != null) {
        return Imageres.data.posters[0].file_path;
      } else {
        return null;
      }
    },
    submit() {
      if (this.selected.length >= 10) {
        this.$session.set("movies", this.selected);
        // console.log(this.$session.get("movies"));
        this.$router.push("/2");
      } else {
        alert("Not Enough Movies.");
      }
    }
  },
  mounted() {
    this.get10NewMovies();
  }
};
</script>
<style>
.flip-list-move {
  transition: transform 0.5s;
}
.no-move {
  transition: transform 0s;
}
.md-card {
    width: 320px;
    margin: 4px;
    display: inline-block;
    vertical-align: top;
  }
.ghost {
  opacity: 0.5;
  background: #c8ebfb;
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
.grid {
  display: grid;
  grid-template-columns: repeat(5, 215px);
  grid-template-rows: repeat(2, 430px);
  grid-gap: 0.2em;
}
.cell {
  display: flex;
}
</style>