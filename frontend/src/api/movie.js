import Vue from 'vue';
import api_key from 'frontend-config.yml';
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
        return Vue.prototype.axios.get("https://api.themoviedb.org/3/movie/" + params + "/images?api_key=",api_key,"&language=en");
    }
    getRecommendResult(params) {
        return Vue.prototype.axios.get("http://localhost:8000/recommend/?id=" + params);
    }
    postResult(params) {
        return Vue.prototype.axios.post("http://localhost:8000/result", params);
    }
    getAccuracy() {
        return Vue.prototype.axios.get("http://localhost:8000/getAccuracy");
    }
    search(params) {
        return Vue.prototype.axios.get("http://localhost:8000/search/?name=" + params);
    }


}
export default new MovieAPI();