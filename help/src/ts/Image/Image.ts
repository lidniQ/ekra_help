import { Image } from "@tiptap/extension-image";
import { mergeAttributes } from "@tiptap/vue-3";

export const MyImage = Image.extend({
  defaultOptions: {
    ...Image.options,
    sizes: ["center", "justify", "left", "right"], //Расположение картинки по форме
  },
  renderHTML({ HTMLAttributes }) {
    const { style } = HTMLAttributes;
    return [
      "figure",
      { style },
      ["img", mergeAttributes(this.options.HTMLAttributes, HTMLAttributes)]
    ];
  }
});
