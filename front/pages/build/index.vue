<template>
    <AuthError v-if="!authorized && error"></AuthError>
    <CommonError v-if="error && authorized"></CommonError>
    <div v-if="authorized && !error">
            <div class="flex flex-row justify-evenly">
                <select name="" id="cycle" class="selector border-shine text-2xl" @change="filtering()">
                    <option value="-1" class="selector text-2xl">Все</option>
                    <option value="0" class="selector text-2xl">Первое бытие</option>
                    <option value="1" class="selector text-2xl">Второе житие</option>
                </select>
                <select name="" id="type" class="selector border-shine text-2xl" @change="filtering()">
                    <option value="-1" class="selector text-2xl">Все</option>
                    <option value="0" class="selector text-2xl">Стартер</option>
                    <option value="1" class="selector text-2xl">Эндгейм</option>
                </select>
                <select name="" id="purpose" class="selector border-shine text-2xl" @change="filtering()">
                    <option value="-1" class="selector text-2xl">Все</option>
                    <option value="0" class="selector text-2xl">Боссинг</option>
                    <option value="1" class="selector text-2xl">Маппинг</option>
                </select>
            </div>
            <div class="container character_selector mt-8" style="min-height: 8vw;">
                <div class="wrapper flex flex-row relative justify-between">
                    <button class="icon flex flex-col-reverse border-shine" v-for="i in 8" @click="() => {
                        if (icon_click == 0){
                            icon_click = i
                        }
                        else if (icon_click == i){
                            icon_click = 9
                        }
                        else {
                            icon_click = i
                        }
                        filtering()
                    }"
                        @mouseenter="icon_hover = i" @mouseleave="icon_hover = 0">
                        <img :src="`../img/classes/${classes[i - 1]}/Small.png`" alt="" class="icon-image">
                        <p v-if="icon_hover == i || icon_click == i" class="icon-text font">{{ classes_ru[i - 1] }}</p>
                    </button>
                </div>
            </div>
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
            more: false,
            selected: 0,
            icon_hover: 0,
            icon_click: 0,
            cycles: ['Первое бытие', 'Второе житие'],
            types: ['Стартер', 'Эндгейм'],
            purposes: ['Маппинг', 'Боссинг'],
            filter: {
                "cycle": "",
                "type": "",
                "purpose": "",
                "class_id": 0
            },
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
        filtering(){
            if (document.getElementById('cycle').value != -1)
            {
                this.filter.cycle = this.cycles[document.getElementById('cycle').value]
            } else {
                this.filter.cycle = ''
            }
            if (document.getElementById('type').value != -1){
                this.filter.type = this.types[document.getElementById('type').value]
            } else {
                this.filter.type = ''
            }
            if (document.getElementById('purpose').value != -1){
                this.filter.purpose = this.purposes[document.getElementById('purpose').value]
            } else {
                this.filter.purpose = ''
            }
            this.filter.class_id = this.icon_click
            let token = localStorage.getItem('token')
            if (token) {
                this.authorized = true
            }
            console.log(this.filter)
            this.get_urls_filtered(token)
        },
        get_urls_filtered(token) {
            fetch('http://127.0.0.1:8000/urls_user_da', {
                method: 'POST',
                headers: {
                    Authorization: `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.filter)
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
                        // console.log(encoded[i])
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
