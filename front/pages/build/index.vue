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
            <BuildCard v-for="i in decoded.length" 
            :league="decoded[i-1].name[0].top_inputs.cycle" 
            :build_class="classes[+decoded[i-1].class_id-1]" 
            :build_class_name="decoded[i-1].name[0].top_inputs.class" 
            :build_lvl="decoded[i-1].name[0].top_inputs.lvl"
            :build_name="decoded[i-1].build_name"
            :url="decoded[i-1].name[1]"
            ></BuildCard>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            error: false,
            authorized: false,
            classes: ['Bogatir', 'Antihrist', 'Bogolub', 'Medvesh', 'Pahan', 'Skomoroh', 'Yazich', 'Zastrel'],
            classes_ru: ['Богатырь', 'Антихрист',  'Боголюб', 'Налетчик', 'Богохульник', 'Скоморох', 'Язычница', 'Застрельщица'],
            decoded:[
                {
                    build_name: 'хуй',
                    class_id: 1,
                    name: [
                        {
                            stats: {
                                armour: 0,
                                elem_damage: 0,
                                elem_res: 0,
                                phys_damage: 0,
                                phys_res: 0,
                                hp: 0,
                            },
                            top_inputs: {
                                class: 'Танцовщица',
                                cycle: 'her',
                                lvl: '1',
                                name: 'hui',
                                purpose: 'sosat',
                                type: 'zalupa'
                            }
                        },
                        '123'
                    ],
                    user: {
                        name: 'down'
                    }
                },
                {
                    build_name: 'хуй',
                    class_id: 1,
                    name: [
                        {
                            stats: {
                                armour: 0,
                                elem_damage: 0,
                                elem_res: 0,
                                phys_damage: 0,
                                phys_res: 0,
                                hp: 0,
                            },
                            top_inputs: {
                                class: 'Танцовщица',
                                cycle: 'her',
                                lvl: '1',
                                name: 'hui',
                                purpose: 'sosat',
                                type: 'zalupa'
                            }
                        },
                        '123'
                    ],
                    user: {
                        name: 'down'
                    }
                },
            ],
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
        get_urls(token) {
            fetch('http://127.0.0.1:8000/urls_user', {
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
                    this.decoded = json
                    let encoded = []
                    for(let i = 0;i < json.length;i++){
                        json[i].name = json[i].name.split('HereWeAre')
                        encoded.push(json[i].name)
                        encoded[i][0] = JSON.parse(encoded[i][0])
                        this.decoded[i].name = encoded[i]
                    }
                    console.log(this.decoded)
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
        this.get_urls(token)
    }
}

</script>

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
