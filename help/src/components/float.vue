<template>
  <div v-if="editor" class="float_edit">
    <button @click="editor.chain().focus().toggleHeading({ level: 1 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }">
      H1
    </button>
    <button @click="editor.chain().focus().toggleHeading({ level: 2 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }">
      H2
    </button>
    <button @click="editor.chain().focus().toggleHeading({ level: 3 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 3 }) }">
      H3
    </button>

    <button @click="editor.chain().focus().toggleBulletList().run()"
      :class="{ 'is-active': editor.isActive('bulletList') }">
      <icon name="ul" />
    </button>

    <button @click="editor.chain().focus().toggleOrderedList().run()"
      :class="{ 'is-active': editor.isActive('orderedList') }">
      <icon name="ol" />
    </button>

    <button @click="editor.chain().focus().toggleBlockquote().run()"
      :class="{ 'is-active': editor.isActive('blockquote') }">
      <icon name="quote" />
    </button>

    <button @click="editor.chain().focus().toggleCodeBlock().run()"
      :class="{ 'is-active': editor.isActive('codeBlock') }">
      <icon name="code" />
    </button>

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
.float_edit {
  position: absolute;
  z-index: 1;
  margin-top: -0.25rem;
  opacity: 1;
  transition: opacity 0.5s ease-out;

  &.is-active {
    opacity: 1;
  }

  &:hover {
    opacity: 1;
  }
}

.float_edit:not(.is-active) {
  visibility: hidden;
  transition: opacity 0.5s ease-out, visibility 0.5s ease-out;
}
</style>
