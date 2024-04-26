<template>
  <div v-if="editor">
    <button @click="editor.chain().focus().setTextAlign('left').run()"
      :class="{ 'is-active': editor.isActive({ textAlign: 'left' }) }">
      <i class="fa-solid fa-align-left"></i>
    </button>
    <button @click="editor.chain().focus().setTextAlign('center').run()"
      :class="{ 'is-active': editor.isActive({ textAlign: 'center' }) }">
      <i class="fa-solid fa-align-center"></i>
    </button>
    <button @click="editor.chain().focus().setTextAlign('right').run()"
      :class="{ 'is-active': editor.isActive({ textAlign: 'right' }) }">
      <i class="fa-solid fa-align-right"></i>
    </button>
    <button @click="editor.chain().focus().setTextAlign('justify').run()"
      :class="{ 'is-active': editor.isActive({ textAlign: 'justify' }) }">
      <i class="fa-solid fa-align-justify"></i>
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
