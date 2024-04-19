<template>
  <div>
    <div class="editor-content">
      <tiptap />
    </div>
    <div class="choise-menu">
      <save_choise />
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import { useEditor, EditorContent } from '@tiptap/vue-3';

import save_choise from './save-choise.vue'
import tiptap from './tiptap.vue';


export default {
  data() {
    return {
      renderContent: '',
    };
  },
  components: {
    tiptap,
    save_choise,
  },
  computed: {
    ...mapState(['flag', 'preview', 'editorContent']),
    DirectoryViewStyles() {
      return {
        marginTop: this.selectedTitle ? '80px' : '20px',
        height: this.selectedTitle ? '700px' : '700px',
      };
    },
    newDirectoryStyle() {
      return {
        height: this.flag ? '700px' : '700px',
        height: this.preview ? '700px' : '700px',
      };
    },
  },
  methods: {
    ...mapMutations(['setflag', 'setpreview']),
    toggleViews() {
      this.setflag(true);
      this.setpreview(true);
    }
  },
};
</script>

<style>
.custom-editor-style {
  width: 1400px;
  /* Установите нужную ширину */
  height: 600px;
  /* Установите нужную высоту */
  overflow-y: auto;
  /* Обеспечьте появление полос прокрутки, если содержимое выходит за пределы */
  border: none;
  /* Удалите границу, если она не нужна */
}

.editor-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: absolute;
  height: 600px;
  width: 1470px;
  border-radius: 5px;
  background: #FFFFFF;
  z-index: 1
}

button {
  background-color: #ffffff;
  border: none;
}

img {
  max-width: 100%;
  height: auto;

  &.ProseMirror-selectednode {
    outline: 3px solid #68CEF8;
  }
}

.color {
  white-space: nowrap;

  &::before {
    content: ' ';
    display: inline-block;
    width: 1em;
    height: 1em;
    border: 1px solid rgba(128, 128, 128, 0.3);
    vertical-align: middle;
    margin-right: 0.1em;
    margin-bottom: 0.15em;
    border-radius: 2px;
    background-color: var(--color);
  }
}

.choise-menu {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: absolute;
  top: 880px;

  height: 60px;
  width: 1470px;

  background: #F2F5F7;
}
</style>
