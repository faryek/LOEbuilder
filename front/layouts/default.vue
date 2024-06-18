<template>
    <div class="login-background" style="position: fixed; top: 0; left: 0; z-index: 500;"
        @click="() => { log = false; reg = false; back = false }" v-if="back"></div>
    <LoginCard style="position: fixed; top: 25%; left: 35%; z-index: 501;" v-if="log" @regActive="()=>{
        log = false
        reg = true
    }" 
    @loggining="()=>{
        logined = true
        log = false
        back = false
    }"></LoginCard>
    <RegistrationCard style="position: fixed; top: 20%; left: 30%; z-index: 501;" v-if="reg" @regged="()=>{
        reg = false
        back = false
    }"></RegistrationCard>
    <div class="main">
        <div>
            <header class="bg-black bg-opacity-80">
                <nav class="container mx-auto p-4 flex justify-between">
                    <ul class="flex gap-4">
                        <li class="flex flex-col justify-center">
                            <NuxtLink to="/" class="text-2xl fonted"><img :src="'img/icons/LoELogo.png'" alt="" style="max-width: 50px;"></NuxtLink>
                        </li>
                        <li class="flex flex-col justify-center">
                            <NuxtLink to="/" class="text-2xl fonted">Билды</NuxtLink>
                        </li>
                        <li class="flex flex-col justify-center">
                            <NuxtLink to="/build/" class="text-2xl fonted">Мои билды</NuxtLink>
                        </li>
                    </ul>
                    <div class="flex gap-4">
                        <button v-if="!logined" class="text-2xl fonted login" @click="() => { reg = true; back = true }">
                            Регистрация
                        </button>
                        <button v-if="!logined" class="text-2xl fonted login" @click="() => { log = true; back = true }">
                            Вход
                        </button>
                        <div ref="dropdown" class="dropdown">
                            <button v-if="logined" class="text-2xl fonted login dropdown-label p-2" @click="show = true">
                                {{ username }}
                            </button>
                            <div v-if="show" class="flex flex-col justify-start absolute bg-black bg-opacity-80 p-2" @mouseleave="show = false">
                                <button v-if="logined" class="text-2xl fonted login dropdown-label text-left">{{email}}</button>
                                <button v-if="logined" class="text-2xl fonted login dropdown-label text-left"@click="() => {
                                    logined = false
                                    remove_token()
                                }">Выйти</button>
                            </div>
                        </div>
                    </div>
                </nav>
            </header>
        </div>
        <div style="flex: 1;">
            <div class="backgroundimage"></div>
            <div class="background"></div>
            <div class="container mx-auto p-4">
                <slot></slot>
            </div>
        </div>
        <div>
            <footer class="mt-10" style="background-color: rgba(0, 0, 0, 0.623);">
                <nav class="container mx-auto p-4 w-screen mt-10">
                    <ul class="flex justify-around">
                        <li style="width: 200px;text-align: center;">
                            <div class="flex flex-col justify-center" style="height: 100%;">
                                <NuxtLink to="/about" class="text-2xl fonted">О нас</NuxtLink>
                            </div>
                        </li>
                        <li style="width: 200px;text-align: center;">
                            <p class="text-2xl fonted-footer mb-2">Контакты</p>
                            <div class="contact-row flex flex-row justify-center gap-3 mb-2">
                                <img :src="'img/icons/phone.png'" alt="">
                                <p class="text-xl fonted-footer footer-min-text" style="min-width: 175px;">8 (3435) 23-09-09</p>
                            </div>
                            <div class="contact-row email flex flex-row justify-center gap-3 mb-2">
                                <img :src="'img/icons/email.png'" alt="">
                                <p class="text-xl fonted-footer footer-min-text">nti@urfu.ru</p>
                            </div>
                        </li>
                        <li style="width: 200px;text-align: center;">
                            <p class="text-2xl fonted-footer mb-2">Товары</p>
                            <div class="contact-row flex flex-row justify-center gap-3 mb-2">
                                <img :src="'img/icons/epic-games-100.png'" alt="">
                                <a href="https://store.epicgames.com/ru/" class="text-xl fonted-footer footer-min-text" style="min-width: 175px;">Epic Games Store</a>
                            </div>
                            <div class="contact-row flex flex-row justify-center gap-3 mb-2">
                                <img :src="'img/icons/steam-100.png'" alt="">
                                <a href="https://store.steampowered.com/?l=russian" class="text-xl fonted-footer footer-min-text">Steam</a>
                            </div>
                        </li>
                    </ul>
                </nav>
                <div class="flex flex-row justify-center" style="width: 100%;">
                    <NuxtLink to="/"><img :src="'img/icons/LoELogo.png'" alt="" style="max-width: 100px;"></NuxtLink>
                </div>
                <nav class="container mx-auto p-4 my-10">
                    <ul class="flex justify-center gap-5">
                        <li>
                            <a href="https://discord.com/"><img src="/assets/img/icons/dis_png_1.png" alt=""></a>
                        </li>
                        <li>
                            <a href="https://vk.com/feed"><img src="/assets/img/icons/vk_png_1.png" alt=""></a>
                        </li>
                        <li>
                            <a href="https://www.youtube.com/"><img src="/assets/img/icons/yotube_png_1.png" alt=""></a>
                        </li>
                    </ul>
                </nav>
            </footer>
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
    data() {
        return {
            log: false,
            reg: false,
            back: false,
            logined: false,
            username: '',
            email: '',
        }
    },
    methods:{
        get_username(token) {
            fetch('http://127.0.0.1:8000/user_name', {
                method: 'GET',
                headers: {
                    Authorization: `Bearer ${token}`,
                }
            }).then(response => response.json())
                .then(json => {
                    if (json.detail) {
                        this.logined = false
                        return null
                    }
                    else{
                        this.logined= true
                        this.username = json.username
                        this.email = json.email
                    }
                })
            return null
        },
        remove_token(){
            localStorage.setItem('token','')
            location.reload()
        },

    },
    beforeMount(){
        let token = localStorage.getItem('token')
        this.get_username(token)
    }
}
</script>
<style>
.login-background {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.623);
}

.fonted-footer {
    font-family: 'TLheader-Regular';
    color: white;
}

.contact-row img{
    width: 30px;
}



.footer-min-text{
    color: gray;
}

body {
    min-height: 100vh;
    margin: 0;

    display: flex;
    flex-direction: column;
}

.main {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}


footer {
    bottom: 0;
    position: sticky;
    height: auto;
}

.background {
    position: fixed;
    z-index: -2;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: black;
    background-size: auto;
}

.backgroundimage {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: -1;
    top: 0;
    background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.301), rgb(0, 0, 0)), url('/assets/img/kandinsky-download-1710434177611-transformed.png');
    background-repeat: no-repeat;
}


.router-link-exact-active {
    color: #C68200;
}

.login {
    color: white;
}

html {
    overflow-y: scroll;
}

::-webkit-scrollbar {
    width: 10px;
    background-color: black;
}

::-webkit-scrollbar-thumb {
    background: #9b7e41;
    border-radius: 10px;
}
</style>