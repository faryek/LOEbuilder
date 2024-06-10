<template>
    <div class="container p-5 flex flex-col justify-between align-middle">
        <div class="flex flex-row justify-between align-middle gap-5" style="width: 100%;">
            <img class="item-img" :src="`..${image}`" alt="">
            <div class="flex flex-col justify-evenly">
                <div class="flex flex-row gap-2">
                    <p class="text-xl font">{{ name }}</p>
                    <p class="text-xl font">{{ sub_name }}</p>
                </div>
                <div class="flex flex-row gap-2">
                    <p class="text-xl font">+{{ implicits_value_start }}</p>
                    <p class="text-xl font">-</p>
                    <p class="text-xl font">{{ implicits_value_end }}</p>
                    <p class="text-xl font">{{ implicits_effect }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
const props = defineProps(['image', 'name', 'sub_name', 'implicits_value_start', 'implicits_value_end', 'implicits_effect'])
</script>

<script>
export default {
    data() {
        return {
            
        }
    },
}
</script>

<style></style>