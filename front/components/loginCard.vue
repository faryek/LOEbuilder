<template>
    <div class="login-form">
        <div class="login-row">
            <p class="font">Логин</p>
            <input type="text" class="font pl-1" v-model="login">
        </div>
        <div class="login-row">
            <p class="font">Пароль</p>
            <input type="text" class="font pl-1" v-model="pwd">
        </div>
        <button style="border: 2px solid white; color: white;" @click="() => {
            get_token()
        }">Войти</button>
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