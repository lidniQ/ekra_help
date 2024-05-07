<script>
import jsonData from '../data/json/articles.json';
import { mapState, mapMutations } from 'vuex';

export default {
  data() {
    return {
      articles: [],
    };
  },
  created() {
    this.loadArticles();
  },
  computed: {
    ...mapState(['editorContent', 'selectedTitle']),
  },
  methods: {
    ...mapMutations(['setEditorContent', 'setSelectedTitle']),
    loadArticles() {
      this.articles = jsonData.articles.map(article => ({
        ...article,
        expanded: false // Initialize 'expanded' property for each article
      }));
    },
    toggleDropdown(index) {
      this.articles.forEach((article, i) => {
        if (i !== index) {
          article.expanded = false; // Свернуть все статьи, кроме выбранной
        }
      });

      const selectedArticle = this.articles[index];
      selectedArticle.expanded = !selectedArticle.expanded;
      if (selectedArticle.expanded) {
        this.setEditorContent(selectedArticle.html);
        this.setSelectedTitle(selectedArticle.title);
      } else {
        this.setEditorContent('');
      }
      this.$emit('articleClicked', selectedArticle);
    },
  },
};
</script>
<template>
  <div class="label">
    <ul>
      <li v-for="(article, index) in articles" :key="index" class="li-title">
        <div @click="toggleDropdown(index)" class="sidebar-item">
          {{ article.title }}
          &nbsp;
          <span v-if="article.expanded && article.items && article.items.length > 0">
            <i class="fa-solid fa-chevron-up"></i>
          </span>
          <span v-else-if="article.items && article.items.length === 0">
          </span>
          <span v-else>
            <i v-if="article.items" class="fa-solid fa-chevron-down"></i>
          </span>
        </div>
        <ul v-if="article.expanded">
          <li v-for="(item, index) in article.items" :key="index" class="li-sub-items">
            <a :href="'#' + item" class="sub-item-link">{{ item }}</a>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>


<style>
.label {
  margin-top: 20px;

  ul {
    list-style-type: none;

    .li-title {
      padding: 0 0 10px 0;
    }
  }
}

.sidebar-item {
  font-family: 'Montserrat';
  font-style: normal;
  font-size: 14px;
  line-height: 17px;
  display: flex;
  align-items: center;
  color: black;
  cursor: pointer;

  ul {
    width: 174px;
    font-family: 'Montserrat';
    font-style: normal;
    font-weight: 500;
    font-size: 12px;
    line-height: 15px;
    display: flex;
    align-items: center;
    list-style-type: none;
  }
}

.sidebar-item:hover {
  color: #16c8aa86;
}

.sub-item-link {
  text-decoration: none;
  color: #707070;
  padding-left: 40px;

}

.sub-item-link:hover {
  color: #16c8aa86;
}

.sub-item-link:focus {
  color: #16c8aa86;
}
</style>
