<template>
  <div>
    <div class="container">
      <div class="col">
        <h3 class="row">Movies</h3>
        <!-- <div class="col"> -->

        <div class="row">
          <fg-input class="col-md-4" placeholder="Search..." v-model="search"></fg-input>
          <button class="btn btn-primary md-4" @click="searchMovie">
            <font-awesome-icon icon="search"/>
          </button>

          <button class="btn btn-secondary md-4" @click="get10NewMovies">
            <font-awesome-icon icon="sync-alt"/>
          </button>
        </div>

        <!-- </div> -->
      </div>
      <draggable :list="movies" group="movies" v-bind="dragOptions" @change="pushMovie">
        <transition-group tag="div" class="grid" name="grid">
          <div class="md-layout-item" v-for="(element) in movies" :key="element.movie.movieId">
            <card>
              <div slot="header">
                <img class="img" v-if="element.poster" v-bind:src="'https://image.tmdb.org/t/p/w154/' + element.poster">
              </div>
              <div class="col-xs-12">{{ element.movie.title }}</div>
            </card>
          </div>
        </transition-group>
      </draggable>
    </div>

    <div class="container">
      <h3>Selected</h3>
      <draggable :list="selected" group="movies" v-bind="dragOptions">
        <transition-group tag="div" class="grid" name="grid">
          <div class="md-layout-item" v-for="(element) in selected" :key="element.movie.movieId">
            <card>
              <div slot="header">
                <img class="img" v-if="element.poster" v-bind:src="'https://image.tmdb.org/t/p/w154/' + element.poster">
              </div>
              <div class="col-xs-12">{{ element.movie.title }}</div>
            </card>
          </div>
        </transition-group>
      </draggable>
      <div>
        <button class="btn btn-secondary" v-if="selected.length == 10" @click="submit">Submit</button>
      </div>
    </div>
  </div>
</template>
<script>
import fgInput from "@/components/Inputs/BaseInput.vue";
import MovieAPI from "@/api/movie.js";
import draggable from "vuedraggable";

export default {
  components: {
    draggable,
    fgInput
  },
  name: "Selection",
  metaInfo: {
    title: "Movies Page"
  },
  data() {
    return {
      movies: [],
      selected: [],
      search: ""
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
          console.log(movie);

          poster = await this.getPoster(movie.movieId);
        }
        movie = {
          movie,
          poster
        };
        this.$set(this.movies, i, movie);
      }
    },
    async searchMovie() {
      this.movies = [];
      var movies = await MovieAPI.search(this.search);
      for (let i = 0; i < movies.data.length; i++) {
        var movie,poster = null;
          movie = movies.data[i];
          console.log(movie);
          poster = await this.getPoster(movie.movieId);

        movie = {
          movie,
          poster
        };
        this.$set(this.movies, i, movie);
      }
    },
    async pushMovie() {
      while (this.movies.length < 10) {
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
.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}
.grid {
  display: grid;
  grid-template-columns: repeat(5, 215px);
  grid-template-rows: repeat(2, 350px);
  grid-gap: 0.2em;
}
.cell {
  display: flex;
}
</style>