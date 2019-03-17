import Vue from 'vue';
class MovieAPI {
    getMovie(params){
        return Vue.prototype.axios.get("http://localhost:8000/api/m/" + params);
    } 
    getRandomMovie(){
        return Vue.prototype.axios.get("http://localhost:8000/api/rm/");
    } 
    postRate(params){
        return Vue.prototype.axios.post("http://localhost:8000/api/cr/?", params);
    }
    getgtUserid(){
        return Vue.prototype.axios.get("http://localhost:8000/api/gcr/");
    } 
    
    
}
export default new MovieAPI();