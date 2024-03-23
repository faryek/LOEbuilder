<template>
    <div>
        <header class="shadow-sm bg-black">
            <nav class="container mx-auto p-4 flex justify-between">
                <ul class="flex gap-4">
                    <li>
                        <NuxtLink to="/" class="text-2xl fonted">Билды</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink to="/" class="text-2xl fonted">Создать билд</NuxtLink>
                    </li>
                    <li>
                        <NuxtLink to="/" class="text-2xl fonted">Руководство</NuxtLink>
                    </li>
                </ul>
                <NuxtLink to="/" class="font-bold text-2xl fonted">Вход</NuxtLink>
            </nav>
        </header>
    </div>
    <div class="container mx-auto p-4">
        <slot></slot>
    </div>
</template>

<style>
    .fonted{
        font-family: 'TLheader-Regular';
    }
    .router-link-exact-active {
        color: white;
    }
</style>