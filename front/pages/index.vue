<template>
    <div class="flex flex-row justify-evenly">
        <select name="" id="" class="selector border-shine" @change="filtering()">
            <option value="-1" class="selector">Все</option>
            <option value="0" class="selector">Первое бытие</option>
            <option value="1" class="selector">Второе житие</option>
        </select>
        <select name="" id="" class="selector border-shine" @change="filtering()">
            <option value="-1" class="selector">Все</option>
            <option value="0" class="selector">Стартер</option>
            <option value="1" class="selector">Эндгейм</option>
        </select>
        <select name="" id="" class="selector border-shine" @change="filtering()">
            <option value="-1" class="selector">Все</option>
            <option value="0" class="selector">Боссинг</option>
            <option value="1" class="selector">Маппинг</option>
        </select>
    </div>
    <div class="container character_selector mt-8" style="min-height: 8vw;">
        <div class="wrapper flex flex-row relative justify-between">
            <button class="icon char_icon1 flex flex-col-reverse border-shine" v-for="i in 8" @click="() => {
                icon_click = i
                filtering(i)
            }"
                @mouseenter="icon_hover = i" @mouseleave="icon_hover = 0">
                <img :src="`../img/classes/${classes[i - 1]}/Small.png`" alt="" class="icon-image">
                <p v-if="icon_hover == i || icon_click == i" class="icon-text font">{{ classes_ru[i - 1] }}</p>
            </button>
        </div>
    </div>
    <div class="container mt-4">
        <div class="card-column px-4" style="display: flex; flex-direction: column;">
            <div class="card-block w-100 px-5"
                style="display: flex; flex-direction: row; justify-content: space-between;">
                <p class="text-xl font text-center">Лига</p>
                <p class="text-xl font text-center">Название</p>
                <p class="text-xl font text-center">Уровень</p>
                <p class="text-xl font text-center">Класс</p>
                <p class="text-xl font text-center">Эфф. здоровье</p>
                <p class="text-xl font text-center">Урон в секунду</p>
                <p class="text-xl font text-center">Автор</p>
        </div>
            <BuildCardBig v-for="i in decoded.length" 
                :league="decoded[i-1].name[0].top_inputs.cycle" 
                :build_class="classes[+decoded[i-1].class_id-1]" 
                :build_class_name="decoded[i-1].name[0].top_inputs.class" 
                :build_lvl="decoded[i-1].name[0].top_inputs.lvl"
                :build_name="decoded[i-1].build_name" 
                :build_ehp="Math.round(+decoded[i-1].name[0].stats.hp*(+decoded[i-1].name[0].stats.armour)/10*(1+ +decoded[i-1].name[0].stats.phys_res/100)*(1+ +decoded[i-1].name[0].stats.elem_res/100))" 
                :build_dps="(+decoded[i-1].name[0].stats.elem_damage+ +decoded[i-1].name[0].stats.phys_damage)*75" :id="i"
                :build_author="decoded[i-1].user.name" :more="more" :selected = "selected" :url="decoded[i-1].name[1]" class="border-shine" @click="() => {selected = i; if(selected == i){more = true}else{more=false}}"></BuildCardBig>
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
            classes: ['Bogatir', 'Antihrist', 'Bogolub', 'Medvesh', 'Pahan', 'Skomoroh', 'Yazich', 'Zastrel'],
            classes_ru: ['Богатырь', 'Антихрист',  'Боголюб', 'Налетчик', 'Богохульник', 'Скоморох', 'Язычница', 'Застрельщица'],
            cycles: ['Первое житие', 'Второе бытие'],
            types: ['Стартер', 'Эндгейм'],
            purposes: ['Маппинг', 'Боссинг'],
            filter: {
                cycle: '',
                type: '',
                purpose: '',
                class: ''
            },
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
            xdd: 0
        }
    },
    methods: {
        get_urls() {
            fetch('http://127.0.0.1:8000/urls', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
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
                        // console.log(encoded[i])
                        encoded[i][0] = JSON.parse(encoded[i][0])
                        this.decoded[i].name = encoded[i]
                    }
                    console.log(this.decoded)
                })
            return null
        },
        filtering(n){

                this.filter.cycle = document.getElementById('cycle').value


                this.filter.type = document.getElementById('type').value


                this.filter.purpose = document.getElementById('purpose').value

                this.filter.class = n
        }
    },
    beforeMount(){
        this.get_urls()
    },
    mounted(){
    }
}
</script>

<style>
.selector {
    border: 3px solid rgba(0, 0, 0, 0);
    border-radius: 25px;
}

.border-shine {
    border-radius: 15px !important;
}

.icon {
    display: flex;
    flex-direction: column;
    border: 3px solid;
    border-color: rgba(0, 0, 0, 0);
}

.icon-image {
    height: 114px;
    width: 114px;
    object-fit: cover;
    border-radius: 13px;
    z-index: 1;
}

.icon-text {
    width: 100%;
    background-color: rgb(0, 0, 0);
    border-bottom-left-radius: 13px;
    border-bottom-right-radius: 13px;
    z-index: 10;
    text-align: center;
    color: #ffffff !important;
}
</style>