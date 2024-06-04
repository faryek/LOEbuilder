<template>
    <NuxtLink :to="`/build/${id}`" class="card border-shine flex flex-row gap-2">
        <img :src="`../img/classes/${build_class}/Medium.png`" alt="">
        <div class="right flex flex-col">
            <h2 class="right__league font">{{league}}</h2>
            <h1 class="right__name font">{{build_name}}</h1>
            <p class="right__lvl font">Уровень: {{ build_lvl }}</p>
            <p class="right__class font">{{build_class_name}}</p>
        </div>
    </NuxtLink>
</template>

<script setup>
    const props = defineProps(['league','build_name','build_lvl','build_class','id', 'build_class_name'])

</script>

<style scoped>
@font-face {
    font-family: 'TLheader-Regular';
    src: url(/fonts/TLheader-Regular.ttf);
}

.font {
    font-family: 'TLheader-Regular';
}

h2 {
    color: #C68200;
    font-size: 28px;
}

h1 {
    color: white;
    font-size: 44px;
}

p {
    color: white;
    font-size: 24px;
}

.card {
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 25px;
    width: 45%;
    height: 200px;
    padding: 15px;
    border: 3px solid rgba(0,0,0,0);
}


.card img {
    border-radius: 25px;
}


@media screen and (max-width: 1023px) {
    .card {
        width: 100%;
        border: 3px solid;
        border-color: #9b7e41;
        padding: 12px;
        box-shadow: 0 0 10px 0 #9b7e41;
    }
}
</style>