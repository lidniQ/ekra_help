<template>
  <div v-if="!preview" class="main-menu-edit">
    <div v-if="editor" class="section">
      <div class="row">
        <div class="col">
          <div class="first box">
            <firstBox :editor="editor" />
          </div>
          <div class="second box">
            <secontBox :editor="editor" />
          </div>
          <div class="third box">
            <thirdBox :editor="editor" />
          </div>
          <div class="fourth box">
            <fourthBox :editor="editor" />
          </div>
          <div class="table_edit box">
            <table_edit :editor="editor" />
          </div>
          <div class="fifth box">
            <fifthBox :editor="editor" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { mapState } from 'vuex';

import secontBox from './box/secondBox.vue';
import firstBox from './box/firstBox.vue';
import thirdBox from './box/thirdBox.vue';
import fourthBox from './box/fourthBox.vue';
import fifthBox from './box/fifthBox.vue';
import table_edit from './smallComponents/table.vue';


export default defineComponent({
  props: {
    editor: Object,
  },
  components: {
    firstBox,
    secontBox,
    thirdBox,
    fourthBox,
    fifthBox,
    table_edit,
  },
  computed: {
    ...mapState(['preview']),
  },
});

</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.row.justify-center {
  justify-content: center;
}

.main-menu-edit {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 1525px;
}

.section {
  margin-top: 20px;
  height: auto;
  width: auto;
}

.row {
  width: auto;
}

.col {
  width: auto;
  margin: 0 auto;
  /* Aligns the element to the center horizontally */
  text-align: center;
  /* Aligns the content inside the element to the center */
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

.table_edit {
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
