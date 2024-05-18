<template>
    <div class="reg-form container">
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
    width: 30%;
    height: 40%;
}

.reg-row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
}

.reg-row input {
    color: black !important;
    width: 50%;
    height: fit-content;
}

.reg-row p {
    white-space: nowrap;
}
</style>