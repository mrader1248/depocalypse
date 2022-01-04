<template>
  <div class="over-time">
    <apex-chart
      type="area"
      width="800"
      :options="chartOptions"
      :series="chartSeries"
    />
  </div>
</template>

<script>
import axios from "axios";
import VueApexCharts from "vue-apexcharts";

export default {
  components: {
    "apex-chart": VueApexCharts,
  },
  data: function () {
    return {
      chartOptions: {
        chart: {
          zoom: {
            enabled: false,
          },
        },
        xaxis: {
          type: "datetime"
        },
        yaxis: {
          title: {
            text: "Inventory calorific value"
          }
        },
        dataLabels: {
          enabled: false,
        },
        tooltip: {
          x: { format: "yyyy-MM-dd" }
        }
      },
      chartSeries: [
        {
          name: "Inventory calorific value",
          data: [],
        },
      ],
    };
  },
  mounted() {
    axios
      .get("/depot/calorific-value-outlook/")
      .then((response) => {
        var data = response.data.dates.map((date, j) => [
          date,
          response.data.calorificValues[j],
        ]);
        this.chartSeries = [
          {
            data: data,
          },
        ];
      })
      .catch((error) => {
        this.showError("Content could not be loaded.");
        console.log(error);
      });
  },
};
</script>
