<script>
import { Editor, EditorContent, FloatingMenu } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import { ColorHighlighter } from '../ts/ColorHighlighter';
import { SmilieReplacer } from '../ts/SmilieReplacer.ts';
import Highlight from '@tiptap/extension-highlight';
import TextAlign from '@tiptap/extension-text-align';
import Image from '@tiptap/extension-image';
import Typography from '@tiptap/extension-typography';
import Underline from '@tiptap/extension-underline';
import { MyImage } from "../ts/Image/Image.ts";
import { Color } from '@tiptap/extension-color'
import Document from '@tiptap/extension-document'
import Paragraph from '@tiptap/extension-paragraph'
import Text from '@tiptap/extension-text'
import TextStyle from '@tiptap/extension-text-style'
import Table from '@tiptap/extension-table'
import TableCell from '@tiptap/extension-table-cell'
import TableHeader from '@tiptap/extension-table-header'
import TableRow from '@tiptap/extension-table-row'
// import Doc from '../ts/Title/Doc.ts'
// import Title from '../ts/Title/Title.ts'
import { ref, watch } from 'vue';
import float from './float.vue';
import menu_edit from './menu_edit.vue';


export default {
  data() {
    return {
      editor: null,
    }
  },
  components: {
    EditorContent,
    menu_edit,
    FloatingMenu,
    float,
  },
  props: {
    modelValue: {
      type: String,
      default: '',
    },
  },

  emits: ['update:modelValue'],

  watch: {
    modelValue(value) {
      // HTML
      const isSame = this.editor.getHTML() === value

      // JSON
      // const isSame = JSON.stringify(this.editor.getJSON()) === JSON.stringify(value)

      if (isSame) {
        return
      }

      this.editor.commands.setContent(value, false)
    },
  },

  mounted() {
    this.editor = new Editor({
      extensions: [
        StarterKit,
        TextAlign.configure({
          types: ['heading', 'paragraph', 'image'],
          alignments: ['left', 'center', 'right', 'justify'],
        }),
        Highlight,
        Image,
        Typography,
        SmilieReplacer,
        ColorHighlighter,
        Underline,
        MyImage,
        Document,
        Paragraph,
        Text,
        TextStyle,
        Color,
        Table.configure({
          resizable: true,
        }),
        TableRow,
        TableHeader,
        TableCell,
      ],
      content: this.modelValue,
      onUpdate: () => {
        // HTML
        this.$emit('update:modelValue', this.editor.getHTML())

        // JSON
        // this.$emit('update:modelValue', this.editor.getJSON())
      },
      editorProps: {
        attributes: {
          class: 'custom-editor-style',
          style: `background-color: #fff;
              width: 1525px;
              height: 880px;
              overflow-y: auto;
              border-radius: 5px;
              border: none;`
        },
      },
    })
  },

  beforeUnmount() {
    editor.destroy()
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

  table {
    border-collapse: collapse;
    table-layout: fixed;
    width: 100%;
    margin: 0;
    overflow: hidden;

    td,
    th {
      min-width: 1em;
      border: 2px solid #ced4da;
      padding: 3px 5px;
      vertical-align: top;
      box-sizing: border-box;
      position: relative;

      >* {
        margin-bottom: 0;
      }
    }

    th {
      font-weight: bold;
      text-align: left;
      background-color: #f1f3f5;
    }

    .selectedCell:after {
      z-index: 2;
      position: absolute;
      content: "";
      left: 0;
      right: 0;
      top: 0;
      bottom: 0;
      background: rgba(200, 200, 255, 0.4);
      pointer-events: none;
    }

    .column-resize-handle {
      position: absolute;
      right: -2px;
      top: 0;
      bottom: -2px;
      width: 4px;
      background-color: #adf;
      pointer-events: none;
    }

    p {
      margin: 0;
    }
  }
}

.tableWrapper {
  padding: 1rem 0;
  overflow-x: auto;
}

.resize-cursor {
  cursor: ew-resize;
  cursor: col-resize;
}
</style>
