<template>
  <div v-if="editor" class="float_edit">
    <button @click="editor.chain().focus().toggleHeading({ level: 1 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }">
      <i class="fa-solid fa-heading"></i>1
    </button>
    <button @click="editor.chain().focus().toggleHeading({ level: 2 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }">
      <i class="fa-solid fa-heading"></i>2
    </button>
    <button @click="editor.chain().focus().toggleHeading({ level: 3 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 3 }) }">
      <i class="fa-solid fa-heading"></i>3
    </button>

    <button @click="editor.chain().focus().toggleBulletList().run()"
      :class="{ 'is-active': editor.isActive('bulletList') }">
      <i class="fa-solid fa-list-ul"></i>
    </button>

    <button @click="editor.chain().focus().toggleOrderedList().run()"
      :class="{ 'is-active': editor.isActive('orderedList') }">
      <i class="fa-solid fa-list-ol"></i> </button>

    <button @click="editor.chain().focus().toggleBlockquote().run()"
      :class="{ 'is-active': editor.isActive('blockquote') }">
      <i class="fa-solid fa-quote-right"></i> </button>

  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { mapState, mapActions } from 'vuex';


export default defineComponent({
  props: {
    editor: Object,
  },
  data() {
    return {
    };
  },
  methods: {
    addImage() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/*';
      input.onchange = (e) => {
        const file = e.target.files[0];
        if (file) {
          const reader = new FileReader();
          reader.readAsDataURL(file);
          reader.onload = (readerEvent) => {
            const url = readerEvent.target.result;
            this.editor.chain().focus().setImage({ src: url }).run();
          };
        }
      };
      input.click();
    },
  }
});
</script>

<style>
.float_edit {}
</style>
