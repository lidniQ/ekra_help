<template>
  <div class="main-menu-edit">
    <div v-if="editor" class="section">
      <div class="row">
        <div class="col">
          <div class="first box">
            <form>
              <select id="font-size" name="text-size" @change="handleHeadingLevelChange">
                <option value="1">Заголовок 1</option>
                <option value="2">Заголовок 2</option>
                <option value="3">Заголовок 3</option>
                <option value="4">Заголовок 4</option>
                <option value="pr">Параграф</option>
              </select>
            </form>
          </div>
          <div class="second box">
            <button @click="editor.chain().focus().toggleBold().run()"
              :disabled="!editor.can().chain().focus().toggleBold().run()"
              :class="{ 'is-active': editor.isActive('bold') }">
              <i class="fa-solid fa-bold"></i>
            </button>
            <button v-tooltip="Курсив" @click="editor.chain().focus().toggleItalic().run()"
              :disabled="!editor.can().chain().focus().toggleItalic().run()"
              :class="{ 'is-active': editor.isActive('italic') }">
              <i class="fa-solid fa-italic"></i>
            </button>
            <button @click="editor.chain().focus().toggleUnderline().run()"
              :disabled="!editor.can().chain().focus().toggleStrike().run()"
              :class="{ 'is-active': editor.isActive('underline') }">
              <i class="fa-solid fa-underline"></i>
            </button>
            <button @click="editor.chain().focus().toggleStrike().run()"
              :disabled="!editor.can().chain().focus().toggleStrike().run()"
              :class="{ 'is-active': editor.isActive('strike') }">
              <i class="fa-solid fa-strikethrough"></i>
            </button>
            <button @click="editor.chain().focus().toggleHighlight({ color: '#ffc078' }).run()"
              :disabled="!editor.can().chain().focus().toggleStrike().run()"
              :class="{ 'is-active': editor.isActive('highlight', { color: '#ffc078' }) }">
              <i class="fa-solid fa-highlighter"></i>
            </button>
            <button>
              <i class="fa-solid"></i> x2
            </button>
            <button>
              <i class="fa-solid"></i> x2
            </button>
          </div>

          <div class="third box">
            <button @click="editor.chain().focus().setTextAlign('left').run()"
              :class="{ 'is-active': editor.isActive({ textAlign: 'left' }) }">
              <i class="fa-solid fa-align-left"></i>
            </button>
            <button @click="editor.chain().focus().setTextAlign('center').run()"
              :class="{ 'is-active': editor.isActive({ textAlign: 'center' }) }">
              <i class="fa-solid fa-align-center"></i>
            </button>
            <button @click="editor.chain().focus().setTextAlign('right').run()"
              :class="{ 'is-active': editor.isActive({ textAlign: 'right' }) }">
              <i class="fa-solid fa-align-right"></i>
            </button>
            <button @click="editor.chain().focus().setTextAlign('justify').run()"
              :class="{ 'is-active': editor.isActive({ textAlign: 'justify' }) }">
              <i class="fa-solid fa-align-justify"></i>
            </button>
          </div>
          <div class="fourth box">
            <button type="button" @click="addImage">
              <i class="fa-solid fa-image"></i>
            </button>
            <button type="button">
              <i class="fa-solid fa-table"></i>

            </button>
            <input type="color" v-model="newColor">
          </div>
          <div class="fifth box">
            <button @click="editor.chain().focus().undo().run()" :disabled="!editor.can().chain().focus().undo().run()">
              <i class="fa-solid fa-rotate-left"></i>
            </button>
            <button @click="editor.chain().focus().redo().run()" :disabled="!editor.can().chain().focus().redo().run()">
              <i class="fa-solid fa-rotate-right"></i>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { mapState, mapActions } from 'vuex';


export default defineComponent({
  props: {
    editor: Object,
  },
  data() {
    return {
      newColor: '',
    };
  },
  computed: {
    ...mapState(['color']),
  },
  created() {
    this.newColor = this.color;
  },
  watch: {
    newColor(event) {
      this.updateColor(event);
    }
  },
  methods: {
    ...mapActions(['updateColor']),
    handleHeadingLevelChange(event) {
      const selectedValue = event.target.value;
      if (selectedValue === 'pr') {
        this.editor.chain().focus().setParagraph().run();
      }
      else {
        this.editor.chain().focus().toggleHeading({ level: parseInt(selectedValue) }).run();
      }
    },
    addImage() {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/*';
      input.onchange = (e) => {
        const file = e.target.files[0];
        if (file) {
          const reader = new FileReader();
          reader.readAsDataURL(file);
          reader.onload = (readerEvent) => {
            const url = readerEvent.target.result;
            this.editor.chain().focus().setImage({ src: url }).run();
          };
        }
      };
      input.click();
    },
  }
});
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.main-menu-edit {
  display: flex;
  justify-content: center;
  align-items: center;
}

.section {
  height: 70px;
  width: 1400px;
}

.box {
  display: inline-block !important;
  padding: 0 5px;
}

.first {
  border-right: 2px solid #40576d33;

  select {
    background-color: #F2F5F7;
  }
}

.second {
  border-right: 2px solid #40576d33;

  button:hover {
    background-color: #16c8aa86;
  }

  button:focus {
    background-color: #0af1cb;
    color: #000000;
  }
}

.third {
  border-right: 2px solid #40576d33;

  button:hover {
    background-color: #16c8aa86;
  }

}

button.is-active {
  background-color: #0af1cb;
  color: #000000;
}

.fourth {
  border-right: 2px solid #40576d33;

  input[type=color] {
    outline: none;
    border: none;
    background-color: #F2F5F7;
  }

  button:hover {
    background-color: #16c8aa86;
  }

}

select {
  outline: none;
  border: none;
  width: 120px;
  color: #131c35;
  font-size: 16px;
  background-color: #fff;
  padding: 10px 0;
  margin-left: 2px;
}

option:nth-child(1) {
  font-size: 18px;
}

option:nth-child(2) {
  font-size: 17px;
}

option:nth-child(3) {
  font-size: 16px;
}

option:nth-child(4) {
  font-size: 14px;
}

option:nth-child(5) {
  font-size: 14px;
}

button {
  border: none;
  color: #131c35;
  font-size: 16px;
  font-weight: 300;
  background: transparent;
  padding: 10px 16px;
  border-radius: 3px;
  cursor: pointer;
  user-select: none;
}

button[disabled] {
  cursor: not-allowed;
  color: #8f8d8dc7;
}
</style>
