import Vue from 'vue';
class MovieAPI {
    getMovie(params) {
        return Vue.prototype.axios.get("http://localhost:8000/api/m/" + params);
    }
    getRandomMovie() {
        return Vue.prototype.axios.get("http://localhost:8000/api/rm/");
    }
    postsRate(params) {
        return Vue.prototype.axios.post("http://localhost:8000/api/sr/?", params);
    }
    postcRate(params) {
        return Vue.prototype.axios.post("http://localhost:8000/api/cr/?", params);
    }
    getgtUserid() {
        return Vue.prototype.axios.get("http://localhost:8000/api/gcr/");
    }
    getLink(params) {
        return Vue.prototype.axios.get("http://localhost:8000/api/l/" + params);
    }
    getMovieImage(params) {
        return Vue.prototype.axios.get("https://api.themoviedb.org/3/movie/" + params + "/images?api_key=34132d035e63f344a5eb1a1ac50e64e2&language=en");
    }
    getRecommendResult(params) {
        return Vue.prototype.axios.get("http://localhost:8000/recommend/?id=" + params);
    }


}
export default new MovieAPI();