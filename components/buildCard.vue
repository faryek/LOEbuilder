<template>
    <div class="card flex flex-row">
        <img src="../assets/img/classes/Антихрист/Medium.png" alt="">
        <div class="right flex flex-col">
            <h2 class="right__league">Первое бытие</h2>
            <h1 class="right__name">xdders</h1>
            <p class="right__lvl">уровень 100</p>
            <p class="right__class">Антихрист</p>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
    h2{
        color: #C68200;
    }
    h1,p{
        color: white;
    }
    .card{
        background-color: rgba(0, 0, 0, 0.5);
        border-radius: 25px;
        width: 45%;
        height: 200px;
        border: 3px;
        padding: 15px;
    }
    .card img{
        border-radius: 25px;
    }
    .card:hover{
        border: 3px solid;
        border-color: #9b7e41;
        padding: 12px;
    }
</style>