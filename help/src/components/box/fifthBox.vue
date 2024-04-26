<template>
  <div v-if="editor">
    <button @click="editor.chain().focus().undo().run()" :disabled="!editor.can().chain().focus().undo().run()">
      <i class="fa-solid fa-rotate-left"></i>
    </button>
    <button @click="editor.chain().focus().redo().run()" :disabled="!editor.can().chain().focus().redo().run()">
      <i class="fa-solid fa-rotate-right"></i>
    </button>
  </div>
</template>

<script>
export default {
  props: {
    editor: Object,
  },
}
</script>
