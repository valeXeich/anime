<template>
    <section class="normal-breadcrumb set-bg">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 text-center">
                    <div class="normal__breadcrumb__text">
                        <h2>Регистрация</h2>
                        <p>Добро пожаловать в AnimeStorage.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>
/*---------------------
    Normal Breadcrumb
-----------------------*/

.normal-breadcrumb {
	height: 300px;
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	justify-content: center;
}

.normal__breadcrumb__text h2 {
	color: #ffffff;
	font-size: 48px;
	font-family: "Oswald", sans-serif;
	font-weight: 700;
	margin-bottom: 22px;
}

.normal__breadcrumb__text p {
	color: #ffffff;
	font-size: 24px;
	margin-bottom: 0;
}
</style>