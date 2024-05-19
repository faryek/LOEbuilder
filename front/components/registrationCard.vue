<template>
    <div class="reg-form container">
        <div class="reg-row">
            <p class="font text-2xl">Логин</p>
            <input type="text" class="font pl-1 text-2xl" v-model="login">
        </div>
        <div class="reg-row">
            <p class="font text-2xl">Эл. почта</p>
            <input type="text" class="font pl-1 text-2xl" v-model="email">
        </div>
        <div class="reg-row">
            <p class="font text-2xl">Пароль</p>
            <input type="text" class="font pl-1 text-2xl"v-model="pwd">
        </div>
        <div class="reg-row">
            <p class="font text-2xl">Подтвердите пароль</p>
            <input type="text" class="font pl-1 text-2xl"v-model="pwd_2">
        </div>
        <button @click="()=>{registrate_user()}" style="border: 2px solid white; color: white;">Войти</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            login: '',
            pwd: '',
            email:'',
            pwd_2:'',
            error_reg: false,
            user_exists: false,
        }
    },
    methods: {
        async registrate_user(){
            let credentials = {
                email:this.email,
                name:this.login,
                pwd:this.pwd,
                pwd_2:this.pwd_2,
            }
            fetch('http://127.0.0.1:8000/register',{
                method: 'POST',
                headers:{
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify(credentials)
            }).then(response => response.json())
            // .then(json =>{
            //     if(json.detail == "User exists"){
            //         this.user_exists = true
            //     }
            //     else if(json.detail){
            //         this.error_reg = true
            //     }
            // })
        },
        // async get_token() {
        //     let credetentials = {
        //         name: this.login,
        //         pwd: this.pwd
        //     }
        //     fetch('http://127.0.0.1:8000/login', {
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json'
        //         },
        //         body: JSON.stringify(credetentials)
        //     })
        //         .then(response => response.json())
        //         .then(json=>{
        //             localStorage.setItem('token',json.token)
        //         });
        // }
    },
}
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