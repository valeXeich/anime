<template>
  <section class="product spad">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <!--Trending-->
          <div class="trending__product">
            <div class="row">
              <div class="col-lg-8 col-md-8 col-sm-8">
                <div class="section-title">
                  <h4>Актуальные</h4>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-sm-4">
                <div class="btn__all">
                  <a href="{% url 'anime:anime_trending' %}" class="primary-btn"
                    >Смотреть все<span class="bi bi-arrow-right"></span
                  ></a>
                </div>
              </div>
            </div>
            <div class="row">
              <anime-item
              :anime="anime_actual"
              />
            </div>
          </div>
          <!-- Popular-->

          <div class="popular__product">
            <div class="row">
              <div class="col-lg-8 col-md-8 col-sm-8">
                <div class="section-title">
                  <h4>Популярные</h4>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-sm-4">
                <div class="btn__all">
                  <a href="{% url 'anime:anime_popular' %}" class="primary-btn"
                    >Смотреть все <span class="bi bi-arrow-right"></span
                  ></a>
                </div>
              </div>
            </div>
            <div class="row">
              <anime-item
              :anime="anime_popular"
              />
            </div>
          </div>
          <!--Recent-->
          <div class="recent__product">
            <div class="row">
              <div class="col-lg-8 col-md-8 col-sm-8">
                <div class="section-title">
                  <h4>Недавно добавленные</h4>
                </div>
              </div>
              <div class="col-lg-4 col-md-4 col-sm-4">
                <div class="btn__all">
                  <a href="{% url 'anime:anime_recent' %}" class="primary-btn"
                    >СМОТРЕТЬ ВСЕ <span class="bi bi-arrow-right"></span
                  ></a>
                </div>
              </div>
            </div>
            <div class="row">
              <anime-item
              :anime="anime_recent"
              />
            </div>
          </div>
        </div>
		<div class="col-lg-4 col-md-6 col-sm-8">
			<sidebar-top-view-vue
      :anime="anime_top_view"
      />
			<sidebar-comments-vue></sidebar-comments-vue>
		</div>
      </div>
    </div>
  </section>
</template>

<script>
import AnimeItem from "@/components/AnimeItem.vue";
import SidebarTopViewVue from "@/components/SidebarTopView.vue";
import SidebarCommentsVue from "@/components/SidebarComments.vue";
import axios from 'axios'
export default {
  components: {
    AnimeItem,
	SidebarTopViewVue,
	SidebarCommentsVue
  },
  data() {
    return {
      anime_actual: [],
      anime_popular: [],
      anime_recent: [],
      anime_top_view: [],
    }
  },
  methods: {
    async getActualAnime() {
      const response = await axios.get('anime/list/?ordering=-views_cnt,-comm_cnt,-release_date');
      this.anime_actual = response.data;
    },
    async getPopularAnime() {
      const response = await axios.get('anime/list/?ordering=-views_cnt,-comm_cnt');
      this.anime_popular = response.data;
    },
    async getRecentAnime() {
        const response = await axios.get('anime/list/?ordering=-created_date');
        this.anime_recent = response.data;
    },
    async getTopViewAnime() {
      const response = await axios.get('anime/list/?ordering=--views_cnt');
      this.anime_top_view = response.data
    }
  },
  mounted() {
    this.getActualAnime(),
    this.getPopularAnime(),
    this.getRecentAnime(),
    this.getTopViewAnime()
  }
};
</script>

<style scoped>
/*---------------------
  Product
-----------------------*/

.product {
  padding-bottom: 60px;
  padding-top: 80px;
}

.product-page {
  padding-top: 60px;
}

.btn__all {
  text-align: right;
  margin-bottom: 30px;
}

.trending__product {
  margin-bottom: 50px;
}

.popular__product {
  margin-bottom: 50px;
}

.recent__product {
  margin-bottom: 50px;
}

.product__page__title {
  border-bottom: 2px solid rgba(255, 255, 255, 0.2);
  padding-bottom: 10px;
  margin-bottom: 30px;
}

.product__page__title .section-title {
  margin-bottom: 0;
}

.product__page__title .product__page__filter {
  text-align: right;
}

.product__page__title .product__page__filter p {
  color: #ffffff;
  display: inline-block;
  margin-bottom: 0;
  margin-right: 16px;
}

.product__page__title .product__page__filter .nice-select {
  float: none;
  display: inline-block;
  font-size: 15px;
  color: #3d3d3d;
  font-weight: 700;
  border-radius: 0;
  padding-left: 15px;
  padding-right: 40px;
  height: 32px;
  line-height: 32px;
}

.product__page__title .product__page__filter .nice-select:after {
  border-bottom: 2px solid #111;
  border-right: 2px solid #111;
  height: 8px;
  top: 47%;
  width: 8px;
  right: 15px;
}

.product__page__title .product__page__filter .nice-select .list {
  margin-top: 0;
  border-radius: 0;
}

.product__pagination {
  padding-top: 15px;
}

.product__pagination a {
  display: inline-block;
  font-size: 15px;
  color: #b7b7b7;
  font-weight: 600;
  height: 50px;
  width: 50px;
  border: 1px solid transparent;
  border-radius: 50%;
  line-height: 48px;
  text-align: center;
  -webkit-transition: all, 0.3s;
  -o-transition: all, 0.3s;
  transition: all, 0.3s;
}

.product__pagination a:hover {
  color: #ffffff;
}

.product__pagination a.current-page {
  border: 1px solid #ffffff;
}

.product__pagination a i {
  color: #b7b7b7;
  font-size: 15px;
}
</style>
