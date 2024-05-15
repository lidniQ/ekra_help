<script>
import sidebar from './components/sidebar.vue'
import directory from './components/directory.vue'
import directoryNewArticle from './components/directoryNewArticle.vue'
import ekra_menu_bar from './components/ekra-menu-bar.vue'
import empty from './components/empty.vue'
import pencil_edit from './components/smallComponents/pencil.vue'

import { mapState } from 'vuex';

export default {
  components: {
    sidebar,
    directory,
    ekra_menu_bar,
    empty,
    pencil_edit,
    directoryNewArticle,
  },
  computed: {
    ...mapState(['flag', 'preview', 'selectedTitle']),
  }
}
</script>

<template>
  <ekra_menu_bar />
  <div class="container">
    <div class="sidebar">
      <sidebar />
    </div>
    <div class="directory">
      <pencil_edit v-if="!flag" />
      <directory />
      <empty v-if="!flag" />
    </div>
  </div>
</template>

<style>
.container {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  position: absolute;
  width: 1865px;
  height: 1010px;
  left: 20px;
  top: 50px;
  background: #F2F5F7;
  border-radius: 5px;

  .sidebar {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 10px;
    gap: 15px;

    width: 320px;
    height: 861px;

    background: #F2F5F7;

    flex: none;
    order: 0;
    align-self: stretch;
    flex-grow: 0;
    border-radius: 5px;
  }

  .directory {
    display: flex;
    flex: 1;
    flex-direction: column;
    height: 100%;
    width: 100%;
  }
}
</style>
