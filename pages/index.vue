<template>
    <div class="flex flex-row justify-evenly">
        <select name="" id="" class="selector border-shine">
            <option value="Мать" class="selector">Все</option>
            <option value="Мать" class="selector">не все</option>
            <option value="Мать" class="selector">Светка</option>
            <option value="Мать" class="selector">Колька</option>
        </select>
        <select name="" id="" class="selector border-shine">
            <option value="Мать" class="selector">Стартер</option>
            <option value="Мать" class="selector">Эндгейм</option>
        </select>
        <select name="" id="" class="selector border-shine">
            <option value="Мать" class="selector">Боссинг</option>
            <option value="Мать" class="selector">Маппинг</option>
        </select>
    </div>
    <div class="container character_selector">
        <div class="wrapper flex flex-row relative justify-between">
            <div class="icon char_icon1 flex flex-col-reverse" v-for="i in 8">
                <img :src="`_nuxt/assets/img/classes/${classes[i - 1]}/Small.png`" alt="" @mouseenter="() => {
                    hovering=1
                    console.log(hovering)
                }" @mouseleave="() => {
                        hovering=0
                        console.log(hovering)
                    }">
                <p v-if="hovering == 1">{{ classes_ru[i - 1] }}</p>
            </div>

        </div>
    </div>
</template>

<script setup>
let hovering
const classes = ['Antihrist', 'Bogatir', 'Bogolub', 'Zastrel', 'Medvesh', 'Pahan', 'Skomoroh', 'Yazich']
const classes_ru = ['Антихрист', 'Богатырь', 'Боголюб', 'Застрельщица', 'Налетчик', 'Богохульник', 'Скоморох', 'Язычница']
</script>

<style>
.selector {
    border: 3px solid rgba(0, 0, 0, 0);
    border-radius: 25px;
}

.icon {
    height: 110px;
    width: 110px;
    border-radius: 15px;
    z-index: 10;
}

.icon img {
    height: 110px;
    width: 110px;
    object-fit: cover;
    border-radius: 15px;
    z-index: -1;
}

.icon p {
    /* position: absolute; */
    width: 110px;
    background-color: white;
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
}
</style>