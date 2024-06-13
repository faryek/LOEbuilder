<template>
    <NuxtLink :to="`/build/${id}`" class="card border-shine flex flex-row gap-10 p-5">
        <img :src="`../img/classes/${build_class}/Medium.png`" alt="">
        <div class="flex flex-col gap-2">
            <p class="font text-2xl" style="color: #C68200;">{{league}}</p>
            <p class="font text-2xl">{{build_name}}</p>
            <p class="font text-xl">Уровень: {{ build_lvl }}</p>
            <p class="font text-xl">{{build_class_name}}</p>
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

.card {
    background-color: rgba(0, 0, 0, 0.5);
    border-radius: 25px;
    width: 45%;
    height: 200px;
    border: 3px solid rgba(0,0,0,0);
}


.card img {
    border-radius: 15px;
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