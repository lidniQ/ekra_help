import { Store } from 'vuex';

interface RootState {
  setflag: boolean;
  setpreview: boolean;
  selectedTitle: string;
  color: string;
  editorContent: string;

}

const store = new Store<RootState>({
  state: {
    flag: false,
    preview: false,
    selectedTitle: '',
    color: "#000000",
    editorContent: '<p>I’m running Tiptap with Vue.js. 🎉</p>',
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

    setColor(state, text) { 
      state.color = text
    },
    setEditorContent(state, content: string) {
      state.editorContent = content;
    },

  },
  actions: {
    updateColor({ commit }, newColor) {
      commit('setColor', newColor);
    },
    saveEditorContent({ commit }, content: string) {
      commit('setEditorContent', content);
    },
  },
  getters: {
    getColor: state => state.color,
  }
});

export default store;
