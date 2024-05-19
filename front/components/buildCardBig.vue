<template>
    <div ref="dropdown" class="dropdown">
        <div class="dropdown-label card-block w-100 px-5"
            style="display: flex; flex-direction: row; justify-content: space-between;" @click="show = !show">
            <p class="text-lg font">{{ league }}</p>
            <p class="text-lg font">{{ build_name }}</p>
            <p class="text-lg font">{{ build_lvl }}</p>
            <p class="text-lg font">{{ build_class_name }}</p>
            <p class="text-lg font">{{ build_ehp }}</p>
            <p class="text-lg font">{{ build_dps }}</p>
            <p class="text-lg font">{{ build_date }}</p>
        </div>
        <div class="dropdown-content" v-if="show" style="color: white;">
            <NuxtLink :to="`/build/${id}`" class="card flex flex-row gap-2">
                <img :src="'../assets/img/classes/'+build_class+'/Fulllength.png'" alt="">
                <div class="right flex flex-col">
                    <h2 class="right__league font">{{ league }}</h2>
                    <h1 class="right__name font">{{ build_name }}</h1>
                    <p class="right__lvl font">Уровень: {{ build_lvl }}</p>
                    <p class="right__class font">{{ build_class_name }}</p>
                </div>
            </NuxtLink>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import autoAnimate from "@formkit/auto-animate"

const props = defineProps(['league', 'build_name', 'build_lvl', 'build_class_name', 'build_class', 'id', 'build_date', 'build_ehp', 'build_dps', 'more'])

const dropdown = ref() // we need a DOM node
const show = ref(false)

onMounted(() => {
    autoAnimate(dropdown.value) // thats it!
})
</script>

<script>
export default {
    data() {
        return {
            
        }
    }
}
</script>

<style>
.card-block p {
    color: white;
    width: 15%;
    text-align: center;
}
</style>