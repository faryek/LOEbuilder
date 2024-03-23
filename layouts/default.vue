<template>
    <div>
        <div>
            <header class="bg-black bg-opacity-80">
                <nav class="container mx-auto p-4 flex justify-between">
                    <ul class="flex gap-4">
                        <li>
                            <NuxtLink to="/" class="text-2xl fonted">Билды</NuxtLink>
                        </li>
                        <li>
                            <NuxtLink to="/build/" class="text-2xl fonted">Создать билд</NuxtLink>
                        </li>
                        <li>
                            <NuxtLink to="/guide/" class="text-2xl fonted">Руководство</NuxtLink>
                        </li>
                    </ul>
                    <NuxtLink to="/" class="text-2xl fonted login">Вход</NuxtLink>
                </nav>
            </header>
        </div>
        <div class="background brightness-75 shadow-2xl"><img src="/assets/img/kandinsky-download-1710434177611-transformed.png" alt=""></div>
        <div class="container mx-auto p-4">
            <slot></slot>
        </div>
        <div>
            <footer>
            </footer>
        </div>
    </div>
</template>

<style>
@font-face {
    font-family: 'TLheader-Regular';
    src: url(/fonts/TLheader-Regular.ttf);
    font-weight: normal;
    font-style: normal;
    font-display: swap;
}

.background{
    width: 100%;
    position: absolute;
    z-index: -1;
    top: 0;
}

.fonted {
    font-family: 'TLheader-Regular';
    color: white;
}

.router-link-exact-active {
    color: #C68200;
}

.login{
    color: white;
}

.fonted:hover{
    color: #C68200;
}
</style>