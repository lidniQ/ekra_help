import { Store } from 'vuex';

interface RootState {
  setflag: boolean;
  setpreview: boolean;
  selectedTitle: string;

}

const store = new Store<RootState>({
  state: {
    flag: false,
    preview: false,
    selectedTitle: '',
  },
  mutations: {
    setflag(state, boolean) { 
      state.flag = boolean;
    },
    setpreview(state, boolean) { 
      state.preview = boolean;
    },
    setSelectedTitle(state, text) { 
      state.selectedTitle = text;
    },

    setEditorContent(state, content: string) {
      state.editorContent = content;
    },

  },
  actions: {
    saveEditorContent({ commit }, content: string) {
      commit('setEditorContent', content);
    },
  },
  getters: {
  }
});

export default store;
