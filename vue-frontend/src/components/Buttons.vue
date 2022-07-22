<template>
  <div class="btn-group" role="group" aria-label="Basic example">
    <button
      @click="$emit('click', 'WatchingNow')"
      class="btn btn-danger btn-sm watching-btn"
    >
      Смотрю
    </button>

    <button
      @click="$emit('click', 'WillWatch')"
      class="btn btn-dark btn-sm will_watching-btn"
    >
      Буду смотреть
    </button>
    <button @click="$emit('click', 'Throw')" class="btn btn-dark btn-sm watching-btn">
      Брошено
    </button>
  </div>
  <div class="d-grid gap-2">
    <button @click="$emit('click', 'Viewed')" class="btn btn-dark btn-sm viewed-btn">
      Просмотрено
    </button>
  </div>
</template>

<script>
export default {
  props: {
    animeTitle: {
      type: String,
      require: true
    },
    animeList: {
      type: Object,
      require: true
    },
  },

};
</script>

<style scoped>
.watching-btn {
  width: 73px;
}

.will_watching-btn {
  width: 112px;
}

.viewed-btn {
  width: 256px;
}
</style>
