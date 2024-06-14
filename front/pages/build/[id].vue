<template>
    <BuildError v-if="error"></BuildError>
    <div v-if="!error">
        <div v-if="!error" class="container flex flex-col">
            <div class="top border-shine-create flex flex-col px-10 py-10 gap-10 justify-evenly">
                <div class="build-info flex flex-row justify-evenly gap-10">
                    <img :src="`../img/classes/${data_ids.top_inputs[6]}/Medium.png`" class="class-img" alt="">
                    <div class="build-info-sub flex flex-row justify-evenly gap-10">
                        <div class="flex flex-col justify-evenly col">
                            <p class="font font-create text-center">Цикл: {{data_ids.top_inputs[1]}}</p>
                            <p class="font font-create text-center">Класс: {{data_ids.top_inputs[0]}}</p>
                            <div class="flex flex-row gap-5 justify-center level-flex">
                                <p class="font font-create text-center">Уровень: </p>
                                <p class="font font-create text-center">{{data_ids.top_inputs[2]}}</p>
                            </div>
                            <p class="font font-create text-center link-text">Ссылка на билд</p>
                        </div>
                        <div class="flex flex-col justify-evenly col">
                            <p class="font font-create text-center build-name">Название: {{data_ids.top_inputs[3]}}</p>
                            <p class="font font-create text-center">Тип: {{data_ids.top_inputs[5]}}</p>
                            <p class="font font-create text-center">Назначение: {{data_ids.top_inputs[4]}}</p>
                            <input type="text" class="font font-create input-field px-4 selector selector-create border-shine" placeholder="" v-model="urlers">
                        </div>
                    </div>
                </div>
            </div>
            <div class="mid flex flex-row justify-center mt-5 gap-10">
                <div class="panel border-shine-create p-10" style="width: 30%;">
                    <div class="item-col flex flex-col gap-2">
                        <div class="item-row flex flex-row justify-center gap-2">
                        <div class="">
                            <img class="item-img border-shine w-14 slot" src="public/img/items/neck_0.png" alt=""
                                style="opacity: 0;">
                        </div>
                        <div class="">
                            <VTooltip>
                                <!-- HELMET -->
                                <img class="item-img w-24 slot" v-if="armour[data_ids.equiped_ids.head_id].id !=0" :src="armour[data_ids.equiped_ids.head_id].image" alt="">
                                <img class="item-img w-24 slot" v-if="armour[data_ids.equiped_ids.head_id].id ==0" src="public/img/items/head_0.png" alt="">
                                <template #popper v-if="armour[data_ids.equiped_ids.head_id].id != 0">
                                    <ItemTooltip 
                                    
                                                :name="armour[data_ids.equiped_ids.head_id].name" :image="armour[data_ids.equiped_ids.head_id].image" :sub_name="armour[data_ids.equiped_ids.head_id].sub_id.name"
                                                :implicits_value_start="armour[data_ids.equiped_ids.head_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="armour[data_ids.equiped_ids.head_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="armour[data_ids.equiped_ids.head_id].sub_id.item_implicits[0].effect">

                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>
                        <div class="">
                            <!-- NECKLACE -->
                            <VTooltip>
                                <img class="item-img w-14 slot" :src="accessories[data_ids.equiped_ids.neck_id].image" alt="">
                                <template #popper v-if="accessories[data_ids.equiped_ids.neck_id].id != 0">
                                    <ItemTooltip 
                                                :name="accessories[data_ids.equiped_ids.neck_id].name" :image="accessories[data_ids.equiped_ids.neck_id].image" :sub_name="accessories[data_ids.equiped_ids.neck_id].sub_id.name"
                                                :implicits_value_start="accessories[data_ids.equiped_ids.neck_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="accessories[data_ids.equiped_ids.neck_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="accessories[data_ids.equiped_ids.neck_id].sub_id.item_implicits[0].effect">

                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>
                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="">
                            <VTooltip>
                                <!-- LEFT_HAND_WPN -->
                                <img class="item-img w-24 slot" :src="weapons[data_ids.equiped_ids.left_hand_id].image" alt="">
                                <template #popper v-if="weapons[data_ids.equiped_ids.left_hand_id].id != 0">
                                    <ItemTooltip 
                                                :name="weapons[data_ids.equiped_ids.left_hand_id].name" :image="weapons[data_ids.equiped_ids.left_hand_id].image" :sub_name="weapons[data_ids.equiped_ids.left_hand_id].sub_id.name"
                                                :implicits_value_start="weapons[data_ids.equiped_ids.left_hand_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="weapons[data_ids.equiped_ids.left_hand_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="weapons[data_ids.equiped_ids.left_hand_id].sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- BODYARMOUR -->
                                <img class="item-img w-36 slot" :src="armour[data_ids.equiped_ids.body_id].image" alt="">
                                <template #popper v-if="armour[data_ids.equiped_ids.body_id].id != 0">
                                    <ItemTooltip 
                                                :name="armour[data_ids.equiped_ids.body_id].name" :image="armour[data_ids.equiped_ids.body_id].image" :sub_name="armour[data_ids.equiped_ids.body_id].sub_id.name"
                                                :implicits_value_start="armour[data_ids.equiped_ids.body_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="armour[data_ids.equiped_ids.body_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="armour[data_ids.equiped_ids.body_id].sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- RIGHT_HAND_WPN -->
                                <img class="item-img w-24 slot" :src="weapons[data_ids.equiped_ids.right_hand_id].image" alt="">
                                <template #popper v-if="weapons[data_ids.equiped_ids.right_hand_id].id != 0">
                                    <ItemTooltip 
                                                :name="weapons[data_ids.equiped_ids.right_hand_id].name" :image="weapons[data_ids.equiped_ids.right_hand_id].image" :sub_name="weapons[data_ids.equiped_ids.right_hand_id].sub_id.name"
                                                :implicits_value_start="weapons[data_ids.equiped_ids.right_hand_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="weapons[data_ids.equiped_ids.right_hand_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="weapons[data_ids.equiped_ids.right_hand_id].sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="">
                            <VTooltip>
                                <!-- LEFT_RING -->
                                <img class="item-img w-14 slot" :src="accessories[data_ids.equiped_ids.left_ring_id].image" alt="">
                                <template #popper v-if="accessories[data_ids.equiped_ids.left_ring_id].id != 0">
                                    <ItemTooltip 
                                                :name="accessories[data_ids.equiped_ids.left_ring_id].name" :image="accessories[data_ids.equiped_ids.left_ring_id].image" :sub_name="accessories[data_ids.equiped_ids.left_ring_id].sub_id.name"
                                                :implicits_value_start="accessories[data_ids.equiped_ids.left_ring_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="accessories[data_ids.equiped_ids.left_ring_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="accessories[data_ids.equiped_ids.left_ring_id].sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- BELT -->
                                <img class="item-img w-36 slot" :src="armour[data_ids.equiped_ids.belt_id].image" alt="">
                                <template #popper v-if="armour[data_ids.equiped_ids.belt_id].id != 0">
                                    <ItemTooltip 
                                                :name="armour[data_ids.equiped_ids.belt_id].name" :image="armour[data_ids.equiped_ids.belt_id].image" :sub_name="armour[data_ids.equiped_ids.belt_id].sub_id.name"
                                                :implicits_value_start="armour[data_ids.equiped_ids.belt_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="armour[data_ids.equiped_ids.belt_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="armour[data_ids.equiped_ids.belt_id].sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- RIGHT_RING -->
                                <img class="item-img w-14 slot" :src="accessories[data_ids.equiped_ids.right_ring_id].image" alt="">
                                <template #popper v-if="accessories[data_ids.equiped_ids.right_ring_id].id != 0">
                                    <ItemTooltip 
                                                :name="accessories[data_ids.equiped_ids.right_ring_id].name" :image="accessories[data_ids.equiped_ids.right_ring_id].image" :sub_name="accessories[data_ids.equiped_ids.right_ring_id].sub_id.name"
                                                :implicits_value_start="accessories[data_ids.equiped_ids.right_ring_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="accessories[data_ids.equiped_ids.right_ring_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="accessories[data_ids.equiped_ids.right_ring_id].sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="">
                            <VTooltip>
                                <!-- GLOVES -->
                                <img class="item-img w-24 slot" :src="armour[data_ids.equiped_ids.gloves_id].image" alt="">
                                <template #popper v-if="armour[data_ids.equiped_ids.gloves_id].id != 0">
                                    <ItemTooltip 
                                                :name="armour[data_ids.equiped_ids.gloves_id].name" :image="armour[data_ids.equiped_ids.gloves_id].image" :sub_name="armour[data_ids.equiped_ids.gloves_id].sub_id.name"
                                                :implicits_value_start="armour[data_ids.equiped_ids.gloves_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="armour[data_ids.equiped_ids.gloves_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="armour[data_ids.equiped_ids.gloves_id].sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- BOOTS -->
                                <img class="item-img w-24 slot" :src="armour[data_ids.equiped_ids.boots_id].image" alt="">
                                <template #popper v-if="armour[data_ids.equiped_ids.boots_id].id != 0">
                                    <ItemTooltip 
                                                :name="armour[data_ids.equiped_ids.boots_id].name" :image="armour[data_ids.equiped_ids.boots_id].image" :sub_name="armour[data_ids.equiped_ids.boots_id].sub_id.name"
                                                :implicits_value_start="armour[data_ids.equiped_ids.boots_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="armour[data_ids.equiped_ids.boots_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="armour[data_ids.equiped_ids.boots_id].sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- RELIC -->
                                <img class="item-img w-24 slot" :src="accessories[data_ids.equiped_ids.relic_id].image" alt="">
                                <template #popper v-if="accessories[data_ids.equiped_ids.relic_id].id != 0">
                                    <ItemTooltip 
                                                :name="accessories[data_ids.equiped_ids.relic_id].name" :image="accessories[data_ids.equiped_ids.relic_id].image" :sub_name="accessories[data_ids.equiped_ids.relic_id].sub_id.name"
                                                :implicits_value_start="accessories[data_ids.equiped_ids.relic_id].sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="accessories[data_ids.equiped_ids.relic_id].sub_id.item_implicits[0].value_end"
                                                :implicits_effect="accessories[data_ids.equiped_ids.relic_id].sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                    </div>
                    </div>
                </div>
                
                <div class="panel border-shine-create p-10" style="width: 30%;">
                    <div class="flex flex-col justify-evenly" style="height: 100%;">
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="text-xl stat-name font">Аттрибуты</p>
                            <div class="flex flex-row stat-value justify-end">
                                <p class="text-xl font" style="color: red;">{{ data_ids.stats.strength }}</p>
                                <p style="color: white;">/</p>
                                <p class="text-xl font" style="color: green;">{{ data_ids.stats.dexterity }}</p>
                                <p style="color: white;">/</p>
                                <p class="text-xl font" style="color: blue;">{{ data_ids.stats.intelligence }}</p>
                            </div>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Физ. урон</p>
                            <p class="stat-value text-xl font">{{data_ids.stats.phys_damage}}</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Элем. урон</p>
                            <p class="stat-value text-xl font">{{data_ids.stats.elem_damage}}</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Здоровье</p>
                            <p class="stat-value text-xl font">{{ data_ids.stats.hp}}</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Мана</p>
                            <p class="stat-value text-xl font">{{ data_ids.stats.mp }}</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Броня</p>
                            <p class="stat-value text-xl font">{{ data_ids.stats.armour }}</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Сопр. физ.урону</p>
                            <p class="stat-value text-xl font">{{ data_ids.stats.phys_res }}%</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Сопр. элем.урону</p>
                            <p class="stat-value text-xl font">{{ data_ids.stats.elem_res }}%</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Шанс крит.удара</p>
                            <p class="stat-value text-xl font">{{data_ids.stats.critical_chance}}%</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Крит. урон</p>
                            <p class="stat-value text-xl font">{{data_ids.stats.critical_damage}}%</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Вампиризм</p>
                            <p class="stat-value text-xl font">{{data_ids.stats.vamp}}%</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Шанс уклонения</p>
                            <p class="stat-value text-xl font">{{ data_ids.stats.evade }}</p>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script setup>
</script>

<script>
export default {
    data() {
        return {
            ids: useRoute().params,
            error: false,
            weapons: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/left_hand_0.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            armour: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/empty_slot.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            accessories: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/empty_slot.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            classes_en: ['Bogatir', 'Antihrist', 'Bogolub', 'Medvesh', 'Pahan', 'Skomoroh', 'Yazich', 'Zastrel'],
            classes_ru: ['Богатырь', 'Антихрист', 'Боголюб', 'Налётчик', 'Богохульник', 'Скоморох', 'Язычница', 'Застрельщица'],
            class_id: 1,
            data_ids:{
                equiped_ids: {
                    head_id: 0,
                    neck_id: 0,
                    left_hand_id:  0,
                    body_id: 0,
                    right_hand_id: 0,
                    left_ring_id: 0, 
                    belt_id: 0,
                    right_ring_id: 0,
                    gloves_id: 0,
                    boots_id: 0,
                    relic_id: 0,
                },
                stats:{
                    armour: 1005,
                    critical_chance:42,
                    critical_damage: 200,
                    dexterity: 200,
                    elem_damage: 21,
                    elem_res: 30,
                    evade: 0,
                    hp: 10012,
                    intelligence: 200,
                    mp: 503,
                    phys_damage: 0,
                    phys_res: 105,
                    strength: 600,
                    vamp: 0,
                },
                top_inputs:['','','','','',''],
                urlers:'http://localhost:3000/build/'
            }
        }
    },
    methods:{
        check_uri(){
            let true_id = this.ids.id;
            for(let i = 0;i<5;i++)
            {
                true_id = true_id.replace('%slash%','/')
            }
            console.log(true_id)
            let credetentials = {
                name: true_id,
            }
            fetch('http://127.0.0.1:8000/check_url', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(credetentials)
            })
                .then(response => response.json())
                .then(json => {
                    if(json.detail){
                        this.error = true
                    }
                    this.data_ids = json
                    for(let i = 0;i<9;i++){
                        if(this.data_ids.top_inputs[0]==this.classes_ru[i]){
                            this.data_ids.top_inputs[6]=this.classes_en[i]
                        }
                    }
                    console.log(json)
                    
        })
        },
        get_weapons() {
            fetch('http://127.0.0.1:8000/weapons_alt', {
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
                    for (let i = 0; i < json.length; i++) {
                        this.weapons.push(json[i])
                    }
                })
            return null
        },
        get_armour() {
            fetch('http://127.0.0.1:8000/armour_alt', {
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
                    for (let i = 0; i < json.length; i++) {
                        this.armour.push(json[i])
                    }
                })
            return null
        },
        get_accessories() {
            fetch('http://127.0.0.1:8000/accessory_alt', {
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
                    for (let i = 0; i < json.length; i++) {
                        this.accessories.push(json[i])
                    }
                })
            return null
        },
    },
    beforeMount(){
        this.check_uri()
        this.get_accessories()
        this.get_armour()
        this.get_weapons()
        this.urlers = "http://localhost:3000/build/" + this.ids.id
        console.log(this.armour[this.data_ids.equiped_ids.head_id].id)
    }
}

</script>

<style>
.stat-row {
    width: 100%;
}

.stat-name{
    width: 60%;
}

.stat-value {
    width: 40%;
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

.border-shine-passive{
    border: 3px solid;
    border-radius: 100% !important;
    border-color: #9b7f4100 !important;
    box-shadow: 0 0 20px 0 #9b7f4100;
}

.border-shine-passive:hover {
    border: 3px solid;
    border-radius: 100% !important;
    border-color: #9b7e41 !important;
    box-shadow: 0 0 20px 0 #9b7e41;
}

@media screen and (max-width: 1530px){
    .build-name{
        display: none;
    }
    .link-text{
        display: none;
    }
}

@media screen and (max-width: 1280px){
    .col{
        width: 100%;
    }
    .build-info{
        flex-wrap: wrap;
    }
    .selector{
        border: 3px solid;
        border-radius: 25px;
        border-color: #9b7e41 !important;
        box-shadow: 0 0 20px 0 #9b7e41;
    }
    .mid{
        flex-direction: column;
    }
    .panel{
        width: 100% !important;
    }
}
@media screen and (max-width: 1024px){
    .build-info-sub{
        width: 100%;
        flex-direction: column;
    }
    .selector{
        width: 100%;
    }
}
</style>

