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
import { MyImage } from "../ts/Image/Image.ts";
import { Color } from '@tiptap/extension-color'
import Document from '@tiptap/extension-document'
import Paragraph from '@tiptap/extension-paragraph'
import Text from '@tiptap/extension-text'
import TextStyle from '@tiptap/extension-text-style'
// import Doc from '../ts/Title/Doc.ts'
// import Title from '../ts/Title/Title.ts'
import { ref, watch } from 'vue';
import float from './float.vue';
import menu_edit from './menu_edit.vue';


export default {
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

  setup(props) {
    const editor = useEditor({
      content: props.modelValue,
      onUpdate: () => {
        props.$emit('update:modelValue', editor.getHTML())
      },
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
      ],
      editorProps: {
        attributes: {
          class: 'custom-editor-style',
          style: `background-color: #fff;
              width: 1525px;
              height: 800px;
              overflow-y: auto;
              border-radius: 5px;
              border: none;`
        },
      },
    });

    const editorInstance = ref(editor);

    watch(() => props.modelValue, (value) => {
      const isSame = editorInstance.value.getHTML() === value;

      if (!isSame) {
        editorInstance.value.commands.setContent(value, false);
      }
    });
    return { editor: editorInstance };
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
}
</style>
