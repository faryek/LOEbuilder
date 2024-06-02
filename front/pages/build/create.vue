<template>
    <AuthError v-if="!authorized && error"></AuthError>
    <CommonError v-if="error && authorized"></CommonError>
    <div v-if="authorized && !error" class="container flex flex-col" @change="addButton()">
        <div class="top border-shine-create flex flex-col px-10 py-10 gap-10 justify-evenly">
            <div class="flex flex-row justify-evenly gap-10">
                <img :src="`../img/classes/${classes_en[choose_class]}/Medium.png`" class="class-img" alt="">
                <div class="flex flex-col justify-evenly col">
                    <select class="selector selector-create border-shine" name="" id="">
                        <option value="1" class="selector selector-create">Первое бытие</option>
                        <option value="2" class="selector selector-create">Второе житие</option>
                    </select>
                    <select name="" id="class" class="selector selector-create border-shine" @change="() => {get_class()}">
                        <option v-for="i in classes.length" :value="i - 1" class="selector selector-create">{{classes[i - 1].name }}</option>
                    </select>
                    <div class="flex flex-row gap-5">
                        <p class="font font-create">Уровень:</p>
                        <input type="text"
                            class="font font-create input-field px-4 selector selector-create border-shine"
                            placeholder="100">
                    </div>
                    <p class="font font-create text-center">Ссылка на билд</p>
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
                    <input type="text" class="font font-create input-field px-4 selector selector-create border-shine"
                        placeholder="...">
                </div>
            </div>
            <ul v-auto-animate>
                <li
                    v-for="k in save"
                    @click="removeButton(k)"
                    style="width: 100%;"
                >
                    <button class="font font-create border-shine-create special-btn" style="width: 100%;">{{ k }}</button>
                </li>
            </ul>
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
                            <img class="item-img border-shine w-24" :src="equiped.head.image" alt="">
                        </div>
                        <div class="slot" @click="choose_item = 2">
                            <img class="item-img border-shine w-14" :src="equiped.neck.image" alt="">
                        </div>

                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="slot" @click="choose_item = 3">
                            <img class="item-img border-shine w-24" :src="equiped.left_hand.image" alt="">
                        </div>

                        <div class="slot" @click="choose_item = 4">
                            <img class="item-img border-shine w-36" :src="equiped.body.image" alt="">
                        </div>

                        <div class="slot" @click="choose_item = 5">
                            <img class="item-img border-shine w-24" :src="equiped.right_hand.image" alt="">
                        </div>

                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="slot" @click="choose_item = 6">
                            <img class="item-img border-shine w-14" :src="equiped.left_ring.image" alt="">
                        </div>

                        <div class="slot" @click="choose_item = 7">
                            <img class="item-img border-shine w-36" :src="equiped.belt.image" alt="">
                        </div>

                        <div class="slot" @click="choose_item = 8">
                            <img class="item-img border-shine w-14" :src="equiped.right_ring.image" alt="">
                        </div>

                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="slot" @click="choose_item = 9">
                            <img class="item-img border-shine w-24" :src="equiped.gloves.image" alt="">
                        </div>

                        <div class="slot" @click="choose_item = 10">
                            <img class="item-img border-shine w-24" :src="equiped.boots.image" alt="">
                        </div>

                        <div class="slot" @click="choose_item = 11">
                            <img class="item-img border-shine w-24" :src="equiped.relic.image" alt="">
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
                        </div>
                    </div>
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
                            <p class="text-xl font" style="color: blue;">{{ classes[choose_class].base_atrs.split(', ')[2] }}</p>
                        </div>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Физ. урон</p>
                        <p class="stat-value text-xl font">+ 100-150</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Маг. урон</p>
                        <p class="stat-value text-xl font">+ 10-15</p>
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
                        <p class="stat-value text-xl font">{{50}}%</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Крит. урон</p>
                        <p class="stat-value text-xl font">{{100}}%</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Вампиризм</p>
                        <p class="stat-value text-xl font">{{40}}%</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Шанс вампиризма</p>
                        <p class="stat-value text-xl font">{{ 20 }}%</p>
                    </div>
                    <div class="stat-row flex flex-row justyfy-between">
                        <p class="stat-name text-xl font">Шанс уклонения</p>
                        <p class="stat-value text-xl font">{{ classes[choose_class].base_evade }}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="bot border-shine-create flex flex-row justify-between mt-5 gap-10" style="height: 50rem;">
            
        </div>
    </div>

