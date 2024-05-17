<template>
  <div v-if="editor">
    <button title="Вставить таблицу" type="button"
      @click="editor.chain().focus().insertTable({ rows: 3, cols: 3, withHeaderRow: true }).run()">
      <svg width="15px" height="15px" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g id="Edit / Table_Add">
          <path id="Vector"
            d="M11 4H15.8002C16.9203 4 17.4801 4 17.9079 4.21799C18.2842 4.40973 18.5905 4.71547 18.7822 5.0918C19 5.5192 19 6.07899 19 7.19691V9.0002L11.0001 9.0001M11 4H6.2002C5.08009 4 4.51962 4 4.0918 4.21799C3.71547 4.40973 3.40973 4.71547 3.21799 5.0918C3 5.51962 3 6.08009 3 7.2002V9M11 4L11.0001 9.0001M3 9V15M3 9L11.0001 9.0001M3 15V16.8002C3 17.9203 3 18.4801 3.21799 18.9079C3.40973 19.2842 3.71547 19.5905 4.0918 19.7822C4.5192 20 5.07899 20 6.19691 20H11.0002L11.0001 9.0001M3 15H11M15 16H18M18 16H21M18 16V19M18 16V13"
            stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </g>
      </svg> </button>
    <button title="Добавить столбец слева" @click="editor.chain().focus().addColumnBefore().run()">
      <svg fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M120 180v1560c0 33 26.88 60 60 60h1020V120H180c-33.12 0-60 27-60 60Zm1620-60h-420v480h480V180c0-33-26.88-60-60-60Zm60 600h-480v480h480V720Zm-60 1080c33.12 0 60-27 60-60v-420h-480v480h420ZM180 1920c-99.24 0-180-80.76-180-180V180C0 80.76 80.76 0 180 0h1560c99.24 0 180 80.76 180 180v1560c0 99.24-80.76 180-180 180H180Zm596.484-510h-240v-330h-330V840h330V510h240v330h330v240h-330v330Z"
          fill-rule="evenodd" />
      </svg>
    </button>
    <button title="Добавить столбец справа" @click="editor.chain().focus().addColumnAfter().run()">
      <svg fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M1740 0c99.24 0 180 80.76 180 180v1560c0 99.24-80.76 180-180 180H180c-99.24 0-180-80.76-180-180V180C0 80.76 80.76 0 180 0h1560Zm60 1740V180c0-33-26.88-60-60-60H720v1680h1020c33.12 0 60-27 60-60Zm-1620 60h420v-480H120v420c0 33 26.88 60 60 60Zm-60-600h480V720H120v480Zm60-1080c-33.12 0-60 27-60 60v420h480V120H180Zm963.516 390h240v330h330v240h-330v330h-240v-330h-330V840h330V510Z"
          fill-rule="evenodd" />
      </svg>
    </button>
    <button title="Удалить столбец" @click="editor.chain().focus().deleteColumn().run()">
      <svg fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M1800 1740c0 33-27 60-60 60h-420v-300h-120v300H720v-300H600v300H180c-33.12 0-60-27-60-60V180c0-33 26.88-60 60-60h420v300h120V120h480v300h120V120h420c33 0 60 27 60 60v1560ZM1740 0H180C80.76 0 0 80.76 0 180v1560c0 99.24 80.76 180 180 180h1560c99.24 0 180-80.76 180-180V180c0-99.24-80.76-180-180-180Zm-305.16 654.84-169.68-169.68L960 790.32 654.84 485.16 485.16 654.84 790.32 960l-305.16 305.16 169.68 169.68L960 1129.68l305.16 305.16 169.68-169.68L1129.68 960l305.16-305.16Z"
          fill-rule="evenodd" />
      </svg>
    </button>
    <button title="Добавить строку сверху" @click="editor.chain().focus().addRowBefore().run()">
      <svg fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M1740 120H180c-33 0-60 26.88-60 60v1020h1680V180c0-33.12-27-60-60-60Zm60 1620v-420h-480v480h420c33 0 60-26.88 60-60Zm-600 60v-480H720v480h480Zm-1080-60c0 33.12 27 60 60 60h420v-480H120v420ZM0 180C0 80.76 80.76 0 180 0h1560c99.24 0 180 80.76 180 180v1560c0 99.24-80.76 180-180 180H180c-99.24 0-180-80.76-180-180V180Zm510 596.484v-240h330v-330h240v330h330v240h-330v330H840v-330H510Z"
          fill-rule="evenodd" />
      </svg>
    </button>
    <button title="Добавить строку снизу" @click="editor.chain().focus().addRowAfter().run()">
      <svg fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M180 1800h1560c33 0 60-26.88 60-60V720H120v1020c0 33.12 27 60 60 60ZM120 180v420h480V120H180c-33 0-60 26.88-60 60Zm600-60v480h480V120H720Zm1080 60c0-33.12-27-60-60-60h-420v480h480V180Zm120 1560c0 99.24-80.76 180-180 180H180c-99.24 0-180-80.76-180-180V180C0 80.76 80.76 0 180 0h1560c99.24 0 180 80.76 180 180v1560Zm-510-596.484v240h-330v330H840v-330H510v-240h330v-330h240v330h330Z"
          fill-rule="evenodd" />
      </svg>
    </button>
    <button title="Удалить строку" @click="editor.chain().focus().deleteRow().run()">
      <svg fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M180 1800c-33 0-60-27-60-60v-420h300v-120H120V720h300V600H120V180c0-33.12 27-60 60-60h1560c33 0 60 26.88 60 60v420h-300v120h300v480h-300v120h300v420c0 33-27 60-60 60H180Zm1740-60V180c0-99.24-80.76-180-180-180H180C80.76 0 0 80.76 0 180v1560c0 99.24 80.76 180 180 180h1560c99.24 0 180-80.76 180-180ZM485.32 1265 655 1434.68l305.16-305.16 305.16 305.16L1435 1265l-305.16-305.16L1435 654.68 1265.32 485 960.16 790.16 655 485 485.32 654.68l305.16 305.16L485.32 1265Z"
          fill-rule="evenodd" />
      </svg>
    </button>
    <button title="Удалить таблицу" @click="editor.chain().focus().deleteTable().run()">
      <svg width="15px" height="15px" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
        <g id="Edit / Table_Remove">
          <path id="Vector"
            d="M11 4H15.8002C16.9203 4 17.4801 4 17.9079 4.21799C18.2842 4.40973 18.5905 4.71547 18.7822 5.0918C19 5.5192 19 6.07899 19 7.19691V9.0002L11.0001 9.0001M11 4H6.2002C5.08009 4 4.51962 4 4.0918 4.21799C3.71547 4.40973 3.40973 4.71547 3.21799 5.0918C3 5.51962 3 6.08009 3 7.2002V9M11 4L11.0001 9.0001M3 9V15M3 9L11.0001 9.0001M3 15V16.8002C3 17.9203 3 18.4801 3.21799 18.9079C3.40973 19.2842 3.71547 19.5905 4.0918 19.7822C4.5192 20 5.07899 20 6.19691 20H11.0002L11.0001 9.0001M3 15H11M15 16H21"
            stroke="#000000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </g>
      </svg>
    </button>
    <button title="Объединить ячейки" @click="editor.chain().focus().mergeCells().run()">
      <svg fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M1740 0c99.24 0 180 80.76 180 180v1560c0 99.24-80.76 180-180 180H180c-99.24 0-180-80.76-180-180V180C0 80.76 80.76 0 180 0h1560Zm60 600V180c0-33-27-60-60-60h-420v480h480Zm0 1065V720H720v1080h945c74.25 0 135-60.75 135-135ZM720 600h480V120H720v480Zm-120 0V120H180c-33 0-60 27-60 60v420h480Zm-480 600h480V720H120v480Zm480 600v-480H120v420c0 33 27 60 60 60h420Z"
          fill-rule="evenodd" />
      </svg>
    </button>
    <button title="Разделить ячейку" @click="editor.chain().focus().splitCell().run()">
      <svg fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M1740 0c99.24 0 180 80.76 180 180v1560c0 99.24-80.76 180-180 180H180c-99.24 0-180-80.76-180-180V180C0 80.76 80.76 0 180 0Zm60 720H720v1080h945c74.25 0 135-60.75 135-135V720ZM600 1320H120v420c0 33 27 60 60 60h420v-480Zm0-600H120v480h480V720Zm1140-600h-420v480h480V180c0-33-27-60-60-60Zm-540 0H720v480h480V120Zm-600 0H180c-33 0-60 27-60 60v420h480V120Zm1134 841.559L1564.441 792 1259.5 1096.941 954.559 792 785 961.559l304.941 304.941L785 1571.441 954.559 1741l304.941-304.941L1564.441 1741 1734 1571.441 1429.059 1266.5 1734 961.559Z"
          fill-rule="evenodd" />
      </svg>
    </button>
    <button title="Выделить главный столбец" @click="editor.chain().focus().toggleHeaderColumn().run()">
      <svg fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M1740 0c99.24 0 180 80.76 180 180v1560c0 99.24-80.76 180-180 180H180c-99.24 0-180-80.76-180-180V180C0 80.76 80.76 0 180 0h1560Zm60 1320h-480v480h420c33 0 60-27 60-60v-420Zm-600 0H720v480h480v-480Zm600-600h-480v480h480V720Zm-600 0H720v480h480V720Zm540-600h-420v480h480V180c0-33-27-60-60-60Zm-540 0H720v480h480V120Z"
          fill-rule="evenodd" />
      </svg>
    </button>
    <button title="Выделить главную строку" @click="editor.chain().focus().toggleHeaderRow().run()">
      <svg fill="#000000" width="15px" height="15px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg">
        <path
          d="M1740 0c99.24 0 180 80.76 180 180v1560c0 99.24-80.76 180-180 180H180c-99.24 0-180-80.76-180-180V180C0 80.76 80.76 0 180 0h1560Zm-420 1200h480V720h-480v480Zm480 540v-420h-480v480h420c33 0 60-27 60-60ZM720 1200h480V720H720v480Zm0 600h480v-480H720v480Zm-600-600h480V720H120v480Zm480 600v-480H120v420c0 33 27 60 60 60h420Z"
          fill-rule="evenodd" />
      </svg>
    </button>
    <button title="Выделить ячейку" @click="editor.chain().focus().toggleHeaderCell().run()">
      toggleHeaderCell
    </button>
    <button title="Объединить|Разделить ячейки" @click="editor.chain().focus().mergeOrSplit().run()">
      mergeOrSplit
    </button>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    editor: Object,
  },
  data() {
    return {

    };
  },
  methods: {
    addTable() {

    },
  }
}
</script>
