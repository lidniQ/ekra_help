<template>
  <div v-if="editor">
    <button title="Вставить изображение" type="button" @click="addImage">
      <i class="fa-solid fa-image"></i>
    </button>
    <button title="Вставить видео" @click="addVideo">
      <i class="fa-solid fa-video"></i>

    </button>
    <input title="Изменить цвет текста" type="color" @input="editor.chain().focus().setColor($event.target.value).run()"
      :value="editor.getAttributes('textStyle').color">
  </div>

</template>

<script>
import axios from 'axios';

export default {
  props: {
    editor: Object,
  },
  components: {
  },
  methods: {
    addImage() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/*';
      input.onchange = (e) => {
        const file = e.target.files[0];
        if (file) {
          const formData = new FormData();
          formData.append('image', file);
          axios.post('http://10.27.1.6:8000/upload_image/', formData)
            .then(response => {
              const imageUrl = response.data.file_url;
              console.log('Image URL:', imageUrl);
              if (imageUrl && imageUrl.trim() !== '') {
                this.editor.chain().focus().setImage({ src: imageUrl }).run();
              } else {
                console.error('Error: Empty or invalid image URL received from server');
                alert('Ошибка: Получен пустой или неверный URL изображения от сервера');
              }
            })
            .catch(error => {
              console.error('Error uploading image:', error);
              alert('Ошибка загрузки изображения: ' + error.response.data.message);
            });
        }
      };
      input.click();
    },
    addVideo() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'video/*';
      input.onchange = (e) => {
        const file = e.target.files[0];
        if (file) {
          const formData = new FormData();
          formData.append('video', file);
          axios.post('http://10.27.1.6:8000/upload_video/', formData)
            .then(response => {
              const videoUrl = response.data.file_url;
              console.log('Video URL:', videoUrl);
              if (videoUrl && videoUrl.trim() !== '') {
                this.editor.chain().focus().setIframe({ src: videoUrl }).run();
              } else {
                console.error('Error: Empty or invalid video URL received from server');
                alert('Ошибка: Получен пустой или неверный URL изображения от сервера');
              }
            })
            .catch(error => {
              console.error('Error uploading video:', error);
              alert('Ошибка загрузки видео: ' + error.response.data.message);
            });
        }
      };
      input.click();
    },


  },
};
</script>

<style></style>
