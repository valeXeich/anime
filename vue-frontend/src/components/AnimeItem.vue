<template>
  <div class="col-lg-4 col-md-6 col-sm-6">
    <div class="product__item">
      <div
        class="product__item__pic set-bg"
        style="background-image: url(https://ae04.alicdn.com/kf/H9ebb6f77a7864fef959de3ce7ef73c82g/-.jpg);"
      >
        <div class="ep">
          12 / 12
        </div>
        <div class="comment">
          <i class="bi bi-chat"></i> 15
        </div>
        <div class="view">
          <i class="bi bi-eye"></i> 5
        </div>
      </div>
      <div class="product__item__text">
        <ul>
          <li>Ongoing</li>
          <li>2022</li>
        </ul>
        <h5>
          <a href="#">Jujutsu kaisen</a>
        </h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.product__item {
	margin-bottom: 30px;
}

.product__item__pic {
	height: 325px;
	position: relative;
	border-radius: 5px;
}

.product__item__pic .ep {
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

.product__item__pic .comment {
	font-size: 13px;
	color: #ffffff;
	background: #3d3d3d;
	display: inline-block;
	padding: 2px 10px;
	border-radius: 4px;
	position: absolute;
	left: 10px;
	bottom: 10px;
}

.product__item__pic .view {
	font-size: 13px;
	color: #ffffff;
	background: #3d3d3d;
	display: inline-block;
	padding: 2px 10px;
	border-radius: 4px;
	position: absolute;
	right: 10px;
	bottom: 10px;
}

.product__item__text {
	padding-top: 20px;
}

.product__item__text ul {
	margin-bottom: 10px;
}

.product__item__text ul li {
	list-style: none;
	font-size: 10px;
	color: #ffffff;
	font-weight: 700;
	padding: 1px 10px;
	background: rgba(255, 255, 255, 0.2);
	border-radius: 50px;
	display: inline-block;
}

.product__item__text h5 a {
	color: #ffffff;
	font-weight: 700;
	line-height: 26px;
}
</style>
