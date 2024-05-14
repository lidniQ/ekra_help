import { Image } from "@tiptap/extension-image";
import { mergeAttributes } from "@tiptap/vue-3";

export const MyImage = Image.extend({
  renderHTML({ HTMLAttributes }) {
    const { src, alt } = HTMLAttributes;
    return [
      "div",
      { class: "wrapper img", style:" display: flex; flex-direction: column; align-items: center;" },
      [
        "div",
        { class: "space zone", style: "margin-bottom: 20px;" },
        [
            "input",
            { type: "range", id: "sizeRange", min: "50", max: "500", value: "250" }
        ],
          [
            "button",
            { onclick: "set_align('left')" }, 
            "Влево"
          ],
          [
            "button",
            { onclick: "set_align('center')" },
            "По центру"
          ],
          [
            "button",
            { onclick: "set_align('right')" }, 
            "Вправо"
          ]
        ],
        [
            "div",
            { id:"imageContainer", class: "image-container", style:"width: 100%; display: flex; justify-content: center; align-items: center; overflow: hidden;" },
          
            ["img",
              mergeAttributes({ src, alt, class: "block;"},)
            ]
        ]  
    ];
  },

});
