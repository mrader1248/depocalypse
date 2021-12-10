<template>
  <div class="home">
    <h2 class="text-h2">Hello world!</h2>
    <p>
      Lorem ipsum, dolor sit amet consectetur adipisicing elit. Iusto suscipit neque temporibus, recusandae corporis ab
      consequatur, maiores amet iste, dolorem nulla excepturi esse autem praesentium? Doloremque aliquam quo eum minus?
    </p>
    <p>
      Note that this has absolutely nothing to do with the intended functionality! This is just a quick-and-dirty 
      demonstration of Vue, Vuetify and axios.
    </p>

    <v-text-field label="symbol" v-model="pairToQuery">XBTEUR</v-text-field>

    <v-btn @click="clickMeClicked">
      <v-icon left>candlestick_chart</v-icon>
      <span>click me</span>
    </v-btn>
    <br />
    <br />

    <v-alert type="success" v-bind:value="outputMessage.length > 0">{{ outputMessage }}</v-alert>
    <v-alert type="error" v-bind:value="errorMessage.length > 0">{{ errorMessage }}</v-alert>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'Home',
    data: function() { 
      return {
        pairToQuery: "XBTEUR",
        outputMessage: "",
        errorMessage: ""
      }
    },
    methods: {
      clickMeClicked: function() {
        this.outputMessage = "";
        this.errorMessage = "";
        axios.get('https://api.kraken.com/0/public/Ticker?pair=' + this.pairToQuery)
          .then((response) => {
            if (response.status != 200) {
              this.errorMessage = 'Request returned with HTTP error code ' + response.status + '.';
            } else if (response.data.error.length > 0) {
              this.errorMessage = response.data.error.join('\n');
            } else {
              this.outputMessage = 'At the moment 1 BTC is worth ' + response.data.result.XXBTZEUR.b[0] + ' EUR.';
            }
          })
          .catch((error) => {
            this.errorMessage = 'Request error: ' + error + '.';
          });
      }
    }
  }
</script>