</template>


<script>
export default {
    data() {
        return {
            weapons: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            armour: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            accessories: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            affixes: [],
            passives: [],
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
            slots: [[{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}]],
            classes: [{ "id": 1, "name": "Богатырь", "main_atr": "Сила", "base_atrs": "60, 20, 20", "base_hp": 1000, "base_mp": 50, "base_armor": 50, "base_evade": 10, "base_ele_res": 30, "base_phys_res": 50 }],
            classes_en: ['Bogatir', 'Antihrist', 'Bogolub', 'Medvesh', 'Pahan', 'Skomoroh', 'Yazich', 'Zastrel'],
            error: false,
            authorized: false,
            equiped: {
                head: { 'image': '../img/items/head_0.png' },
                neck: { 'image': '../img/items/neck_0.png' },
                left_hand: { 'image': '../img/items/left_hand_0.png' },
                body: { 'image': '../img/items/body_0.png' },
                right_hand: { 'image': '../img/items/right_hand_0.png' },
                left_ring: { 'image': '../img/items/ring_0.png' },
                belt: { 'image': '../img/items/belt_0.png' },
                right_ring: { 'image': '../img/items/ring_0.png' },
                gloves: { 'image': '../img/items/gloves_0.png' },
                boots: { 'image': '../img/items/boots_0.png' },
                relic: { 'image': '../img/items/relic_0.png' },
            },
            equipment: { 1: 'head', 2: 'neck', 3: 'left_hand', 4: 'body', 5: 'right_hand', 6: 'left_ring', 7: 'belt', 8: 'right_ring', 9: 'gloves', 10: 'boots', 11: 'relic' },
            choose_item: 0,
            show_item: { 'id': 0, 'name': 'Сиракузиан', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 'писюмба', 'value_end': 'нти' }] } },
            choose_class: 0,
			stats:{
                strength:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                dexterity:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                intelligence:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [],
                    level:0,
                },
                hp:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                mana:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                armour:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                phys_res:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                poison_res:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                void_res:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                cold_res:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                fire_res:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                lightning_res:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                necrotic_res:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                vamp_chance:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                vamp:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                critical_chance:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                critical_damage:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                phys_damage:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                },
                mag_damage:{
                    base: 0,
                    implicits: [0],
                    affixes: [0],
                    passives: [0],
                    level:0,
                }
            },
            save: ['Сохранить'],
            saved: 1
        }
    },
    props: [],
    methods: {
        get_auth(token) {
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
        removeButton(btn){
            this.save.pop()
            this.saved = 0
        },
        addButton() {
            if (this.saved < 1)
            {
                this.save.push('Сохранить')
            }
            this.saved++
        },
        get_class() {
            this.choose_class = document.getElementById('class').value
        },
        get_item(j) {
            this.equiped[`${this.equipment[`${this.choose_item}`]}`] = this.slots[this.choose_item][j]
            this.show_item = this.slots[this.choose_item][j]
            this.choose_item = 0
            this.addButton()
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
                            this.boots.push(json[i])
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
                    for (let i = 0; i < json.length; i++) {
                        this.classes.push(json[i])
                    }
                    this.classes.splice(0,1)
                })
            return null
        },
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
        this.slots.push(this.heads, this.necks, this.left_hands, this.bodies, this.right_hands, this.rings, this.belts, this.rings, this.gloves, this.boots, this.relics)
        console.log(this.slots)
    },
    updated() {
        let token = localStorage.getItem('token')
        if (token) {
            this.authorized = true
        }
        this.get_auth(token)
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