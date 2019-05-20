<template>
  <div class="content">
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.2.0/css/all.css"
      crossorigin="anonymous"
    >
    <div class="container-fluid">
      <div class="row">
        <div class="col-xl-3 col-md-6">
          <stats-card>
            <div slot="header" class="icon-warning">
              <i class="nc-icon nc-chart-pie-35 text-warning"></i>
            </div>
            <div slot="content">
              <p class="card-category">RMSE</p>
              <h4 class="card-title">{{Math.round(testsetAccuracy[0] * 10000) / 10000}}</h4>
            </div>
            <div slot="footer">Latest Scale Testset Accuracy</div>
          </stats-card>
        </div>

        <div class="col-xl-3 col-md-6">
          <stats-card>
            <div slot="header" class="icon-success">
              <i class="nc-icon nc-chart-bar-32 text-success"></i>
            </div>
            <div slot="content">
              <p class="card-category">RMSE</p>
              <h4 class="card-title">{{Math.round(testsetAccuracy[1] * 10000) / 10000}}</h4>
            </div>
            <div slot="footer">Latest Item Comparison Testset Accuracy</div>
          </stats-card>
        </div>

        <div class="col-xl-3 col-md-6">
          <stats-card>
            <div slot="header" class="icon-danger">
              <i class="nc-icon nc-align-center text-danger"></i>
            </div>
            <div slot="content">
              <p class="card-category">Sum of 5-Star Scale</p>
              <h4
                class="card-title"
              >{{" Precision:" + Math.round(pnR[0][0] * 100) / 100 +", Recall:" + Math.round(pnR[0][1] * 100) / 100}}</h4>
            </div>
            <div slot="footer">
              <i class="fa fa-clock-o"></i>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-3 col-md-6">
          <stats-card>
            <div slot="header" class="icon-info">
              <i class="nc-icon nc-align-center text-primary"></i>
            </div>
            <div slot="content">
              <p class="card-category">Sum of Item Comparison</p>
              <h4
                class="card-title"
              >{{" Precision:" + Math.round(pnR[1][0] * 100) / 100 +", Recall:" + Math.round(pnR[1][1] * 100) / 100}}</h4>
            </div>
            <div slot="footer">
              <i class="fa fa-refresh"></i>
            </div>
          </stats-card>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <chart-card
            :chart-data="ResultChart.data"
            :chart-options="ResultChart.options"
            :responsive-options="ResultChart.responsiveOptions"
          >
            <template slot="header">
              <h4 class="card-title">RMSE Mean</h4>
              <p class="card-category">Accuracy of Data and Algorithms</p>
            </template>
            <template slot="footer">
              <div class="legend">
                <i class="fa fa-circle text-info"></i> 5-Star Method
                <i class="fa fa-circle text-danger"></i> Item-comparison
              </div>
              <hr>
              <div class="stats">Updated</div>
            </template>
          </chart-card>
        </div>
      </div>

      <div class="row">
        <div class="col-md-12">
          <chart-card
            :chart-data="Result2Chart.data"
            :chart-options="Result2Chart.options"
            :responsive-options="Result2Chart.responsiveOptions"
          >
            <template slot="header">
              <h4 class="card-title">MAE Mean</h4>
              <p class="card-category">Accuracy of Data and Algorithms</p>
            </template>
            <template slot="footer">
              <div class="legend">
                <i class="fa fa-circle text-info"></i> 5-Star Method
                <i class="fa fa-circle text-danger"></i> Item-comparison
              </div>
              <hr>
              <div class="stats">Updated</div>
            </template>
          </chart-card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ChartCard from "../components/Cards/ChartCard.vue";
import StatsCard from "../components/Cards/StatsCard.vue";
import LTable from "../components/Table.vue";
import MovieAPI from "@/api/movie.js";

export default {
  components: {
    LTable,
    ChartCard,
    StatsCard
  },
  data() {
    return {
      editTooltip: "Edit Task",
      deleteTooltip: "Remove",
      testsetAccuracy: [],
      pnR: [[], []],
      ResultChart: {
        data: {
          labels: [],
          series: [[], []]
        },
        options: {
          low: 0,
          high: 2,
          showArea: false,
          height: "245px",
          axisX: {
            showGrid: false
          },
          lineSmooth: false,
          showLine: true,
          showPoint: true,
          fullWidth: true,
          chartPadding: {
            right: 50
          }
        }
      },
      Result2Chart: {
        data: {
          labels: [],
          series: [[], []]
        },
        options: {
          low: 0,
          high: 2,
          showArea: false,
          height: "245px",
          axisX: {
            showGrid: false
          },
          lineSmooth: false,
          showLine: true,
          showPoint: true,
          fullWidth: true,
          chartPadding: {
            right: 50
          }
        }
      },
      responsiveOptions: [
        [
          "screen and (max-width: 640px)",
          {
            axisX: {
              labelInterpolationFnc(value) {
                return value[0];
              }
            }
          }
        ]
      ]
    };
  },
  methods: {
    async loadInfo() {
      var res = await MovieAPI.getAccuracy();
      //   console.log(res.data);
      var scaleRSMESeries = [];
      var compareRSMESeries = [];
      var scaleMAESeries = [];
      var comapareMAESeries = [];
      for (let i = 0; i < res.data.length; i++) {
        const method = res.data[i].Method;
        if (res.data[i].Method == "Scale") {
          scaleRSMESeries.push(Math.round(res.data[i].RMSEMean * 100) / 100);
          scaleMAESeries.push(Math.round(res.data[i].MAEMean * 100) / 100);
          this.ResultChart.data.labels.push(i / 2 + 1);
          this.Result2Chart.data.labels.push(i / 2 + 1);
          this.$set(this.testsetAccuracy, 0, res.data[i].RMSETestsetAccuracy);
          this.$set(this.pnR[0], 0, res.data[i].sumOfPrecisions);
          this.$set(this.pnR[0], 1, res.data[i].sumOfRecalls);
        } else {
          compareRSMESeries.push(Math.round(res.data[i].RMSEMean * 100) / 100);
          comapareMAESeries.push(Math.round(res.data[i].MAEMean * 100) / 100);
          this.$set(this.testsetAccuracy, 1, res.data[i].RMSETestsetAccuracy);
          this.$set(this.ResultChart.data.series, 0, scaleRSMESeries);
          this.$set(this.pnR[1], 0, res.data[i].sumOfPrecisions);
          this.$set(this.pnR[1], 1, res.data[i].sumOfRecalls);
        }
      }
      this.$set(this.ResultChart.data.series, 0, scaleRSMESeries);
      this.$set(this.ResultChart.data.series, 1, compareRSMESeries);
      this.$set(this.Result2Chart.data.series, 0, scaleMAESeries);
      this.$set(this.Result2Chart.data.series, 1, comapareMAESeries);
      console.log(res.data);
    }
  },
  mounted() {
    this.loadInfo();
  }
};
</script>
<style>
</style>
