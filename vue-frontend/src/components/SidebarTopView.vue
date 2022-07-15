<template>
  <div class="product__sidebar">
                        <div class="product__sidebar__view">
                            <div class="section-title">
                                <h5>ТОП ПРОСМОТРОВ</h5>
                            </div>
                            <div class="filter__gallery">
                                    <div class="product__sidebar__view__item set-bg mix day years" style="background-image: url(https://ae04.alicdn.com/kf/H9ebb6f77a7864fef959de3ce7ef73c82g/-.jpg);">
                                        <div class="ep">12 / 12</div>
                                        <div class="view"><i class="bi bi-eye"></i> 54</div>
                                        <h5><a href="#">Jujutsu kaisen</a></h5>
                                    </div>
                            </div>
                            </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.product__sidebar .section-title h5 {
  color: #ffffff;
  font-weight: 600;
  font-family: "Oswald", sans-serif;
  line-height: 21px;
  text-transform: uppercase;
  padding-left: 20px;
  position: relative;
}

.product__sidebar .section-title h5:after {
  position: absolute;
  left: 0;
  top: -6px;
  height: 32px;
  width: 4px;
  background: #e53637;
  content: "";
}

.product__sidebar__view {
  position: relative;
  margin-bottom: 80px;
}

.product__sidebar__view .filter__controls {
  position: absolute;
  right: 0;
  top: -5px;
}

.product__sidebar__view .filter__controls li {
  list-style: none;
  font-size: 13px;
  color: #b7b7b7;
  display: inline-block;
  margin-right: 7px;
  cursor: pointer;
}

.product__sidebar__view .filter__controls li.active {
  color: #ffffff;
}

.product__sidebar__view .filter__controls li:last-child {
  margin-right: 0;
}

.product__sidebar__view__item {
  height: 190px;
  position: relative;
  border-radius: 5px;
  margin-bottom: 20px;
}

.product__sidebar__view__item .ep {
  font-size: 13px;
  color: #ffffff;
  background: #e53637;
  display: inline-block;
  padding: 2px 12px;
  border-radius: 4px;
  position: absolute;
  left: 10px;
  top: 10px;
}

.product__sidebar__view__item .view {
  font-size: 13px;
  color: #ffffff;
  background: #3d3d3d;
  display: inline-block;
  padding: 2px 10px;
  border-radius: 4px;
  position: absolute;
  right: 10px;
  top: 10px;
}

.product__sidebar__view__item h5 {
  position: absolute;
  left: 0;
  bottom: 25px;
  width: 100%;
  padding: 0 30px 0 20px;
}

.product__sidebar__view__item h5 a {
  color: #ffffff;
  font-weight: 700;
  line-height: 26px;
}
</style>
