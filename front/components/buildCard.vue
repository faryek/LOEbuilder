<template>
    <NuxtLink :to="`/build/${url}`" class="card2 border-shine flex flex-row gap-10">
        <div class="card flex flex-row gap-10 p-5" style="border-color: black !important;box-shadow: none !important; background-color: rgba(0, 0, 0, 0);border: 0px;">
            <img :src="`../img/classes/${build_class}/Medium.png`" alt="">
            <div class="media-text flex flex-col gap-2" style="min-width: 200px;">
                <p class="font text-2xl" style="color: #C68200;">{{league}}</p>
                <p class="font text-2xl">{{build_name}}</p>
                <p class="font text-xl">Уровень: {{ build_lvl }}</p>
                <p class="font text-xl">{{build_class_name}}</p>
            </div>
        </div>
    </NuxtLink>
    <div class="deleting flex justify-center" style="max-width: 100%;" @click="()=>{
            back= true
        }">
            <img :src="`../img/icons/delete.png`" alt="" style="object-fit: contain;max-width: 40px;">
        </div>
    <div class="login-background" style="z-index:5 !important;position: fixed; top: 0; left: 0; z-index: 500;"
        @click="() => {back = false }" v-if="back"></div>
    <CommonError v-if="error"></CommonError>
    <div class="accepting p-10" style="z-index: 500 !important; position: fixed; top: 25%; left: 35%;" v-if="back" v-auto-animate>
        <p class="font text-4xl">Удалить билд?</p>
        <div class="flex flex-row align-middle justify-center gap-2">
            <button @click="() => {
                delete_build()
                back=false
            }" class="login-btn text-xl font py-1 px-5">Да</button>
            <button @click="() => { back = false }" class="login-btn text-xl font py-1 px-5">Нет</button>
        </div>
    </div>
</template>

<script setup>
    const props = defineProps(['id','league','build_name','build_lvl','build_class','url', 'build_class_name'])

</script>

<script>
    export default {
    data() {
        return {
            back: false,
            error: false
        }
    },
    methods:{
        delete_build() {
            let token = localStorage.getItem('token')
            fetch(`http://127.0.0.1:8000/build/delete/${this.id}`, {
                method: 'DELETE',
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            }).then(response => response.json())
                .then(json => {
                    if (json.detail) {
                        this.error = true
                        return null
                    }
                    this.$emit('deleted')
                })
            return null
        },
    }
}
</script>

<style scoped>
@font-face {
    font-family: 'TLheader-Regular';
    src: url(/fonts/TLheader-Regular.ttf);
}

.accepting{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 5vh;
    width: 30%;
    background-color: black;
    border: 3px solid;
    border-radius: 25px;
    border-color: #9b7e41 !important;
    box-shadow: 0 0 20px 0 #9b7e41;
}

.login-background {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.623);
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

.card2{
        width: 45%;
        background-color: rgba(0, 0, 0, 0.5);
        border-radius: 25px;
        height: 200px;
        border: 3px solid rgba(0,0,0,0);
    }

@media screen and (max-width: 1538px) {
    .card {
        width: 100%;
        border: 3px solid;
        border-color: #9b7e41;
        padding: 12px;
        box-shadow: 0 0 10px 0 #9b7e41;
    }

    .card img{
        height: 150px;
        object-fit: contain;
    }

    .card2{
        width: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        border-radius: 25px;
        height: 200px;
        border: 3px solid rgba(0,0,0,0);
    }

    .deleting{
        width: 100%;
    }

}
@media screen and (max-width: 650px) {
    .flex-row{
        flex-direction: column;
    }
    .card2{
        height: 400px;

    }

    .media-text{
        text-align: center;
    }
}
</style>