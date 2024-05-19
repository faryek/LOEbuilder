<template>
    <div class="login-form container">
        <div class="login-row">
            <p class="font text-2xl">Логин</p>
            <input type="text" class="font pl-1 text-2xl">
        </div>
        <div class="login-row">
            <p class="font text-2xl">Пароль</p>
            <input type="text" class="font pl-1 text-2xl">
        </div>
        <button style="border: 2px solid white; color: white;">Войти</button>
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
    gap: 4vh;
    width: 30%;
    height: 40%;
}

.login-row {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
}

.login-row input {
    color: black !important;
    width: 50%;
    height: fit-content;
}

.login-row p {
    white-space: nowrap;
}
</style>