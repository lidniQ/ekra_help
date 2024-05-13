import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import store from './store/store';
import ImgEdit from './components/smallComponents/image_edit.vue';


createApp(App)
  .use(store)
  .component('img-edit', ImgEdit) 
  .mount('#app')
