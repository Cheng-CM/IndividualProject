<template>
  <div>
    <div>
      <h3>Movie Info</h3>
      <card class="container" style="width: 20rem;">
        <h4 slot="header">{{ selected[page].movie.title }}</h4>
        <div class="col-xs-12">
          <img
            v-if=" selected[page].poster"
            v-bind:src="'https://image.tmdb.org/t/p/w154/' +  selected[page].poster"
          >
        </div>
        <div class="stats col-xs-12">{{ selected[page].movie.genres }}</div>
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
      </card>
      <div class="container">
        <b-btn variant="primary" @click="move(page--)"><</b-btn>

        <b-btn variant="primary" @click="move(page++)">></b-btn>
        <div>{{page+1}}</div>
      </div>
      <b-btn variant="primary" @click="submit()">Submit</b-btn>
      <div>{{message}}</div>
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
      message: ""
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
    notifyVue(verticalAlign, horizontalAlign) {
      const notification = {
        template: `<span>` + this.message + `</span>`
      };
      const color = Math.floor(Math.random() * 4 + 1);
      this.$notify({
        component: notification,
        icon: "fa fa-gift",
        horizontalAlign: horizontalAlign,
        verticalAlign: verticalAlign,
        type: this.type[color]
      });
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
      } else {
        this.notifyVue("bottom", "center");
        this.message = "Rating not completed. Please rate all the movies.";
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
<style lang="scss">
.vue-notifyjs.notifications {
  .alert {
    z-index: 100;
  }
  .list-move {
    transition: transform 0.3s, opacity 0.4s;
  }
  .list-item {
    display: inline-block;
    margin-right: 10px;
  }
  .list-enter-active {
    transition: transform 0.2s ease-in, opacity 0.4s ease-in;
  }
  .list-leave-active {
    transition: transform 1s ease-out, opacity 0.4s ease-out;
  }

  .list-enter {
    opacity: 0;
    transform: scale(1.1);
  }
  .list-leave-to {
    opacity: 0;
    transform: scale(1.2, 0.7);
  }
}
</style>