<template>
    <!-- Normal Breadcrumb Begin -->
    <Breadcrumb></Breadcrumb>
    <!-- Normal Breadcrumb End -->
    <!-- Login Section Begin -->
    <section class="login spad">
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <div class="login__form">
                        <h3>Авторизация</h3>
                        <form method="POST">
                        
                            <div class="input__item">
                                <input type="text" placeholder="Username">
                                <span class="bi bi-person-fill"></span>
                            </div>
                            <div class="input__item">
                                <input type="password" placeholder="Password">
                                <span class="bi bi-shield-lock"></span>
                            </div>
                            <button type="submit" class="site-btn">Войти</button>
                        </form>
                        <a href="#" class="forget_pass">Забыли пароль?</a>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="login__register">
                        <h3>Нет учетной записи?</h3>
                        <a href="#" class="primary-btn">Зарегистрироваться</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Login Section End -->
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
/*---------------------
  Login
-----------------------*/

.login {
	padding-top: 130px;
	padding-bottom: 120px;
}

.login__form {
	position: relative;
	padding-left: 145px;
}

.login__form:after {
	position: absolute;
	right: -14px;
	top: -40px;
	height: 330px;
	width: 1px;
	background: rgba(255, 255, 255, 0.2);
	content: "";
}

.login__form h3 {
	color: #ffffff;
	font-weight: 700;
	font-family: "Oswald", sans-serif;
	margin-bottom: 30px;
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

.login__form form button {
	border-radius: 0;
	margin-top: 10px;
}

.login__form .forget_pass {
	font-size: 15px;
	color: #ffffff;
	display: inline-block;
	position: absolute;
	right: 60px;
	bottom: 12px;
}

.login__register {
	padding-left: 30px;
}

.login__register h3 {
	color: #ffffff;
	font-weight: 700;
	font-family: "Oswald", sans-serif;
	margin-bottom: 30px;
}

.login__register .primary-btn {
	background: #e53637;
	padding: 12px 42px;
}

.login__social {
	padding-top: 52px;
}

.login__social__links {
	text-align: center;
}

.login__social__links span {
	color: #ffffff;
	display: block;
	font-size: 13px;
	font-weight: 700;
	letter-spacing: 2px;
	text-transform: uppercase;
	margin-bottom: 30px;
}

.login__social__links ul li {
	list-style: none;
	margin-bottom: 15px;
}

.login__social__links ul li:last-child {
	margin-bottom: 0;
}

.login__social__links ul li a {
	color: #ffffff;
	display: block;
	font-size: 13px;
	font-weight: 700;
	letter-spacing: 2px;
	text-transform: uppercase;
	width: 460px;
	padding: 14px 0;
	position: relative;
	margin: 0 auto;
}

.login__social__links ul li a.facebook {
	background: #4267b2;
}

.login__social__links ul li a.google {
	background: #ff4343;
}

.login__social__links ul li a.twitter {
	background: #1da1f2;
}

.login__social__links ul li a i {
	font-size: 20px;
	position: absolute;
	left: 32px;
	top: 14px;
}
</style>