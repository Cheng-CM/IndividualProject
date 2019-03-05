import Vue from 'vue';
class MovieAPI {
    getMovie(params){
        return Vue.prototype.axios.get("http://localhost:8000/api/Movies/" + params);
    } 
    postRate(params){
        return Vue.prototype.axios.post("http://localhost:8000/api/custom_ratings/?", params);
    }
}
export default new MovieAPI();