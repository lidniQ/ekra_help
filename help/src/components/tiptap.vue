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
import { MyImage } from "../ts/Image/Image.ts";
// import Doc from '../ts/Title/Doc.ts'
// import Title from '../ts/Title/Title.ts'

import float from './float.vue';
import menu_edit from './menu_edit.vue';

export default {
  components: {
    EditorContent,
    menu_edit,
  },

  data() {
    return {
      content: '',
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
        MyImage,
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
    <float :editor="editor"></float>

  </floating-menu>
  <editor-content :editor="editor" />
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

  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    line-height: 1.1;
  }

  code {
    background-color: rgba(#616161, 0.1);
    color: #616161;
  }

  pre {
    background: #0D0D0D;
    color: #FFF;
    font-family: 'JetBrainsMono', monospace;
    padding: 0.75rem 1rem;
    border-radius: 0.5rem;

    code {
      color: inherit;
      padding: 0;
      background: none;
      font-size: 0.8rem;
    }
  }

  img {
    max-width: 100%;
    height: auto;
  }

  blockquote {
    padding-left: 1rem;
    border-left: 2px solid rgba(#0D0D0D, 0.1);
    color: rgb(80, 80, 80);
  }

  hr {
    border: none;
    border-top: 2px solid rgba(#0D0D0D, 0.1);
    margin: 2rem 0;
  }
}
</style>
