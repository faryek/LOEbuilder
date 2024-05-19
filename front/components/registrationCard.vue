<template>
    <div class="reg-form container py-10 px-10">
        <p class="font text-4xl">Регистрация</p>
        <div class="reg-row">
            <p class="font text-2xl">Логин</p>
            <input type="text" class="font pl-1 text-2xl">
        </div>
        <div class="reg-row">
            <p class="font text-2xl">Эл. почта</p>
            <input type="text" class="font pl-1 text-2xl">
        </div>
        <div class="reg-row">
            <p class="font text-2xl">Пароль</p>
            <input type="text" class="font pl-1 text-2xl">
        </div>
        <div class="reg-row">
            <p class="font text-2xl">Подтвердите пароль</p>
            <input type="text" class="font pl-1 text-2xl">
        </div>
        <button class="reg-btn text-2xl font py-1 px-6 mt-5"
            style="border: 2px solid white; color: white;">Регистрация</button>
    </div>
</template>

<script>

</script>

<style>
.reg-form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 4vh;
    width: 40%;
    background-color: black;
    border: 3px solid;
    border-radius: 25px;
    border-color: #9b7e41 !important;
    box-shadow: 0 0 20px 0 #9b7e41;
}

.reg-row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
}

.reg-row input {
    color: white !important;
    background-color: rgb(51, 51, 51);
    width: 50%;
    height: fit-content;
    border: 3px solid;
    border-radius: 25px;
    border-color: #9b7e41 !important;
    box-shadow: 0 0 20px 0 #9b7e41;
}

.reg-row p {
    white-space: nowrap;
}

.reg-btn {
    border: 3px solid;
    border-radius: 25px;
    border-color: #9b7e41 !important;
    box-shadow: 0 0 20px 0 #9b7e41;
}
</style>