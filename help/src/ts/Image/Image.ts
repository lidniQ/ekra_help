import { Image } from "@tiptap/extension-image";
import { mergeAttributes } from "@tiptap/vue-3";

export const MyImage = Image.extend({
  defaultOptions: {
    ...Image.options,
    sizes: ["inline", "block", "left", "right"]
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
