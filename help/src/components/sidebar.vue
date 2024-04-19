<script>
import { mapState, mapMutations } from 'vuex';
import jsonData from '../data/json/articles.json';

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
    ...mapState(['selectedTitle'])
  },
  methods: {
    ...mapMutations(['setSelectedTitle']),
    loadArticles() {
      this.articles = jsonData.articles; // устанавливаем данные статей из импортированного JSON
    },
    toggleDropdown(index, items) {
      this.articles[index].expanded = !this.articles[index].expanded;
      this.setSelectedTitle(this.articles[index].title);
    },
  },
  components: {
  }
};
</script>

<template>
  <div class="label">
    <ul>
      <li v-for="(article, index) in articles" :key="index" class="li-title">
        <div @click="toggleDropdown(index)" class="sidebar-item">
          {{ article.title }}
          &nbsp;
          <span v-if="article.expanded">
            <i v-if="article.items" class="fa-solid fa-chevron-up"></i>
          </span>
          <span v-else>
            <i v-if="article.items" class="fa-solid fa-chevron-down"></i>
          </span>
        </div>
        <ul v-if="article.expanded">
          <li v-for="(items, index) in article.items" :key="index" class="li-sub-items">
            <a :href="'#' + items" class="sub-item-link">{{ items }}</a>
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
