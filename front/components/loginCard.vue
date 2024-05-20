<template>
    <div class="login-form container py-10 px-10">
        <p class="font text-4xl">Авторизация</p>
        <div class="login-row">
            <p class="font">Логин</p>
            <input type="text" class="font pl-1" v-model="login">
        </div>
        <div class="login-row">
            <p class="font">Пароль</p>
            <input type="text" class="font pl-1" v-model="pwd">
        </div>
        <div class="flex flex-col align-middle justify-center gap-2">
            <button class="login-btn mt-5 text-2xl font py-1 px-5">Войти</button>
            <button class="login-btn text-xl font py-1 px-5">Регистрация</button>
            <NuxtLink to="/support" class="font text-lg text-center">Забыли пароль?</NuxtLink>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            login: '',
            pwd: '',
        }
    },
    methods: {
        async get_token() {
            let credetentials = {
                name: this.login,
                pwd: this.pwd
            }
            fetch('http://127.0.0.1:8000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(credetentials)
            })
                .then(response => response.json())
                .then(json=>{
                    localStorage.setItem('token',json.token)
                });
        }
    },
}
</script>

<style>
.login-form {
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

.login-row {
    display: flex;
    flex-direction: row;
    gap: 1vw;
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