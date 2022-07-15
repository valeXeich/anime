<template>
    <div class="anime__details__form">
                        
                            <div class="section-title">
                                <h5>Оставить отзыв</h5>
                            </div>
                            <form method="POST">
                                
                                <textarea></textarea>
                                <button type="submit"><i class="bi bi-send"></i>Отправить</button>
                            </form>
                        
                    </div>
                    <div class="anime__details__review mt-5">
                        <div class="section-title">
                            <h5>Отзывы</h5>
                        </div>
                        
                            <div class="anime__review__item">
                                <div class="anime__review__item__pic">
                                    <a href="#"><img src="https://i.pinimg.com/originals/b9/a4/ca/b9a4caf4948ac1d4dd6bfdd63bd178d9.jpg" alt="avatar"></a>
                                </div>
                                <div class="anime__review__item__text">
                                    <h6 class="prof-link"><a href="#">valex</a> -<span> 12.05.2021</span></h6>
                                    <p>Very Good!</p>
                                        <form method="post">
                                            <button class="btn btn-outline-danger" type="submit">Удалить</button>
                                        </form>
                                </div>
                            </div>
                        
                    </div>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>
.anime__details__review {
	margin-bottom: 55px;
}

.anime__details__form form textarea {
	width: 100%;
	font-size: 15px;
	color: #b7b7b7;
	padding-left: 20px;
	padding-top: 12px;
	height: 110px;
	border: none;
	border-radius: 5px;
	resize: none;
	margin-bottom: 24px;
}

.anime__details__form form button {
	font-size: 11px;
	color: #ffffff;
	font-weight: 700;
	letter-spacing: 2px;
	text-transform: uppercase;
	background: #e53637;
	border: none;
	padding: 10px 15px;
	border-radius: 2px;
}

.anime__details__form button {
	font-size: 11px;
	color: #ffffff;
	font-weight: 700;
	letter-spacing: 2px;
	text-transform: uppercase;
	background: #e53637;
	border: none;
	padding: 10px 15px;
	border-radius: 2px;
}

.anime__review__item {
	overflow: hidden;
	margin-bottom: 15px;
}

.anime__review__item__pic {
	float: left;
	margin-right: 20px;
	position: relative;
}

.anime__review__item__pic:before {
	position: absolute;
	right: -30px;
	top: 15px;
	border-top: 15px solid transparent;
	border-left: 15px solid #1d1e39;
	content: "";
	-webkit-transform: rotate(45deg);
	-ms-transform: rotate(45deg);
	transform: rotate(45deg);
}

.anime__review__item__pic img {
	height: 50px;
	width: 50px;
	border-radius: 50%;
}

.anime__review__item__text {
	overflow: hidden;
	background: #1d1e39;
	padding: 18px 30px 16px 20px;
	border-radius: 10px;
}

.anime__review__item__text h6 {
	color: #ffffff;
	font-weight: 700;
	margin-bottom: 10px;
}

.anime__review__item__text h6 span {
	color: #b7b7b7;
	font-weight: 400;
}

.anime__review__item__text p {
	color: #b7b7b7;
	line-height: 23px;
	margin-bottom: 0;
}

.prof-link a:hover {
    color: #fff;
}
</style>