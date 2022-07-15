<template>
<footer class="footer">
    <div class="page-up">
        <a href="#" id="scrollToTopButton"><i class="bi bi-arrow-up-short"></i></a>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-lg-3">
                <div class="footer__logo">
                    <a href="{% url 'anime:anime_list' %}"><img src="/static/img/logo.png" alt=""></a>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="footer__nav">
                    <ul>
                        <li><a href="{% url 'anime:anime_list' %}">Главная</a></li>
                        <li><a href="{% url 'anime:genre_list' %}">Жанры</a></li>
                        <li><a href="{% url 'anime:anime_all' %}">Все аниме</a></li>
                        <li><a href="{% url 'anime:anime_detail' slug=random_anime.url %}">Случайное аниме</a></li>
                    </ul>
                </div>
            </div>
            <div class="col-lg-3">
                <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
                    Copyright &copy; All rights reserved | AnimeStorage
                    <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
            </div>
        </div>
    </div>
</footer>
</template>

<script>

</script>

<style scoped>
.footer {
	background: #070720;
	padding-top: 60px;
	padding-bottom: 40px;
	position: relative;
}

.page-up {
	position: absolute;
	left: 50%;
	top: -25px;
	margin-left: -25px;
}

.page-up a {
	display: inline-block;
	font-size: 36px;
	color: #ffffff;
	height: 50px;
	width: 50px;
	background: #e53637;
	line-height: 50px;
	text-align: center;
	border-radius: 50%;
}

.page-up a span {
	position: relative;
	top: 2px;
	left: -1px;
}

.footer__nav {
	text-align: center;
}

.footer__nav ul li {
	list-style: none;
	display: inline-block;
	position: relative;
	margin-right: 40px;
}

.footer__nav ul li:last-child {
	margin-right: 0;
}

.footer__nav ul li a {
	font-size: 15px;
	color: #b7b7b7;
	display: block;
	font-weight: 700;
}

.footer__copyright__text {
	color: #b7b7b7;
	margin-bottom: 0;
	text-align: right;
}

.footer__copyright__text a {
	color: #e53637;
}

</style>