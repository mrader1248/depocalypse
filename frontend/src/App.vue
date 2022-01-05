<template>
  <v-app>
      <v-app-bar
        app
        color="primary"
        dark>

        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-toolbar-title>Depocalypse</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-app-bar-nav-icon @click.stop="drawer = !drawer" />

      </v-app-bar>

      <v-navigation-drawer v-model="drawer" right absolute temporary>
        <v-list>
          <v-list-item-group>
            <v-list-item
              v-for="item in drawerItems"
              :key="item.title"
              :to="item.route">
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>

    <v-main class="ma-4">
      <router-view/>
    </v-main>

  </v-app>
</template>

<script>

export default {
  name: 'App',
  data: function() {
    return {
      drawer: false,
      drawerItems: [
        {title: 'Home', icon: 'mdi-home', route: '/'},
        {title: 'Outlook', icon: 'mdi-chart-areaspline', route: '/outlook'}
      ]
    }
  },
};
</script>
