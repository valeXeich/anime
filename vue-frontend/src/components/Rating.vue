<template>
  <div class="rating">
    <ul class="list">
      <li @click="$emit('star', star), rate(star)" v-for="star in maxStars" :class="{ 'active': star <= stars }" :key="star.stars" class="star">
      <i :class="star <= stars ? 'bi bi-star-fill' : 'bi bi-star'"></i> 
      </li>
      8.8
    </ul>
  </div>
</template>
<script>
export default {
  name: 'Rating',
  props: ['grade', 'maxStars', 'hasCounter'],
  data() {
    return {
      stars: this.grade
    }
  },
  methods: {
    rate(star) {
      if (typeof star === 'number' && star <= this.maxStars && star >= 0) {
        this.stars = this.stars === star ? star - 1 : star
      }
    }
  },
}
</script>

<style scoped lang="scss">
  @import '@/assets/css/rating.scss';
</style>