<template>
    <BuildError v-if="error"></BuildError>
    <!-- <div v-if="!error">
        <div v-if="!error" class="container flex flex-col" @change="addButton()">
            <div class="top border-shine-create flex flex-col px-10 py-10 gap-10 justify-evenly">
                <div class="flex flex-row justify-evenly gap-10">
                    <img :src="`../img/classes/${classes_en[class_id]}/Medium.png`" class="class-img" alt="">
                    <div class="flex flex-col justify-evenly col">
                        <p class="font font-create text-center">{{data['top_inputs']['cycle']}}</p>
                        <p class="font font-create text-center">{{data['top_inputs']['class']}}</p>
                        <div class="flex flex-row gap-5">
                            <p class="font font-create text-center">{{data['top_inputs']['lvl']}}</p>
                        </div>
                        <p class="font font-create text-center">Ссылка на билд</p>
                    </div>
                    <div class="flex flex-col justify-evenly col">
                        <p class="font font-create text-center">{{data['top_inputs']['name']}}</p>
                        <p class="font font-create text-center">{{data['top_inputs']['type']}}</p>
                        <p class="font font-create text-center">{{data['top_inputs']['purpose']}}</p>
                        <p class="font font-create text-center">http://localhost:3000/build/{{ ids.id }}</p>
                    </div>
                </div>
                <div class="flex flex-row justify-between">
                    <ul v-auto-animate style="width: 45%;">
                        <li
                            v-for="k in save"
                            @click="()=>{
                                removeButton(k)
                                urlers = `http://localhost:3000/build/${encoded}`
                                }"
                            style="width: 100%;"
                        >
                            <button class="font font-create border-shine-create special-btn" style="width: 100%;">{{ k }}</button>
                        </li>
                    </ul>
                    <button class="font font-create border-shine-create special-btn" @click="()=>{
                        save_build()
                    }" style="width: 45%;">Создать</button>
                </div>
            </div>
            <div class="mid flex flex-row justify-between mt-5 gap-10">
                <div class="border-shine-create p-10" style="width: 30%;">
                    <div class="item-col flex flex-col gap-2">
                        <div class="item-row flex flex-row justify-center gap-2">
                            <div class="">
                                <img class="item-img border-shine w-14 slot" src="public/img/items/neck_0.png" alt=""
                                    style="opacity: 0;">
                            </div>
                            <div class="">
                                <img class="item-img border-shine w-24 slot" :src="equiped.head.image" alt="" @click="choose_item = 1">
                            </div>
                            <div class="">
                                <img class="item-img border-shine w-14 slot" :src="equiped.neck.image" alt="" @click="choose_item = 2">
                            </div>

                        </div>
                        <div class="item-row flex flex-row justify-center gap-2">

                            <div class="">
                                <img class="item-img border-shine w-24 slot" :src="equiped.left_hand.image" alt="" @click="choose_item = 3">
                            </div>

                            <div class="">
                                <img class="item-img border-shine w-36 slot" :src="equiped.body.image" alt="" @click="choose_item = 4">
                            </div>

                            <div class="">
                                <img class="item-img border-shine w-24 slot" :src="equiped.right_hand.image" alt="" @click="choose_item = 5">
                            </div>

                        </div>
                        <div class="item-row flex flex-row justify-center gap-2">

                            <div class="">
                                <img class="item-img border-shine w-14 slot" :src="equiped.left_ring.image" alt="" @click="choose_item = 6">
                            </div>

                            <div class="">
                                <img class="item-img border-shine w-36 slot" :src="equiped.belt.image" alt="" @click="choose_item = 7">
                            </div>

                            <div class="">
                                <img class="item-img border-shine w-14 slot" :src="equiped.right_ring.image" alt="" @click="choose_item = 8">
                            </div>

                        </div>
                        <div class="item-row flex flex-row justify-center gap-2">

                            <div class="">
                                <img class="item-img border-shine w-24 slot" :src="equiped.gloves.image" alt="" @click="choose_item = 9">
                            </div>

                            <div class="">
                                <img class="item-img border-shine w-24 slot" :src="equiped.boots.image" alt="" @click="choose_item = 10">
                            </div>

                            <div class="">
                                <img class="item-img border-shine w-24 slot" :src="equiped.relic.image" alt="" @click="choose_item = 11">
                            </div>

                        </div>
                    </div>
                </div>
                <div class="border-shine-create p-10" style="width: 40%;">
                    <div v-for="i in 11" v-show="choose_item == i" class="container flex flex-wrap p-10 gap-5">
                        <img v-for="j in slots[choose_item].length" v-show="j != 1" class="border-shine item-img slot"
                            :src="`..${slots[choose_item][j - 1].image}`" alt="" @click="get_item(j - 1)">
                    </div>
                    <div v-show="choose_item == 0 && show_item.id != 0" class="container p-5 flex flex-col justify-between align-middle">
                        <div class="flex flex-row justify-between align-middle" style="width: 100%;">
                            <img class="item-img" :src="`..${show_item.image}`" alt="">
                            <div class="flex flex-col justify-evenly">
                                <div class="flex flex-row gap-2">
                                    <p class="text-xl font">{{ show_item.name }}</p>
                                    <p class="text-xl font">{{ show_item.sub_id.name }}</p>
                                </div>
                                <div class="flex flex-row gap-2">
                                    <p class="text-xl font">+{{ show_item.sub_id.item_implicits[0].value_start }}</p>
                                    <p class="text-xl font">-</p>
                                    <p class="text-xl font">{{ show_item.sub_id.item_implicits[0].value_end }}</p>
                                    <p class="text-xl font">{{ show_item.sub_id.item_implicits[0].effect }}</p>
                                </div>
                                <button class="font text-2xl border-shine" style="width: 100%;">Снять</button>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="border-shine-create p-10" style="width: 30%;">
                    <div class="flex flex-col justify-evenly" style="height: 100%;">
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="text-xl stat-name font">Аттрибуты</p>
                            <div class="flex flex-row stat-value justify-end">
                                <p class="text-xl font" style="color: red;">{{ get_stat('strength') }}</p>
                                <p style="color: white;">/</p>
                                <p class="text-xl font" style="color: green;">{{ get_stat('dexterity') }}</p>
                                <p style="color: white;">/</p>
                                <p class="text-xl font" style="color: blue;">{{ get_stat('intelligence') }}</p>
                            </div>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Физ. урон</p>
                            <p class="stat-value text-xl font">{{get_stat('phys_damage')}}</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Элем. урон</p>
                            <p class="stat-value text-xl font">{{get_stat('elem_damage')}}</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Здоровье</p>
                            <p class="stat-value text-xl font">{{ get_stat('hp') }}</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Мана</p>
                            <p class="stat-value text-xl font">{{ get_stat('mp') }}</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Броня</p>
                            <p class="stat-value text-xl font">{{ get_stat('armour') }}</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Сопр. физ.урону</p>
                            <p class="stat-value text-xl font">{{ get_stat('phys_res') }}%</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Сопр. элем.урону</p>
                            <p class="stat-value text-xl font">{{ get_stat('elem_res') }}%</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Шанс крит.удара</p>
                            <p class="stat-value text-xl font">{{get_stat('critical_chance')}}%</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Крит. урон</p>
                            <p class="stat-value text-xl font">{{get_stat('critical_damage')}}%</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Вампиризм</p>
                            <p class="stat-value text-xl font">{{get_stat('vamp')}}%</p>
                        </div>
                        <div class="stat-row flex flex-row justyfy-between">
                            <p class="stat-name text-xl font">Шанс уклонения</p>
                            <p class="stat-value text-xl font">{{ get_stat('evade') }}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="bot border-shine-create flex flex-row justify-between mt-5 gap-10 p-10" style="height: 15rem;">
                <div v-for="j in 5" class="1st-col flex flex-col">
                    <img v-for="i in 3" :src="passives[i-1 + (j-1)*3].image" class="item-img border-shine-passive" style="width: 50px;">
                </div>
            </div>
        </div>
    </div> -->
