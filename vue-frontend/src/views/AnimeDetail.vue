<template>
  <section class="anime-details spad">
    <div class="container">
      <div class="anime__details__content">
        <div class="row">
          <div class="col-lg-3">
            <div
              class="anime__details__pic set-bg"
              style="
                background-image: url(https://ae04.alicdn.com/kf/H9ebb6f77a7864fef959de3ce7ef73c82g/-.jpg);
              "
            >
              <form method="post">
                <div class="favorite">
                  <button class="btn btn-outline-danger">
                    <i class="bi bi-heart"></i>
                  </button>
                </div>
              </form>
              <div class="comment"><i class="bi bi-chat"></i> {{ anime.total_comments }}</div>
              <div class="view"><i class="bi bi-eye"></i> {{ anime.views }}</div>
            </div>
            <Buttons
            @click="changeAnimeList"
            :animeTitle="anime.title"
            />
          </div>
          <div class="col-lg-9">
            <div class="anime__details__text">
              <div class="anime__details__title">
                <h3>{{ anime.title }}</h3>
                <span>{{ anime.second_title }}</span>
              </div>

              <Rating @star="getStar" :grade="3" :maxStars="5"/>

              <p class="mt-2">{{ anime.description }}</p>
              <div class="anime__details__widget">
                <div class="row">
                  <div class="col-lg-6 col-md-6">
                    <ul class="red-link">
                      <li><span>Тип:</span> {{ anime.type }}</li>
                      <li><span>Студия:</span> <a v-for="studio in anime.studios" href="#">{{ studio }} {{ '' }}</a></li>
                      <li><span>Дата выхода:</span> {{ anime.release_date }}</li>
                      <li><span>Статус:</span> {{ anime.status }}</li>
                      <li>
                        <span>Жанры:</span> <a v-for="genre in anime.genres" href="#">{{ genre }} {{ '' }}</a>
                      </li>
                      <li>
                        <span>Режиссеры:</span> <a v-for="director in anime.directors" href="#">{{ director }} {{ '' }}</a>
                      </li>
                    </ul>
                  </div>
                  <div class="col-lg-6 col-md-6">
                    <ul>
                      <li><span>Рейтинг:</span>{{ anime.avg_rating }}</li>
                      <li><span>Воз. рейтинг:</span> {{ anime.age_ratings }}</li>
                      <li><span>Качество:</span> HD</li>
                      <li><span>Просмотров:</span>{{ anime.views }}</li>
                    </ul>
                  </div>
                </div>
              </div>
              <div class="anime__details__btn"></div>
            </div>
          </div>
        </div>
      </div>
      <AnimeShots></AnimeShots>
      <div class="row">
        <div class="col-lg-8 col-md-8">
          <Comments 
		 	    :comments="anime.comments"
		      />
        </div>
        <div class="col-lg-4 col-md-4">
            <AnimeSimilar
              :anime="anime.similar_anime"
            />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import Buttons from "@/components/Buttons.vue";
import AnimeShots from "@/components/AnimeShots.vue";
import Comments from "@/components/Comments.vue";
import AnimeSimilar from "@/components/AnimeSimilar.vue";
import Rating from "@/components/Rating.vue";
import { mapGetters } from 'vuex'
import axios from "axios";
export default {
	name: "anime-detail",
	components: {
    	Buttons,
    	AnimeShots,
    	Comments,
      AnimeSimilar,
      Rating
  	},
	data() {
		return {
			anime: [],
		}
	},
  computed: mapGetters(['username']),
	methods: {
		async getAnime() {
			const response = await axios.get(`anime/${this.$route.params.slug}/`)
			this.anime = response.data
		},
    async changeAnimeList(name_of_list) {
      const formData = {
        field: name_of_list,
        anime: this.anime.id
      }
      await axios.patch('user/update/anime-list/', formData)
    },
    async getStar(star) {
      const formData = {
        anime: this.anime.id,
        star: star
      }
      await axios.post('anime/rating/', formData)
    }
	},
	mounted() {
		this.getAnime()
	}
};
</script>

<style scoped>
.favorite {
  margin-left: 10px;
  padding-top: 10px;
}

.favorite button {
  opacity: 1;
}

/*---------------------
  Anime Details
-----------------------*/

.anime-details {
  padding-top: 60px;
}

.anime__details__content {
  margin-bottom: 65px;
}

.anime__details__text {
  position: relative;
}

.anime__details__text p {
  color: #b7b7b7;
  font-size: 18px;
  line-height: 30px;
}

.anime__details__pic {
  height: 440px;
  border-radius: 5px;
  position: relative;
}

.anime__details__pic .comment {
  font-size: 13px;
  color: #ffffff;
  background: #3d3d3d;
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  position: absolute;
  left: 10px;
  bottom: 25px;
}

.anime__details__pic .view {
  font-size: 13px;
  color: #ffffff;
  background: #3d3d3d;
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  position: absolute;
  right: 10px;
  bottom: 25px;
}

.anime__details__title {
  margin-bottom: 20px;
}

.anime__details__title h3 {
  color: #ffffff;
  font-weight: 700;
  margin-bottom: 13px;
}

.anime__details__title span {
  font-size: 15px;
  color: #b7b7b7;
  display: block;
}

.anime__details__rating {
  text-align: center;
  position: absolute;
  right: 0;
  top: 0;
}

.anime__details__rating .rating i {
  font-size: 24px;
  color: #e89f12;
  display: inline-block;
}

.anime__details__rating span {
  display: block;
  font-size: 18px;
  color: #b7b7b7;
}

.anime__details__widget {
  margin-bottom: 15px;
}

.anime__details__widget ul {
  margin-bottom: 20px;
}

.anime__details__widget ul li {
  list-style: none;
  font-size: 15px;
  color: #ffffff;
  line-height: 30px;
  position: relative;
  padding-left: 18px;
}

.anime__details__widget ul li:before {
  position: absolute;
  left: 0;
  top: 12px;
  height: 6px;
  width: 6px;
  background: #b7b7b7;
  content: "";
}

.anime__details__widget ul li span {
  color: #b7b7b7;
  width: 115px;
  display: inline-block;
}

.anime__details__btn .follow-btn {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 14px 20px;
  border-radius: 4px;
  margin-right: 11px;
}

.anime__details__btn .watch-btn span {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 14px 20px;
  border-radius: 4px 0 0 4px;
  margin-right: 1px;
}

.anime__details__btn .watch-btn i {
  font-size: 20px;
  display: inline-block;
  background: #e53637;
  padding: 11px 5px 16px 8px;
  color: #ffffff;
  border-radius: 0 4px 4px 0;
}
</style>
