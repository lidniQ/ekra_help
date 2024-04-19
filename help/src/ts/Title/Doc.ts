import { Node } from '@tiptap/pm/model';

export default class CustomDoc extends Node {
  get schema() {
    return {
      content: 'title block+',
    };
  }
}
