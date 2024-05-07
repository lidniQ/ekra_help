
import { Store } from 'vuex';

interface RootState {
  setflag: boolean;
  setpreview: boolean;
  selectedTitle: string;
  seteditorContent: string; 
}

const store = new Store<RootState>({
  state: {
    flag: true,
    preview: true,
    selectedTitle: '',
    editorContent: '', 
  },
  mutations: {
    setFlag(state, flag: boolean) { // Измененное название мутации
      state.flag = flag;
    },
    setPreview(state, preview: boolean) { // Измененное название мутации
      state.preview = preview;
    },
    setSelectedTitle(state, selectedTitle: string) {
      state.selectedTitle = selectedTitle;
    },
    setEditorContent(state, editorContent: string) { // Измененное название мутации
      state.editorContent = editorContent;
    },

  },
  actions: {
  },
  getters: {
  }
});

export default store;
