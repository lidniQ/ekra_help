<script>
import { mapState, mapMutations } from 'vuex';

export default {
  computed: {
    ...mapState(['flag', 'preview', 'selectedTitle']),
  },
  methods: {
    ...mapMutations(['setFlag', 'setPreview']),
    openEdit() {
      this.setFlag(true);
    },
    newArticls() {
      this.setFlag(true)
    }
  },
}
</script>

<template>
  <div class="pencil-space-zone">
    <div v-if="!selectedTitle">
      <div class="spaceBG">
        <button @click="newArticls">
          <i class="fa-solid fa-plus"></i>
        </button>
      </div>
    </div>
    <div v-if="selectedTitle">
      <div class="spaceBG">
        <button @click="openEdit">
          <i class="fa-solid fa-pencil"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<style>
.pencil-space-zone {
  width: max-content;

}

.spaceBG {
  position: relative;
}

.spaceBG button {
  position: relative;
  overflow: hidden;
}

.spaceBG button:before {
  content: "";
  position: absolute;
  top: 45%;
  left: 50%;
  width: 80%;
  height: 80%;
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 50%;
  transition: all 0.3s ease;
  transform: translate(-50%, -50%) scale(0);
}

.spaceBG button:hover:before {
  transform: translate(-50%, -50%) scale(1);
}
</style>
