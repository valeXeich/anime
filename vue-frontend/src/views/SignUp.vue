<template>
    <!-- Normal Breadcrumb Begin -->
    <Breadcrumb></Breadcrumb>
    <!-- Normal Breadcrumb End -->
    <!-- Signup Section Begin -->
    <section class="signup spad">
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <div class="login__form">
                        <h3>Регистрация</h3>
                        <form method="post">
                            <div class="input__item">
                                <input type="text" placeholder="Username">
                                <span class="bi bi-person-fill"></span>
                            </div>
                            <div class="input__item">
                                <input type="email" placeholder="Email">
                                <span class="bi bi-envelope"></span>
                            </div>
                            <div class="input__item">
                                <input type="password" placeholder="Password">
                                <span class="bi bi-shield-lock"></span>
                            </div>
                            <div class="input__item">
                                <input type="password" placeholder="Repeat Password">
                                <span class="bi bi-shield-lock"></span>
                            </div>
                            <button type="submit" class="site-btn">Зарегистрироваться</button>
                        </form>
                        <h5>У вас уже есть аккаунт? <a href="#">Авторизоваться!</a></h5>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="login__social__links">
                        <h3>Наши соц.сети:</h3>
                        <ul>
                            <li><a href="#" class="facebook"><i class="fa fa-facebook"></i>Facebook</a>
                            </li>
                            <li><a href="#" class="twitter"><i class="fa fa-twitter"></i>Twitter</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Signup Section End -->
</template>

<script>
import Breadcrumb from '@/components/Breadcrumb.vue'
    export default {
        components: {
			Breadcrumb
		}
    }
</script>

<style scoped>
.signup {
	padding-top: 130px;
	padding-bottom: 150px;
}

.signup .login__form:after {
	height: 450px;
}

.signup .login__form h5 {
	font-size: 15px;
	color: #ffffff;
	margin-top: 36px;
}

.signup .login__form h5 a {
	color: #e53637;
	font-weight: 700;
}

.signup .login__social__links {
	text-align: left;
	padding-left: 40px;
}

.signup .login__social__links h3 {
	color: #ffffff;
	font-weight: 700;
	font-family: "Oswald", sans-serif;
	margin-bottom: 30px;
}

.signup .login__social__links ul li a {
	margin: 0;
	text-align: center;
}

.login__form form .input__item {
	position: relative;
	width: 370px;
	margin-bottom: 20px;
}

.login__form form .input__item:before {
	position: absolute;
	left: 50px;
	top: 10px;
	height: 30px;
	width: 1px;
	background: #b7b7b7;
	content: "";
}

.login__form form .input__item input {
	height: 50px;
	width: 100%;
	font-size: 15px;
	color: #b7b7b7;
	background: #ffffff;
	border: none;
	padding-left: 76px;
}

.login__form form .input__item input::-webkit-input-placeholder {
	color: #b7b7b7;
}

.login__form form .input__item input::-moz-placeholder {
	color: #b7b7b7;
}

.login__form form .input__item input:-ms-input-placeholder {
	color: #b7b7b7;
}

.login__form form .input__item input::-ms-input-placeholder {
	color: #b7b7b7;
}

.login__form form .input__item input::placeholder {
	color: #b7b7b7;
}

.login__form form .input__item span {
	color: #b7b7b7;
	font-size: 20px;
	position: absolute;
	left: 15px;
	top: 13px;
}
</style>