</template>

<script setup>
</script>

<script>
export default {
    data() {
        return {
            ids: useRoute().params,
            error: false,
            weapons: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            armour: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            accessories: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            heads:[{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            necks: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            bodies: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            gloves: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            boots: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            relics:[{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            left_hands: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            right_hands: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            belts:[{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            rings: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            classes_en: ['Bogatir', 'Antihrist', 'Bogolub', 'Medvesh', 'Pahan', 'Skomoroh', 'Yazich', 'Zastrel'],
            classes_ru: ['Богатырь', 'Антихрист', 'Боголюб', 'Налётчик', 'Богохульник', 'Скоморох', 'Язычница', 'Застрельщица'],
            class_id: 1,
            data_ids:{}
        }
    },
    methods:{
        check_uri(){
            let credetentials = {
                name: this.ids.id,
            }
            fetch('http://127.0.0.1:8000/check_url/', {
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
                    this.data.push(json['equiped_ids'],json['stats'],json['top_inputs'])
                    for(let i = 0;i < 9;i++){
                        if(json['top_inputs']['class']==this.classes_ru[i]){
                            this.class_id = i
                            break
                        }
                    }
        }})
        },
        decode_uri(){
            console.log(decodeURIComponent(escape(window.atob(this.ids.id))))
        },
        get_weapons(token) {
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
                            this.boots.push(json[i])
                        }
                    }
                })
            return null
        },
        get_accessories(token) {
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
    },
    beforeMount(){
        this.check_uri()
        this.decode_uri()
    }
}

</script>

<style>

</style>