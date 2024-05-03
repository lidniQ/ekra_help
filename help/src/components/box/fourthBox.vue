<template>
  <div v-if="editor">
    <button title="Вставить изображение" type="button" @click="addImage">
      <i class="fa-solid fa-image"></i>
    </button>
    <table_insert :editor="editor" />
    <input title="Изменить цвет текста" type="color" @input="editor.chain().focus().setColor($event.target.value).run()"
      :value="editor.getAttributes('textStyle').color">
  </div>
</template>

<script>
import table_insert from '../smallComponents/table.vue';

export default {
  props: {
    editor: Object,
  },
  components: {
    table_insert,
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
  },
}




</script>
