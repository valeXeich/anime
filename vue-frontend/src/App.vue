<template>
  <Header></Header>
  <router-view></router-view>
  <Footer></Footer>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';
export default {
  components: {
    Header,
    Footer
  },
}
</script>

<style>
@import url(https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css);
@import url(https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css);
@import './assets/css/main.css';

</style>
