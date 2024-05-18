<template>
    <div class="login-form">
        <div class="login-row">
            <p class="font">Логин</p>
            <input type="text" class="font pl-1">
        </div>
        <div class="login-row">
            <p class="font">Пароль</p>
            <input type="text" class="font pl-1">
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
    gap: 5vh;
    width: 30%;
    height: 40%;
}

.login-row {
    display: flex;
    flex-direction: row;
    gap: 1vw;
}

.login-row input {
    color: black !important;
}
</style>