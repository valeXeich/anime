<template>
  <div class="container bootstrap snippets bootdey">
    <div class="row">
      <div class="profile-nav col-md-3">
        <div class="panel">
          <div class="user-heading round">
            <a href="#">
              <img
                src="https://i.pinimg.com/originals/b9/a4/ca/b9a4caf4948ac1d4dd6bfdd63bd178d9.jpg"
                alt=""
              />
            </a>
            <h1 class="text-white">valex</h1>
          </div>
        </div>
      </div>

      <div class="profile-info col-md-9">
        <div class="panel">
          <div id="status-menu" class="status-menu-container mt-2">
            <div class="anime text-center">
              <template v-for="(value, name) in field_names">
                <button v-if="field === name" @click.prevent="changeAnimeList(name)" class="btn btn btn-danger btn-lg">{{ value }}</button>
                <button v-else @click.prevent="changeAnimeList(name)" class="btn btn-outline-danger btn-lg">{{ value }}</button>
              </template>
            </div>
          </div>

          <table class="table table table-hover mt-2 table-cus">
            <thead>
              <tr>
                <th scope="col" class="text-white">Постер</th>
                <th scope="col" class="text-white">Название</th>
                <th scope="col" class="text-white">Рейтинг</th>
              </tr>
            </thead>
            <tbody class="text-white">
              <tr v-for="anime in animeList">
                <td>
                  <a href="#"
                    ><img
                      src="https://ae04.alicdn.com/kf/H9ebb6f77a7864fef959de3ce7ef73c82g/-.jpg"
                      class="image"
                  /></a>
                </td>
                <td class="red-link-profile text-white">
                  <a href="#">{{ anime }}</a>
                </td>
                <td class="text-white">3.0</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userInfo: [],
      animeList: [],
      field: 'watching_now',
      field_names: {
        'watching_now': 'СМОТРЮ',
        'will_watch': 'БУДУ СМОТРЕТЬ',
        'viewed': 'ПРОСМОТРЕНО',
        'throw': 'БРОШЕНО',
        'favorite': 'ЛЮБИМЫЕ'
      }
    }
  },
  methods: {
    async getUserInfo() {
      const response = await axios.get(`user/get/${this.$route.params.slug}/`)
      this.userInfo = response.data
      this.animeList = response.data.watching_now
      console.log(response.data)
    },
    changeAnimeList(field) {
        console.log(field)
        this.animeList = this.userInfo[field]
    }
  },
  mounted() {
    this.getUserInfo()
  },
};
</script>

<style scoped>
.red-link-profile a:hover {
  color: red;
}

.table-cus {
  background-color: #070720;
  margin-bottom: 320px;
}

.status-menu-container {
  height: 49px;
  background-color: #070720;
  border-bottom: 1px solid red;
  z-index: 1;
}

.image {
  width: 120px;
}

.profile-nav,
.profile-info {
  margin-top: 30px;
}

.profile-nav .user-heading {
  background: #070720;
  color: #fff;
  border-radius: 4px 4px 0 0;
  -webkit-border-radius: 4px 4px 0 0;
  padding: 30px;
  text-align: center;
}

.profile-nav .user-heading.round a {
  border-radius: 50%;
  -webkit-border-radius: 50%;
  border: 10px solid rgba(255, 255, 255, 0.3);
  display: inline-block;
}

.profile-nav .user-heading a img {
  width: 112px;
  height: 112px;
  border-radius: 50%;
  -webkit-border-radius: 50%;
}

.profile-nav .user-heading h1 {
  font-size: 22px;
  font-weight: 300;
  margin-bottom: 5px;
}

.profile-nav .user-heading p {
  font-size: 12px;
}

.profile-nav ul {
  margin-top: 1px;
}

.profile-nav ul > li {
  border-bottom: 1px solid #ebeae6;
  margin-top: 0;
  line-height: 30px;
}

.profile-nav ul > li:last-child {
  border-bottom: none;
}

.profile-nav ul > li > a {
  border-radius: 0;
  -webkit-border-radius: 0;
  color: #89817f;
  border-left: 5px solid #fff;
}

.profile-nav ul > li > a:hover,
.profile-nav ul > li > a:focus,
.profile-nav ul li.active a {
  background: #f8f7f5 !important;
  border-left: 5px solid #fbc02d;
  color: #89817f !important;
}

.profile-nav ul > li:last-child > a:last-child {
  border-radius: 0 0 4px 4px;
  -webkit-border-radius: 0 0 4px 4px;
}

.profile-nav ul > li > a > i {
  font-size: 16px;
  padding-right: 10px;
  color: #bcb3aa;
}
</style>
