<template>
    <div class="container flex flex-col items-center"><NuxtLink :to="`${0}`" class="create-build-btn" >Создать новый билд!</NuxtLink></div>
    <div class="container flex flex-row flex-wrap justify-between gap-y-10">
        <buildCard v-for="i in 7" :league="'Первое бытие'" :build_class="'Антихрист'" :build_lvl="100" :build_name="'xdders'" :id="i"></buildCard>
    </div>
</template>

<script setup>


</script>

<style>
.create-build-btn {
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    border-radius: 25px;
    width: 45%;
    height: 50px;
    border: 3px;
    padding: 15px;
    font-family: 'TLheader-Regular';
    margin-bottom: 35px;
    font-size: 18px;
    box-shadow: 0 0 10px 0 #9b7e41;
    text-align: center;
    
}
.create-build-btn:hover {
    border: 3px solid;
    border-color: #9b7e41;
    padding: 12px;
    box-shadow: 0 0 20px 0 #9b7e41;
}
</style>