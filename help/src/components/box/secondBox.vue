<template>
  <div v-if="editor">
    <button title="Жирный (Ctrl + B)" @click="editor.chain().focus().toggleBold().run()"
      :disabled="!editor.can().chain().focus().toggleBold().run()" :class="{ 'is-active': editor.isActive('bold') }">
      <i class="fa-solid fa-bold"></i>
    </button>
    <button title="Курсив (Ctrl + I)" @click="editor.chain().focus().toggleItalic().run()"
      :disabled="!editor.can().chain().focus().toggleItalic().run()"
      :class="{ 'is-active': editor.isActive('italic') }">
      <i class="fa-solid fa-italic"></i>
    </button>
    <button title="Подчеркнуть (Ctrl + U)" @click="editor.chain().focus().toggleUnderline().run()"
      :disabled="!editor.can().chain().focus().toggleStrike().run()"
      :class="{ 'is-active': editor.isActive('underline') }">
      <i class="fa-solid fa-underline"></i>
    </button>
    <button title="Зачеркнуть (Ctrl + Shift + S)" @click="editor.chain().focus().toggleStrike().run()"
      :disabled="!editor.can().chain().focus().toggleStrike().run()"
      :class="{ 'is-active': editor.isActive('strike') }">
      <i class="fa-solid fa-strikethrough"></i>
    </button>
    <button title="Выделить (Ctrl + Shift + H)" @click="editor.chain().focus().toggleHighlight().run()"
      :disabled="!editor.can().chain().focus().toggleStrike().run()"
      :class="{ 'is-active': editor.isActive('highlight') }">
      <i class="fa-solid fa-highlighter"></i>
    </button>
    <button title="Цитата" @click="editor.chain().focus().toggleBlockquote().run()"
      :disabled="!editor.can().chain().focus().toggleStrike().run()"
      :class="{ 'is-active': editor.isActive('blockquote') }">
      <i class="fa-solid fa-quote-left"></i>
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
