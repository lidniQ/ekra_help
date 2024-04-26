<template>
  <div v-if="editor">
    <button title="Жирный (Ctr + B)" @click="editor.chain().focus().toggleBold().run()"
      :disabled="!editor.can().chain().focus().toggleBold().run()" :class="{ 'is-active': editor.isActive('bold') }">
      <i class="fa-solid fa-bold"></i>
    </button>
    <button title="Жирный (Ctr + I)" @click="editor.chain().focus().toggleItalic().run()"
      :disabled="!editor.can().chain().focus().toggleItalic().run()"
      :class="{ 'is-active': editor.isActive('italic') }">
      <i class="fa-solid fa-italic"></i>
    </button>
    <button title="Жирный (Ctr + B)" @click="editor.chain().focus().toggleUnderline().run()"
      :disabled="!editor.can().chain().focus().toggleStrike().run()"
      :class="{ 'is-active': editor.isActive('underline') }">
      <i class="fa-solid fa-underline"></i>
    </button>
    <button title="Жирный (Ctr + B)" @click="editor.chain().focus().toggleStrike().run()"
      :disabled="!editor.can().chain().focus().toggleStrike().run()"
      :class="{ 'is-active': editor.isActive('strike') }">
      <i class="fa-solid fa-strikethrough"></i>
    </button>
    <button title="Выделить" @click="editor.chain().focus().toggleHighlight().run()"
      :disabled="!editor.can().chain().focus().toggleStrike().run()"
      :class="{ 'is-active': editor.isActive('highlight') }">
      <i class="fa-solid fa-highlighter"></i>
    </button>
    <button>
      <i class="fa-solid"></i> x2
    </button>
    <button>
      <i class="fa-solid"></i> x2
    </button>
  </div>
</template>

<script>
export default {
  props: {
    editor: Object,
  },
  components: {
  }
}
</script>
