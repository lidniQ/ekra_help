<template>
  <form>
    <select title="Заголовок" id="font-size" name="text-size" v-model="headingLevel" @change="handleHeadingLevelChange">
      <option v-for="option in headingOptions" :key="option.value" :value="option.value">{{ option.label }}</option>
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
      headingLevel: '',
      headingOptions: [
        { value: '1', label: 'Заголовок 1' },
        { value: '2', label: 'Заголовок 2' },
        { value: '3', label: 'Заголовок 3' },
        { value: '4', label: 'Заголовок 4' },
        { value: 'pr', label: 'Параграф' },
      ],
    };
  },
  mounted() {
    this.setHeadingLevel();
  },
  methods: {
    handleHeadingLevelChange() {
      if (this.headingLevel === 'pr') {
        this.editor.chain().focus().setParagraph().insertContent('\n').run();
      } else {
        this.editor.chain().focus().toggleHeading({ level: parseInt(this.headingLevel) }).insertContent('\n').run();
      }
    },
    setHeadingLevel() {
      const { $from, to, node } = this.editor.state.selection;
      const headingNode = this.editor.state.schema.nodes.heading;
      if (node && node.type === headingNode) {
        this.headingLevel = String(node.attrs.level);
      }
    },
  },
});
</script>