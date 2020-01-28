import Vue from 'vue';
import config from "../config.json";
class MovieAPI {
    getMovie(params) {
        return Vue.prototype.axios.get("http://"+ config.development.database +":"+config.development.db_port+"/api/m/" + params);
    }
    getRandomMovie() {
        return Vue.prototype.axios.get("http://"+ config.development.database +":"+config.development.db_port+"/api/rm/");
    }
    postsRate(params) {
        return Vue.prototype.axios.post("http://"+ config.development.database +":"+config.development.db_port+"/api/sr/?", params);
    }
    postcRate(params) {
        return Vue.prototype.axios.post("http://"+ config.development.database +":"+config.development.db_port+"/api/cr/?", params);
    }
    getgtUserid() {
        return Vue.prototype.axios.get("http://"+ config.development.database +":"+config.development.db_port+"/api/gcr/");
    }
    getLink(params) {
        return Vue.prototype.axios.get("http://"+ config.development.database +":"+config.development.db_port+"/api/l/" + params);
    }
    getMovieImage(params) {
        return Vue.prototype.axios.get("https://api.themoviedb.org/3/movie/" + params + "/images?api_key=" + config.development.api_key + "&language=en");
    }
    getRecommendResult(params) {
        return Vue.prototype.axios.get("http://"+ config.development.database +":"+config.development.db_port+"/recommend/?id=" + params);
    }
    postResult(params) {
        return Vue.prototype.axios.post("http://"+ config.development.database +":"+config.development.db_port+"/result", params);
    }
    getAccuracy() {
        return Vue.prototype.axios.get("http://"+ config.development.database +":"+config.development.db_port+"/getAccuracy");
    }
    search(params) {
        return Vue.prototype.axios.get("http://"+ config.development.database +":"+config.development.db_port+"/search/?name=" + params);
    }


}
export default new MovieAPI();