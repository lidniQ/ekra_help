import { Image } from "@tiptap/extension-image";
import { mergeAttributes } from "@tiptap/vue-3";

export const MyImage = Image.extend({
  defaultOptions: {
    ...Image.options,
    sizes: ["center", "justify", "left", "right"],
  },
  renderHTML({ HTMLAttributes }) {
    const { src, alt, style } = HTMLAttributes;
    return [
      "figure",
      { style },
      ["img", mergeAttributes({ src, alt })],
    ];
  },
});
