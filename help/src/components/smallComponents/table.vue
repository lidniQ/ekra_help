<template>
  <button title="Вставить таблицу" type="button"
    @click="editor.chain().focus().insertTable({ rows: 3, cols: 3, withHeaderRow: true }).run()">
    <i class="fa-solid fa-table"></i>
  </button>
</template>

<script lang="ts">
export default {
  props: {
    editor: Object,
  },
  data() {
    return {

    };
  },
  methods: {
    addTable() {

    },
  }
}
</script>
