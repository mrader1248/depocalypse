<template>
  <div class="outlook">
    <h4 class="text-h4">Outlook</h4>

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
            text: "Inventory calorific value [kcal]"
          }
        },
        dataLabels: {
          enabled: false,
        },
        tooltip: {
          x: { format: "yyyy-MM-dd" }
        },
        stroke: {
          curve: "straight"
        }
      },
      chartSeries: [
        {
          name: "Inventory calorific value [kcal]",
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
