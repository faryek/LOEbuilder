<template>
    <div ref="dropdown" class="dropdown">
        <NuxtLink to="/" class="dropdown-label" @click="() => { show = !show; show_drop = !show_drop }">
            <div v-show="show_drop" class="card-block w-100 px-5 py-5"
                style="display: flex; flex-direction: row; justify-content: space-between;">
                <p class="text-lg font">{{ league }}</p>
                <p class="text-lg font">{{ build_name }}</p>
                <p class="text-lg font">{{ build_lvl }}</p>
                <p class="text-lg font">{{ build_class_name }}</p>
                <p class="text-lg font">{{ build_ehp }}</p>
                <p class="text-lg font">{{ build_dps }}</p>
                <p class="text-lg font">{{ build_author }}</p>
            </div>
            <div v-show="!show_drop" class="hide font text-lg px-5 py-5 mb-2" style="width: 100%; text-align: center">
                Скрыть</div>
        </NuxtLink>
        <div class="dropdown-content" v-if="show" style="color: white;">
            <NuxtLink class="card flex flex-row px-10 pb-10 pt-5 justify-between">
                <div class="right flex flex-col">
                    <div class="flex flex-col gap-2">
                        <p class="text-4xl font">{{ build_name }}</p>
                        <p class="text-2xl font" style="color: #C68200;">{{ league }}</p>
                    </div>
                    <p class="text-2xl font">Уровень: {{ build_lvl }}</p>
                    <p class="text-2xl font">Класс: {{ build_class_name }}</p>
                </div>
                <img class="class-img" :src="`../img/classes/${build_class}/Medium.png`" alt="">
            </NuxtLink>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import autoAnimate from "@formkit/auto-animate"

//const props = defineProps(['league', 'build_name', 'build_lvl', 'build_class_name', 'build_class', 'id', 'build_date', 'build_ehp', 'build_dps', 'more', 'selected'])

const dropdown = ref() // we need a DOM node
const show = ref(false)



onMounted(() => {
    autoAnimate(dropdown.value) // thats it!
})
</script>

<script>
export default {
    props: ['league', 'build_name', 'build_lvl', 'build_class_name', 'build_class', 'id', 'build_author', 'build_ehp', 'build_dps', 'more', 'selected'],
    data() {
        return {
            show_drop: true,
        }
    },
}
</script>

<style>
.hide {
    border: 3px solid;
    border-color: rgba(94, 94, 94, 0);
    border-radius: 13px;
}

.hide:hover {
    border: 3px solid;
    border-color: rgba(94, 94, 94, 0.24);
    border-radius: 13px;
}

.card-block p {
    color: white;
    width: 15%;
    text-align: center;
}

.class-img {
    border: 3px solid;
    border-color: rgba(0, 0, 0, 0);
    object-fit: cover;
    border-radius: 13px;
}
</style>