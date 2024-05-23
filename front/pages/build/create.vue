<template>
    <AuthError v-if="!authorized && error"></AuthError>
    <CommonError v-if="error && authorized"></CommonError>
    <div v-if="authorized && !error" class="container flex flex-col">
        <div class="top border-shine-create flex flex-row px-10 py-10 gap-10 justify-evenly">
            <img :src="`../img/classes/${classes_en[choose_class]}/Medium.png`" class="class-img" alt="">
            <div class="flex flex-col justify-evenly col">
                <select class="selector selector-create border-shine" name="" id="">
                    <option value="1" class="selector selector-create">Первое бытие</option>
                    <option value="2" class="selector selector-create">Второе житие</option>
                </select>
                <select name="" id="class" class="selector selector-create border-shine" @change="()=>{
                    get_class()
                    }">
                    <option v-for="i in classes.length" :value="i - 1" class="selector selector-create">{{
                        classes[i-1].name }}</option>
                </select>
                <div class="flex flex-row gap-5">
                    <p class="font font-create">Уровень:</p>
                    <input type="text" class="font font-create input-field px-4 selector selector-create border-shine"
                        placeholder="100">
                </div>
            </div>
            <div class="flex flex-col justify-evenly col">
                <input type="text" class="font font-create input-field px-4 selector selector-create border-shine"
                    placeholder="Фулл понос">
                <select name="" id="" class="selector selector-create border-shine">
                    <option value="" class="selector selector-create">Стартер</option>
                    <option value="" class="selector selector-create">Эндгейм</option>
                </select>
                <select name="" id="" class="selector selector-create border-shine">
                    <option value="" class="selector selector-create">Маппинг</option>
                    <option value="" class="selector selector-create">Боссинг</option>
                </select>
            </div>
        </div>
        <div class="mid flex flex-row justify-between mt-5 gap-10">
            <div class="border-shine-create p-10" style="width: 30%;">
                <div class="item-col flex flex-col gap-2">
                    <div class="item-row flex flex-row justify-center gap-2">
                        <div class="slot">
                            <img class="item-img border-shine w-14" src="public/img/items/neck_0.png" alt=""
                                style="opacity: 0;">
                        </div>
                        <div class="slot" @click="choose_item = 1">
                            <img class="item-img border-shine w-24" :src="`../img/items/head_${equiped.head}.png`"
                                alt="">
                        </div>
                        <div class="slot" @click="choose_item = 2">
                            <img class="item-img border-shine w-14" :src="`../img/items/neck_${equiped.neck}.png`"
                                alt="">
                        </div>

                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="slot" @click="choose_item = 3">
                            <img class="item-img border-shine w-24"
                                :src="`../img/items/main_hand_${equiped.left_hand}.png`" alt="">
                        </div>

                        <div class="slot" @click="choose_item = 4">
                            <img class="item-img border-shine w-36" :src="`../img/items/body_${equiped.body}.png`"
                                alt="">
                        </div>

                        <div class="slot" @click="choose_item = 5">
                            <img class="item-img border-shine w-24"
                                :src="`../img/items/off_hand_${equiped.right_hand}.png`" alt="">
                        </div>

                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="slot" @click="choose_item = 6">
                            <img class="item-img border-shine w-14" :src="`../img/items/ring_${equiped.left_ring}.png`"
                                alt="">
                        </div>

                        <div class="slot" @click="choose_item = 7">
                            <img class="item-img border-shine w-36" :src="`../img/items/belt_${equiped.belt}.png`"
                                alt="">
                        </div>

                        <div class="slot" @click="choose_item = 8">
                            <img class="item-img border-shine w-14" :src="`../img/items/ring_${equiped.right_ring}.png`"
                                alt="">
                        </div>

                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="slot" @click="choose_item = 9">
                            <img class="item-img border-shine w-24" :src="`../img/items/gloves_${equiped.gloves}.png`"
                                alt="">
                        </div>

                        <div class="slot" @click="choose_item = 10">
                            <img class="item-img border-shine w-24" :src="`../img/items/boots_${equiped.boots}.png`"
                                alt="">
                        </div>

                        <div class="slot" @click="choose_item = 11">
                            <img class="item-img border-shine w-24" :src="`../img/items/relic_${equiped.relic}.png`"
                                alt="">
                        </div>

                    </div>
                </div>
            </div>
            <div class="border-shine-create p-10" style="width: 40%;">
                <div v-for="i in 11" v-show="choose_item == i && show_item == 0" class="container flex flex-wrap p-10">
                    <!-- <img v-for="j in slots.length" :src="slots[i][j].image" alt=""> -->
                </div>
                <div v-for="i in 11" v-show="show_item == i && choose_item == 0" class="container flex flex-wrap p-10">
                    <p class="text-2xl font">Шмотка {{ i }}</p>
                </div>
            </div>
            <div class="border-shine-create p-10" style="width: 30%;">
                <div class="flex flex-col justify-evenly" style="height: 100%;">
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="text-xl font">Аттрибуты</p>
                        <div class="flex flex-row">
                            <p class="text-xl font" style="color: red;">{{ classes[choose_class].base_atrs.split(', ')[0] }}</p>
                            <p style="color: white;">/</p>
                            <p class="text-xl font" style="color: green;">{{ classes[choose_class].base_atrs.split(', ')[1] }}</p>
                            <p style="color: white;">/</p>
                            <p class="text-xl font" style="color: blue;">{{ classes[choose_class].base_atrs.split(', ')[2 ] }}</p>
                        </div>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Здоровье</p>
                        <p class="stat-value text-xl font">{{ classes[choose_class].base_hp }}</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Мана</p>
                        <p class="stat-value text-xl font">{{ classes[choose_class].base_mp }}</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Броня</p>
                        <p class="stat-value text-xl font">{{ classes[choose_class].base_armor }}</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Сопр. физ.урону</p>
                        <p class="stat-value text-xl font">{{ classes[choose_class].base_phys_res }}</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Сопр. элем.урону</p>
                        <p class="stat-value text-xl font">{{ classes[choose_class].base_ele_res }}</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Шанс крит.удара</p>
                        <p class="stat-value text-xl font">{{crit_chance}}%</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Крит. урон</p>
                        <p class="stat-value text-xl font">{{crit_damage}}%</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Вампиризм</p>
                        <p class="stat-value text-xl font">{{vampirism}}%</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Шанс уклонения</p>
                        <p class="stat-value text-xl font">{{ classes[choose_class].base_evade }}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="bot border-shine-create flex flex-row justify-between mt-5 gap-10" style="height: 50rem;"></div>
    </div>

