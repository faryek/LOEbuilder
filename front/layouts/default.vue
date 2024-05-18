<template>
    <div class="login-background" style="position: fixed; top: 0; left: 0; z-index: 500;" @click="() => { click = false}" v-if="click"></div>
    <LoginCard style="position: fixed; top: 25%; left: 35%; z-index: 501;" v-if="click"></LoginCard>
    <div class="main">
        <div>
            <header class="bg-black bg-opacity-80">
                <nav class="container mx-auto p-4 flex justify-between">
                    <ul class="flex gap-4">
                        <li>
                            <NuxtLink to="/" class="text-2xl fonted">Билды</NuxtLink>
                        </li>
                        <li>
                            <NuxtLink to="/build/" class="text-2xl fonted">Мои билды</NuxtLink>
                        </li>
                        <li>
                            <NuxtLink to="/guide" class="text-2xl fonted">Руководство</NuxtLink>
                        </li>
                    </ul>
                    <button class="text-2xl fonted login"
                        @click="() => { click = true}">Вход</button>
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
            <footer class="mt-10">
                <nav class="container mx-auto p-4 w-screen mt-10">
                    <ul class="flex justify-around">
                        <li>
                            <NuxtLink to="/about" class="text-2xl fonted">О нас</NuxtLink>
                        </li>
                        <li>
                            <NuxtLink to="/contacts" class="text-2xl fonted">Контакты</NuxtLink>
                        </li>
                        <li>
                            <NuxtLink to="/support" class="text-2xl fonted">Поддержать нас</NuxtLink>
                        </li>
                    </ul>
                </nav>
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
<script>
export default {
    data() {
        return {
            click: false
        }
    }
}
</script>
<style>
.login-background {
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.623);
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