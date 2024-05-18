<template>
    <button class="card-block w-100 px-5" style="display: flex; flex-direction: row; justify-content: space-between;">
        <p class="text-lg font">{{ league }}</p>
        <p class="text-lg font">{{ build_name }}</p>
        <p class="text-lg font">{{ build_lvl }}</p>
        <p class="text-lg font">{{ build_class_name }}</p>
        <p class="text-lg font">{{ build_ehp }}</p>
        <p class="text-lg font">{{ build_dps }}</p>
        <p class="text-lg font">{{ build_date }}</p>
    </button>
</template>

<script setup>
const props = defineProps(['league', 'build_name', 'build_lvl', 'build_class_name', 'build_class', 'id', 'build_date', 'build_ehp', 'build_dps', 'more'])
</script>

<script>

</script>

<style>
.card-block p {
    color: white;
    width: 15%;
    text-align: center;
}

</style>