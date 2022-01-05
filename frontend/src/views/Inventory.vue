<template>
  <div class="home">
    <h4 class="text-h4">Inventory</h4>

    <v-data-table
      :headers="inventoryItemHeaders"
      :items="inventoryItems"
      :items-per-page="5" />

    <v-alert
      type='error' 
      dismissible
      v-model='isErrorMessageVisible'>
      {{ errorMessage }}
    </v-alert>

  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'Home',
    data: function() { 
      return {
        errorMessage: '',
        isErrorMessageVisible: false,
        inventoryItems: [],
        inventoryItemHeaders: [
          {text: 'Name', value: 'commodityName'},
          {text: 'Amount', value: 'amount'},
          {text: 'Total calorific value [kcal]', value: 'totalCalorificValueInKcal'},
        ],
      }
    },
    mounted() {
      axios.get('/depot/inventory/')
        .then((response) => {
          this.inventoryItems = response.data;
        })
        .catch((error) => {
          this.showError('The inventory could not be loaded.');
          console.log('calling /depot/inventory failed');
          console.log(error);
        });
    },
    methods: {
      showError: function(message) {
        this.errorMessage = message;
        this.isErrorMessageVisible = true;
      }
    }
  }

</script>
