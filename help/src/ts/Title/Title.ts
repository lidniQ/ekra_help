import { NodeSpec } from '@tiptap/pm/model';

export default class Title implements NodeSpec {
  get name() {
    return 'title';
  }

  get schema() {
    return {
      content: 'inline*',
      parseDOM: [{
        tag: 'h1',
      }],
      toDOM: () => ['h1', 0],
    };
  }
}
