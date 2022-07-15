<template>
    <section class="anime-details spad">
        <div class="container">
            <div class="anime__details__content">
                <div class="row">
                    <div class="col-lg-3">
                        <div class="anime__details__pic set-bg" style="background-image: url(https://ae04.alicdn.com/kf/H9ebb6f77a7864fef959de3ce7ef73c82g/-.jpg);">
                                
                                
                               
                                    <form method="post">
                                        
                                        <div class="favorite"><button class="btn btn-outline-danger"><i class="bi bi-heart"></i></button></div>
                                        <input type="hidden" name="anime_id" value="">
                                    </form>
                                
                    
                            <div class="comment"><i class="bi bi-chat"></i> 43</div>
                            <div class="view"><i class="bi bi-eye"></i> 23</div>
                        </div>

                        <Buttons></Buttons>
                    </div>

                    <div class="col-lg-9">
                        <div class="anime__details__text">
                            <div class="anime__details__title">
                                <h3>Jujutsu kaisen</h3>
                                <span>Jujutsu kaisen 2</span>
                            </div>
                            <p class="mt-2">uiuiuiuiu</p>
                            <div class="anime__details__widget">
                                <div class="row">
                                    <div class="col-lg-6 col-md-6">
                                        <ul class="red-link">
                                            <li><span>Тип:</span> Serial</li>
                                            <li><span>Студия:</span> <a href="#">MAPPA</a></li>
                                            <li><span>Дата выхода:</span> 2022</li>
                                            <li><span>Статус:</span> Ongoing</li>
                                            <li><span>Жанры:</span> <a href="#">Isekai, Horror </a></li>
                                            <li><span>Режиссеры:</span> <a href="#">Vasya, Tolya </a></li>
                                        </ul>
                                    </div>
                                    <div class="col-lg-6 col-md-6">
                                        <ul>
                                            <li><span>Рейтинг:</span>Нету оценок</li>
                                            <li><span>Воз. рейтинг:</span> 16+</li>
                                            <li><span>Качество:</span> HD</li>
                                            <li><span>Просмотров:</span>54</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="anime__details__btn">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <AnimeShots></AnimeShots>
            <div class="row">
                <div class="col-lg-8 col-md-8">
                    <Comments></Comments>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    import Buttons from '@/components/Buttons.vue'
    import AnimeShots from '@/components/AnimeShots.vue'
    import Comments from '@/components/Comments.vue'
    export default {
        components: {
            Buttons,
            AnimeShots,
            Comments
        },
        name: 'anime-detail',
    }
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