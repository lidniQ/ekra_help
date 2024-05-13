import { Image } from "@tiptap/extension-image";
import { mergeAttributes } from "@tiptap/vue-3";

export const MyImage = Image.extend({
  renderHTML({ HTMLAttributes }) {
    const { src, alt } = HTMLAttributes;
    return [
      "div",
      { class: "wrapper img" },
      [
        "div",
        { class: "space zone", style: "" },
        [
          "div",
          { class: "mx-auto", style: "width: 50%; " },
          [
            "div",
            {style:"width: max-content", contenteditable: "false" },
            ["img",
            mergeAttributes({ src, alt, class: "block;" })],
          ],
        ],
      ],
    ];
  },
});
