import { Node } from '@tiptap/vue-3';
import { Image } from '@tiptap/extension-image';
import { mergeAttributes } from '@tiptap/core';

export const MyImage = Image.extend({
  defaultOptions() {
    return {
      ...Image.defaultOptions(),
      sizes: ['inline', 'block', 'left', 'right'],
    };
  },
  renderHTML({ HTMLAttributes }) {
    const { style } = HTMLAttributes;
    return [
      'figure',
      { style },
      ['img', mergeAttributes(this.options.HTMLAttributes, HTMLAttributes)],
    ];
  },
}) as unknown as Node;
