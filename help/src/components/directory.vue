<template>
  <div class="view-edit">
  </div>
  <div class="editor-conteiners">
    <div class="editor-content">
      <tiptap v-model="content" />
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
      content: '<p>Артем, я не трогал Только data(content) поменял)</p>',
    };
  },
  components: {
    tiptap,
    save_choise,
  },
  computed: {
    ...mapState(['flag', 'preview']),
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
  watch: {
    content(newContent) {
      this.setEditorContent(newContent); // Вызываем мутацию при изменении content
    },
  },
  methods: {
    ...mapMutations(['setflag', 'setpreview', 'setEditorContent']),
    logContent() {
      console.log(this.content); // Вывод содержимого в консоль
    },
  },
  mounted() {
  },
};
</script>

<style>
.editor-content {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: absolute;
  height: 600px;
  width: 1525px;
  border-radius: 5px;
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
  top: 950px;
  height: 60px;
  width: 1525px;

  background: #F2F5F7;
}
</style>
