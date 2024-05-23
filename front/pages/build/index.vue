<template>
    <AuthError v-if="!authorized && error"></AuthError>
    <CommonError v-if="error && authorized"></CommonError>
    <div v-if="authorized && !error">
        <div class="container flex flex-col items-center">
            <NuxtLink to="/build/create" class="create-build-btn border-shine flex justify-center items-center">
                <p class="text-2xl w-max">Создать новый билд!</p>
            </NuxtLink>
        </div>
        <div class="container flex flex-row flex-wrap justify-between gap-y-10">
            <BuildCard v-for="i in 7" :league="'Первое бытие'" :build_class="'Bogolub'" :build_lvl="100"
                :build_name="'test_name'" :build_class_name="'Боголюб'" :id="i"></BuildCard>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            error: false,
            authorized: false,
        }
    },
    methods: {
        auth_check(token) {
            fetch('http://127.0.0.1:8000/weapons', {
                method: 'GET',
                headers: {
                    Authorization: `Bearer ${token}`,
                }
            }).then(response => response.json())
                .then(json => {
                    if (json.detail) {
                        this.error = true
                        return null
                    }
                })
            return null
        },
    },
    beforeMount(){
        let token = localStorage.getItem('token')
        if (token) {
            this.authorized = true
        }
        this.auth_check(token)
    }
}

</script>
export default {
data() {
return {
}
}
}
<style>
.create-build-btn {
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    border-radius: 25px;
    width: 50%;
    height: 50px;
    border: 3px;
    font-family: 'TLheader-Regular';
    margin-bottom: 35px;
    box-shadow: 0 0 10px 0 #9b7e41;
    text-align: center;
}
</style>
