<template>
  <form>
    <select title="Заголовок" id="font-size" name="text-size" @change="handleHeadingLevelChange">
      <option value="1" :selected="headingLevel === '1'">Заголовок 1</option>
      <option value="2" :selected="headingLevel === '2'">Заголовок 2</option>
      <option value="3" :selected="headingLevel === '3'">Заголовок 3</option>
      <option value="4" :selected="headingLevel === '4'">Заголовок 4</option>
      <option value="pr" :selected="headingLevel === 'pr'">Параграф</option>
    </select>
  </form>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  props: {
    editor: Object,
  },
  data() {
    return {
      headingLevel: '', //хранит выбранный заголовок(тег{h1,h2,h3,h4,p})
    };
  },
  mounted() {
    this.setHeadingLevel();
  },

  methods: {
    handleHeadingLevelChange(event) {
      const selectedValue = event.target.value;
      if (selectedValue === 'pr') {
        this.editor.chain().focus().setParagraph().run();
      }
      else {
        this.editor.chain().focus().toggleHeading({ level: parseInt(selectedValue) }).run();
      }
    },
    setHeadingLevel() {
      //нуже метод для определения тега, чтобы заголовки сами определялись и что бы пофиксить баги-_-
    },
  }
});
</script>
