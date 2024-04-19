<script>
import { useEditor, EditorContent, FloatingMenu } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import { ColorHighlighter } from '../ts/ColorHighlighter';
import { SmilieReplacer } from '../ts/SmilieReplacer.ts';
import Highlight from '@tiptap/extension-highlight';
import TextAlign from '@tiptap/extension-text-align';
import Image from '@tiptap/extension-image';
import Typography from '@tiptap/extension-typography';
import Underline from '@tiptap/extension-underline';
import DraggableItem from '../ts/DraggableItem.ts'

import float from './float.vue';

import menu_edit from './menu_edit.vue';


export default {
  components: {
    EditorContent,
    menu_edit,
    FloatingMenu,
    float,
  },

  data() {
    return {
    }
  },
  setup() {
    const editor = useEditor({
      extensions: [
        StarterKit,
        TextAlign.configure({
          types: ['heading', 'paragraph'],
          alignments: ['left', 'center', 'right', 'justify'],
        }),
        Highlight,
        Image,
        Typography,
        SmilieReplacer,
        ColorHighlighter,
        Underline,
        DraggableItem,

      ],
      editorProps: {
        attributes: {
          class: 'custom-editor-style',
          style: `background-color: #fff;
              width: 1400px;
              height: 800px;
              overflow-y: auto;
              border: none;`
        },
      },
      content: `<p>Running tiptap with Vue.js</p>`,
    });
    return { editor };
  },
  beforeUnmount() {
    this.editor.destroy()
  },
  watch: {
    isEditable(value) {
      this.editor.setEditable(value)
    },
  },
}
</script>

<template>
  <menu_edit :editor="editor"></menu_edit>
  <floating-menu :editor="editor" :tippy-options="{ duration: 100 }" v-if="editor">
    <!-- <button @click="editor.chain().focus().toggleHeading({ level: 1 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 1 }) }">
      H1
    </button>
    <button @click="editor.chain().focus().toggleHeading({ level: 2 }).run()"
      :class="{ 'is-active': editor.isActive('heading', { level: 2 }) }">
      H2
    </button>
    <button @click="editor.chain().focus().toggleBulletList().run()"
      :class="{ 'is-active': editor.isActive('bulletList') }">
      Bullet List
    </button> -->
    <float :editor="editor"></float>

  </floating-menu>
  <editor-content :editor="editor" v-model="content" />
</template>

<style>
.tiptap {
  >*+* {
    margin-top: 0.75em;
  }

  ul,
  ol {
    padding: 0 1rem;
  }
}
</style>
