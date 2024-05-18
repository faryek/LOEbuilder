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
    <div class="container character_selector mt-4">
        <div class="wrapper flex flex-row relative justify-between">
            <div class="icon char_icon1 flex flex-col-reverse border-shine" v-for="i in 8">
                <img :src="`_nuxt/assets/img/classes/${classes[i - 1]}/Small.png`" alt="" class="icon-image">
                <p class="icon-text font">{{ classes_ru[i - 1] }}</p>
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

.border-shine{
    border-radius: 15px !important;
}

.border-shine:hover{
    .icon-image{
        border-bottom-left-radius: 0 !important;
        border-bottom-right-radius: 0 !important;
    }
}

.icon {
    display: flex;
    flex-direction: column;
    border: 3px solid;
    border-color: rgba(0, 0, 0, 0);
}

.icon-image {
    height: 114px;
    width: 114px;
    object-fit: cover;
    border-radius: 13px;
    z-index: 1;
}

.icon-text {
    display: none;
    width: 100%;
    background-color: rgb(0, 0, 0);
    border-bottom-left-radius: 13px;
    border-bottom-right-radius: 13px;
    z-index: 10;
    text-align: center;
    color: #ffffff !important;
}
</style>