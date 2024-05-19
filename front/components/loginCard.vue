<template>
    <div class="login-form container py-10 px-10">
        <p class="font text-4xl">Авторизация</p>
        <div class="login-row">
            <p class="font text-2xl">Логин</p>
            <input type="text" class="font pl-1 text-2xl">
        </div>
        <div class="login-row">
            <p class="font text-2xl">Пароль</p>
            <input type="text" class="font pl-1 text-2xl">
        </div>
        <div class="flex flex-col align-middle justify-center gap-2">
            <button class="login-btn mt-5 text-2xl font py-1 px-5">Войти</button>
            <button class="login-btn text-xl font py-1 px-5">Регистрация</button>
            <NuxtLink to="/support" class="font text-lg text-center">Забыли пароль?</NuxtLink>
        </div>
    </div>
</template>

<script>

</script>

<style>
.login-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 4vh;
    width: 30%;
    background-color: black;
    border: 3px solid;
    border-radius: 25px;
    border-color: #9b7e41 !important;
    box-shadow: 0 0 20px 0 #9b7e41;
}

.login-row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
}

.login-row input {
    color: white !important;
    background-color: rgb(51, 51, 51);
    width: 50%;
    height: fit-content;
    border: 3px solid;
    border-radius: 25px;
    border-color: #9b7e41 !important;
    box-shadow: 0 0 20px 0 #9b7e41;
}

.login-row p {
    white-space: nowrap;
}

.login-btn {
    border: 3px solid;
    border-radius: 25px;
    border-color: #9b7e41 !important;
    box-shadow: 0 0 20px 0 #9b7e41;
}
</style>