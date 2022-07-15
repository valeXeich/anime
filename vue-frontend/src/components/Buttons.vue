<template>
    <div class="btn-group" role="group" aria-label="Basic example">
        <form  method="post">
            
            <button class="btn btn-danger btn-sm watching-btn">Смотрю</button>
            <input type="hidden" name="model_name" value="WatchingNow">
            <input type="hidden" name="anime_id" value="">
        </form>

        <form method="post">
            
            <button class="btn btn-dark btn-sm will_watching-btn">Буду смотреть</button>
            <input type="hidden" name="model_name" value="WillWatch">
            <input type="hidden" name="anime_id" value="">
        </form>

    
        <form  method="post">
            
            <button class="btn btn-dark btn-sm watching-btn">Брошено</button>
            <input type="hidden" name="model_name" value="Throw">
            <input type="hidden" name="anime_id" value="">
        </form>
    
</div>
<div class="d-grid gap-2">
        <form method="post">
            
            <button class="btn btn-dark btn-sm viewed-btn">Просмотрено</button>
            <input type="hidden" name="model_name" value="Viewed">
            <input type="hidden" name="anime_id" value="">
        </form>
</div>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>
.watching-btn {
	width: 79px;
}

.will_watching-btn {
	width: 112px;
}

.viewed-btn {
	width: 270px;
}

</style>