</template>

<script>
export default {
    data() {
        return {
            weapons: [],
            armour: [],
            accessories: [],
            affixes: [],
            passives: [],
            heads:[],
            necks: [],
            bodies: [],
            gloves: [],
            boots: [],
            relics:[],
            left_hands: [],
            right_hands: [],
            belts:[],
            rings: [],
            classes: [{ "id": 1, "name": "Богатырь", "main_atr": "Сила", "base_atrs": "60, 20, 20", "base_hp": 1000, "base_mp": 50, "base_armor": 50, "base_evade": 10, "base_ele_res": 30, "base_phys_res": 50 }],
            classes_en: ['Bogatir', 'Antihrist', 'Bogolub', 'Medvesh', 'Pahan', 'Skomoroh', 'Yazich', 'Zastrel'],
            slots: [],
            error: false,
            authorized: false,
            equiped: {
                head: 0,
                neck: 0,
                left_hand: 0,
                body: 0,
                right_hand: 0,
                left_ring: 0,
                belt: 0,
                right_ring: 0,
                gloves: 0,
                boots: 0,
                relic: 0,
            },
            choose_item: 0,
            show_item: 0,
            choose_class: 0,
            crit_chance:0,
            crit_damage:0,
            vampirism: 0
        }
    },
    props: [],
    methods: {
        get_class() {
            this.choose_class = document.getElementById('class').value
        },
        get_weapons(token) {
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
                    for (let i = 0; i < json.length; i++) {
                        this.weapons.push(json[i])
                        if (json[i].sub_id.item_types[0].name == 'Второстепенное') {
                            this.right_hands.push(json[i])
                        }
                        else {
                            this.left_hands.push(json[i])
                        }
                    }
                })
            return null
        },
        get_armour(token) {
            fetch('http://127.0.0.1:8000/armour', {
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
                    for (let i = 0; i < json.length; i++) {
                        this.armour.push(json[i])
                        if (json[i].sub_id.name == 'Шлем') {
                            this.heads.push(json[i])
                        }
                        else if (json[i].sub_id.name == 'Наручи') {
                            this.gloves.push(json[i])
                        }
                        else if (json[i].sub_id.name == 'Ремень') {
                            this.belts.push(json[i])
                        }
                        else if (json[i].sub_id.name == 'Нагрудник') {
                            this.bodies.push(json[i])
                        }
                        else if (json[i].sub_id.name == 'Ботинки') {
                            this.bodies.push(json[i])
                        }
                    }
                })
            return null
        },
        get_accessories(token) {
            fetch('http://127.0.0.1:8000/accessory', {
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
                    for (let i = 0; i < json.length; i++) {
                        this.accessories.push(json[i])
                        if (json[i].sub_id.name == 'Ожерелье') {
                            this.necks.push(json[i])
                        }
                        else if (json[i].sub_id.name == 'Кольцо') {
                            this.rings.push(json[i])
                        }
                        else if (json[i].sub_id.name == 'Реликвия') {
                            this.relics.push(json[i])
                        }
                    }
                })
            return null
        },
        get_affixes(token) {
            fetch('http://127.0.0.1:8000/affixes', {
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
                    for (let i = 0; i < json.length; i++) {
                        this.affixes.push(json[i])
                    }
                })
            return null
        },
        get_passives(token) {
            fetch('http://127.0.0.1:8000/passives', {
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
                    for (let i = 0; i < json.length; i++) {
                        this.passives.push(json[i])
                    }
                })
            return null
        },
        get_classes(token) {
            fetch('http://127.0.0.1:8000/classes', {
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
                    for (let i = 1; i < json.length; i++) {
                        this.classes.push(json[i])
                    }
                })
            return null
        },
        auth_check(token){
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
    beforeMount() {
        let token = localStorage.getItem('token')
        if (token) {
            this.authorized = true
        }
        this.get_weapons(token)
        this.get_armour(token)
        this.get_accessories(token)
        this.get_affixes(token)
        this.get_passives(token)
        this.get_classes(token)
    },
    mounted() {
        this.slots.push(this.heads, this.necks, this.left_hands, this.bodies, this.right_hands, this.rings, this.belts, this.rings, this.gloves, this.boots, this.relics)
        console.log(this.slots)
    },
    updated() {
        let token = localStorage.getItem('token')
        if (token) {
            this.authorized = true
        }
        this.get_weapons(token)
    },
}
</script>

<style>
.stat-row p {
    width: 100%;
}

.stat-value {
    text-align: end;
}

.selector-create {
    border: 3px solid rgba(0, 0, 0, 0);
    border-radius: 25px;
    font-size: 2.25rem
        /* 36px */
    ;
    line-height: 2.5rem
        /* 40px */
    ;
}

.slot:hover {
    cursor: pointer;
}

.item-img {
    border-radius: 15px !important;
    border: 3px solid;
    border-color: #9b7f4100 !important;
    object-fit: cover;
}

.top {
    background-color: rgba(0, 0, 0, 0.103);
}

.col {
    width: 40%;
}

.border-shine-create {
    border-radius: 15px !important;
    border: 3px solid;
    border-color: #9b7e41 !important;
    box-shadow: 0 0 20px 0 #9b7e41;
}

.font-create {
    color: white;
    font-size: 2.25rem
        /* 36px */
    ;
}

.class-img {
    border: 3px solid;
    border-color: rgba(0, 0, 0, 0);
    object-fit: cover;
    border-radius: 13px;
}

.input-field {
    width: 100%;
    text-align: start;
}
</style>