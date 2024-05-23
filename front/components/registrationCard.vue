<template>
    <div class="reg-form container py-10 px-10">
        <p class="font text-4xl">Регистрация</p>
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
        <button class="reg-btn text-2xl font py-1 px-6 mt-5"
            style="border: 2px solid white; color: white;" @click="()=>{
                registrate_user()
            }">Регистрация</button>
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
            .then(json =>{
                if(json.detail == "User exists"){
                    this.user_exists = true
                }
                else if(json.detail){
                    this.error_reg = true
                    this.$emit('regged')
                }
            })
        },
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