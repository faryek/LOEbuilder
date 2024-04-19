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
            <div class="icon char_icon1 flex flex-col-reverse">
                <p>Антихрист</p><img src="/assets/img/classes/Antihrist/Small.png" alt="">
            </div>
            <div class="icon char_icon2 flex flex-col-reverse">
                <p>Богатырь</p><img src="/assets/img/classes/Bogatir/Small.png" alt="">
            </div>
            <div class="icon char_icon3 flex flex-col-reverse">
                <p>Боголюб</p><img src="/assets/img/classes/Bogolub/Small.png" alt="">
            </div>
            <div class="icon char_icon4 flex flex-col-reverse">
                <p>Застрельщица</p><img src="/assets/img/classes/Zastrel/Small.png" alt="">
            </div>
            <div class="icon char_icon5 flex flex-col-reverse">
                <p>Налётчик</p><img src="/assets/img/classes/Medvesh/Small.png" alt="">
            </div>
            <div class="icon char_icon6 flex flex-col-reverse">
                <p>Богохульник</p><img src="/assets/img/classes/Pahan/Small.png" alt="">
            </div>
            <div class="icon char_icon7 flex flex-col-reverse">
                <p>Скоморох</p><img src="/assets/img/classes/Skomoroh/Small.png" alt="">
            </div>
            <div class="icon char_icon8 flex flex-col-reverse">
                <p>Язычница</p><img src="/assets/img/classes/Yazich/Small.png" alt="">
            </div>
        </div>
    </div>
</template>

<script setup>

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
}

.icon img {
    height: 110px;
    width: 110px;
    object-fit: cover;
    border-radius: 15px;
}

.icon p {
    position: absolute;
    width: 110px;
    background-color: white;
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
}
</style>