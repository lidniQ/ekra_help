<script>
import { Editor, EditorContent, BubbleMenu } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'
import { ColorHighlighter } from '../ts/ColorHighlighter';
import { SmilieReplacer } from '../ts/SmilieReplacer.ts';
import Highlight from '@tiptap/extension-highlight';
import TextAlign from '@tiptap/extension-text-align';
import Typography from '@tiptap/extension-typography';
import Underline from '@tiptap/extension-underline';
import Link from '@tiptap/extension-link';

import CustomImage from '../js/Image/custom-image.js';

import { Color } from '@tiptap/extension-color';
import Document from '@tiptap/extension-document';
import Paragraph from '@tiptap/extension-paragraph';
import Text from '@tiptap/extension-text';
import TextStyle from '@tiptap/extension-text-style';
import Table from '@tiptap/extension-table';
import TableCell from '@tiptap/extension-table-cell';
import TableHeader from '@tiptap/extension-table-header';
import TableRow from '@tiptap/extension-table-row';
// import Doc from '../ts/Title/Doc.ts'
// import Title from '../ts/Title/Title.ts'
import { ref, watch } from 'vue';
import menu_edit from './menu_edit.vue';

import { mapState } from 'vuex';

export default {
  data() {
    return {
      editor: null,
    }
  },
  computed: {
    ...mapState(['flag', 'preview']),
  },
  components: {
    EditorContent,
    menu_edit,
    BubbleMenu
  },
  props: {
    modelValue: {
      type: String,
      default: '',
    },
  },

  emits: ['update:modelValue'],
  watch: {
    flag(newFlagValue) {
      this.editor.options.editable = newFlagValue;
    },
    preview(newPreviewValue) {
      this.editor.options.editable = !newPreviewValue;
    },

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
        CustomImage.configure({
          HTMLAttributes: {
            class: 'custom-image'
          }
        }),
        TextAlign.configure({
          types: ['heading', 'paragraph', 'image'],
          alignments: ['left', 'center', 'right', 'justify'],
        }),
        Highlight,
        Typography,
        SmilieReplacer,
        ColorHighlighter,
        Underline,
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
      editable: false,
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
              height: ${this.flag ? '880px' : '860px'}; // изменение высоты в зависимости от flag
              overflow-y: auto;
              margin: ${this.flag ? '0 0 0 0' : '20px 0px 20px 0'};`
        },
      },
    },
    )
  },

  beforeDestroy() {
    this.editor.destroy()
  },
}
</script>

<template>
  <menu_edit v-if="flag" :editor="editor"></menu_edit>
  <bubble-menu class="bubble-menu" :tippy-options="{ animation: false }" :editor="editor" v-if="editor"
    v-show="editor.isActive('custom-image')">
    <div class="sizeIMG">
      <button @click="
    editor
      .chain()
      .focus()
      .setImage({ size: 'small' })
      .run()
    " :class="{
    'is-active': editor.isActive('custom-image', {
      size: 'small'
    })
  }">
        Маленький
      </button>
      <button @click="
    editor
      .chain()
      .focus()
      .setImage({ size: 'medium' })
      .run()
    " :class="{
    'is-active': editor.isActive('custom-image', {
      size: 'medium'
    })
  }">
        Средний
      </button>
      <button @click="
    editor
      .chain()
      .focus()
      .setImage({ size: 'large' })
      .run()
    " :class="{
    'is-active': editor.isActive('custom-image', {
      size: 'large'
    })
  }">
        Большой
      </button>
    </div>
    <span style="color: #aaa">|</span>
    <div class="alignsIMG">
      <button @click="
    editor
      .chain()
      .focus()
      .setImage({ float: 'left' })
      .run()
    " :class="{
    'is-active': editor.isActive('custom-image', {
      float: 'left'
    })
  }">
        Слева
      </button>
      <button @click="
    editor
      .chain()
      .focus()
      .setImage({ float: 'none' })
      .run()
    " :class="{
    'is-active': editor.isActive('custom-image', {
      float: 'none'
    })
  }">
        По центру
      </button>
      <button @click="
    editor
      .chain()
      .focus()
      .setImage({ float: 'right' })
      .run()
    " :class="{
    'is-active': editor.isActive('custom-image', {
      float: 'right'
    })
  }">
        Справа
      </button>
    </div>
  </bubble-menu>
  <editor-content :editor="editor" />
</template>

<style>
.tiptap {
  >*+* {
    margin-top: 0.75em;
  }
 blockquote {
    padding-left: 2rem;
    border-left: 2px solid rgba(#b6b6b6, 0.1);
  }
  ul,
  ol {
    padding: 0 2rem;
  }

  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    line-height: 1.1;
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

.frame {
  max-width: 900px;
  background: white;
  margin: 0 auto;
}

.controls {
  padding: 10px;
  border-bottom: 3px solid #eee;
  display: flex;
  width: 100%;
  align-items: center;

  button {
    background: none;
    font-weight: bold;
    width: 36px;
    height: 36px;
    display: flex;
    justify-content: center;
    margin-right: 4px;
    align-items: center;
    color: #0d0d0d;
    padding: 7px;
    border: 1px solid #ccc;

    &.is-active {
      background: #ddd;
    }
  }
}

.video-wrapper {
  position: relative;
  padding-bottom: 56.25%;
  padding-top: 10px;
  height: 0;
  overflow: hidden;
}

.video-wrapper iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.ProseMirror {

  &:focus {
    outline: 2px solid #26ada5;
  }

  >*+* {
    margin-top: 0.75em;
  }

  img {
    width: 100%;
    height: auto;
    display: block;
    margin-left: auto;
    margin-right: auto;

    &.ProseMirror-selectednode {
      outline: 3px solid #16c8ab;
    }
  }

  .custom-image-small {
    max-width: 200px;
  }

  .custom-image-medium {
    max-width: 500px;
  }

  .custom-image-large {
    max-width: 80%;
  }

  .custom-image-float-none {
    float: none;
  }

  .custom-image-float-left {
    float: left;
  }

  .custom-image-float-right {
    float: right;
  }
}

.bubble-menu {
  display: flex;
  padding-left: 2px;
  padding-right: 2px;
  background-color: #0d0d0d;
  border-radius: 0.5rem;

  .sizeIMG {
    display: flex
  }

  .alignsIMG {
    display: flex
  }

  button {
    border: none;
    background: none;
    color: #fff;
    font-size: 0.85rem;
    font-weight: 500;
    padding: 0 0.2rem;
    opacity: 0.6;

    &:hover,
    &.is-active {
      opacity: 1;
    }

    &.is-active {
      text-decoration: underline;
      color: #16c8ab;
    }
  }
}
</style>
