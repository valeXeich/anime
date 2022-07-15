<template>
  <div class="product__sidebar__comment">
    <div class="section-title">
      <h5>Новый комментарий</h5>
    </div>

    <div class="product__sidebar__comment__item">
      <div class="product__sidebar__comment__item__pic">
        <img class="anime-poster" src="https://ae04.alicdn.com/kf/H9ebb6f77a7864fef959de3ce7ef73c82g/-.jpg" alt="" />
      </div>
      <div class="product__sidebar__comment__item__text">
        <ul>
          <li>Ongoing</li>
          <li>2020</li>
        </ul>
        <h5>
          <a href="#">Jujutsu kaisen</a>
        </h5>
        <span
          ><i class="bi bi-eye"></i> 43 Просмотров</span
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.product__sidebar__comment {
  margin-bottom: 35px;
}

.product__sidebar__comment__item {
  margin-bottom: 20px;
  overflow: hidden;
}

.product__sidebar__comment__item__pic {
  float: left;
  margin-right: 15px;
}

.product__sidebar__comment__item__text {
  overflow: hidden;
}

.product__sidebar__comment__item__text ul {
  margin-bottom: 10px;
}

.product__sidebar__comment__item__text ul li {
  list-style: none;
  font-size: 10px;
  color: #ffffff;
  font-weight: 700;
  padding: 1px 10px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50px;
  display: inline-block;
}

.product__sidebar__comment__item__text h5 {
  margin-bottom: 10px;
}

.product__sidebar__comment__item__text h5 a {
  color: #ffffff;
  font-weight: 700;
  line-height: 26px;
}

.product__sidebar__comment__item__text span {
  display: block;
  font-size: 13px;
  color: #b7b7b7;
}
</style>
