<template>
    <BuildError v-if="error"></BuildError>
    <div v-if="!error">
        <div v-if="!error" class="container flex flex-col" @change="addButton()">
            <div class="top border-shine-create flex flex-col px-10 py-10 gap-10 justify-evenly">
                <div class="flex flex-row justify-evenly gap-10">
                    <img :src="`../img/classes/${data_ids.top_inputs[6]}/Medium.png`" class="class-img" alt="">
                    <div class="flex flex-col justify-evenly col">
                        <p class="font font-create text-center">{{data_ids.top_inputs[1]}}</p>
                        <p class="font font-create text-center">{{data_ids.top_inputs[0]}}</p>
                        <div class="flex flex-row gap-5">
                            <p class="font font-create text-center">{{data_ids.top_inputs[2]}}</p>
                        </div>
                        <p class="font font-create text-center">Ссылка на билд</p>
                    </div>
                    <div class="flex flex-col justify-evenly col">
                        <p class="font font-create text-center">{{data_ids.top_inputs[3]}}</p>
                        <p class="font font-create text-center">{{data_ids.top_inputs[5]}}</p>
                        <p class="font font-create text-center">{{data_ids.top_inputs[4]}}</p>
                        <input type="text" class="font font-create input-field px-4 selector selector-create border-shine" placeholder="" v-model="urlers">
                    </div>
                </div>
            </div>
            <div class="mid flex flex-row justify-center mt-5 gap-10">
                <div class="border-shine-create p-10" style="width: 30%;">
                    <div class="item-col flex flex-col gap-2">
                        <div class="item-row flex flex-row justify-center gap-2">
                        <div class="">
                            <img class="item-img border-shine w-14 slot" src="public/img/items/neck_0.png" alt=""
                                style="opacity: 0;">
                        </div>
                        <div class="">
                            <VTooltip>
                                <!-- HELMET -->
                                <img class="item-img border-shine w-24 slot" :src="equiped.head.image" alt="" @click="choose_item = 1">
                                <template #popper v-if="equiped.head.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.head.name" :image="equiped.head.image" :sub_name="equiped.head.sub_id.name"
                                                :implicits_value_start="equiped.head.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.head.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.head.sub_id.item_implicits[0].effect">

                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>
                        <div class="">
                            <!-- NECKLACE -->
                            <VTooltip>
                                <img class="item-img border-shine w-14 slot" :src="equiped.neck.image" alt="" @click="choose_item = 2">
                                <template #popper v-if="equiped.neck.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.neck.name" :image="equiped.neck.image" :sub_name="equiped.neck.sub_id.name"
                                                :implicits_value_start="equiped.neck.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.neck.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.neck.sub_id.item_implicits[0].effect">

                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>
                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="">
                            <VTooltip>
                                <!-- LEFT_HAND_WPN -->
                                <img class="item-img border-shine w-24 slot" :src="equiped.left_hand.image" alt="" @click="choose_item = 3">
                                <template #popper v-if="equiped.left_hand.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.left_hand.name" :image="equiped.left_hand.image" :sub_name="equiped.left_hand.sub_id.name"
                                                :implicits_value_start="equiped.left_hand.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.left_hand.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.left_hand.sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- BODYARMOUR -->
                                <img class="item-img border-shine w-36 slot" :src="equiped.body.image" alt="" @click="choose_item = 4">
                                <template #popper v-if="equiped.body.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.body.name" :image="equiped.body.image" :sub_name="equiped.body.sub_id.name"
                                                :implicits_value_start="equiped.body.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.body.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.body.sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- RIGHT_HAND_WPN -->
                                <img class="item-img border-shine w-24 slot" :src="equiped.right_hand.image" alt="" @click="choose_item = 5">
                                <template #popper v-if="equiped.right_hand.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.right_hand.name" :image="equiped.right_hand.image" :sub_name="equiped.right_hand.sub_id.name"
                                                :implicits_value_start="equiped.right_hand.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.right_hand.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.right_hand.sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="">
                            <VTooltip>
                                <!-- LEFT_RING -->
                                <img class="item-img border-shine w-14 slot" :src="equiped.left_ring.image" alt="" @click="choose_item = 6">
                                <template #popper v-if="equiped.left_ring.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.left_ring.name" :image="equiped.left_ring.image" :sub_name="equiped.left_ring.sub_id.name"
                                                :implicits_value_start="equiped.left_ring.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.left_ring.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.left_ring.sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- BELT -->
                                <img class="item-img border-shine w-36 slot" :src="equiped.belt.image" alt="" @click="choose_item = 7">
                                <template #popper v-if="equiped.belt.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.belt.name" :image="equiped.belt.image" :sub_name="equiped.belt.sub_id.name"
                                                :implicits_value_start="equiped.belt.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.belt.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.belt.sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- RIGHT_RING -->
                                <img class="item-img border-shine w-14 slot" :src="equiped.right_ring.image" alt="" @click="choose_item = 8">
                                <template #popper v-if="equiped.right_ring.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.right_ring.name" :image="equiped.right_ring.image" :sub_name="equiped.right_ring.sub_id.name"
                                                :implicits_value_start="equiped.right_ring.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.right_ring.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.right_ring.sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                    </div>
                    <div class="item-row flex flex-row justify-center gap-2">

                        <div class="">
                            <VTooltip>
                                <!-- GLOVES -->
                                <img class="item-img border-shine w-24 slot" :src="equiped.gloves.image" alt="" @click="choose_item = 9">
                                <template #popper v-if="equiped.gloves.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.gloves.name" :image="equiped.gloves.image" :sub_name="equiped.gloves.sub_id.name"
                                                :implicits_value_start="equiped.gloves.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.gloves.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.gloves.sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- BOOTS -->
                                <img class="item-img border-shine w-24 slot" :src="equiped.boots.image" alt="" @click="choose_item = 10">
                                <template #popper v-if="equiped.boots.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.boots.name" :image="equiped.boots.image" :sub_name="equiped.boots.sub_id.name"
                                                :implicits_value_start="equiped.boots.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.boots.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.boots.sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                        <div class="">
                            <VTooltip>
                                <!-- RELIC -->
                                <template #popper v-if="equiped.relic.id != 0">
                                    <ItemTooltip 
                                                :name="equiped.relic.name" :image="equiped.relic.image" :sub_name="equiped.relic.sub_id.name"
                                                :implicits_value_start="equiped.relic.sub_id.item_implicits[0].value_start"
                                                :implicits_value_end="equiped.relic.sub_id.item_implicits[0].value_end"
                                                :implicits_effect="equiped.relic.sub_id.item_implicits[0].effect">
                            
                                    </ItemTooltip>
                                </template>
                            </VTooltip>
                        </div>

                    </div>
                    </div>
                </div>
                
                <div class="border-shine-create p-10" style="width: 30%;">
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
            nuxtxdd: 0,
            weapons: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            armour: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            accessories: [{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}],
            passives: [{"id": 1,"name": "Ловкость","desc": "+15 к ловкости","image": "/img/icons/dexterity.png","effects": [{"id": 1,"name": "dexterity","value": 15}]},],
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
            },
            equiped: {
                head: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/head_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 0, 'value_end': 0, 'tag': 'phys_damage' }] } },
                neck: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/neck_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 0, 'value_end': 0, 'tag': 'phys_damage' }] } },
                left_hand: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/left_hand_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 0, 'value_end': 0, 'tag': 'phys_damage' }] } },
                body: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/body_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 0, 'value_end': 0, 'tag': 'phys_damage' }] } },
                right_hand: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/right_hand_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 0, 'value_end': 0, 'tag': 'phys_damage' }] } },
                left_ring: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/ring_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 1, 'value_end': 0, 'tag': 'phys_damage' }] } },
                belt: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/belt_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 0, 'value_end': 0, 'tag': 'phys_damage' }] } },
                right_ring: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/ring_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 1, 'value_end': 0, 'tag': 'phys_damage' }] } },
                gloves: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/gloves_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 0, 'value_end': 0, 'tag': 'phys_damage' }] } },
                boots: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/boots_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 0, 'value_end': 0, 'tag': 'phys_damage' }] } },
                relic: { 'id': 0, 'name': 'Сиракузиан', 'image': '../img/items/relic_0.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 0, 'value_end': 0, 'tag': 'phys_damage' }] } },
            },
            equipment: { 1: 'head', 2: 'neck', 3: 'left_hand', 4: 'body', 5: 'right_hand', 6: 'left_ring', 7: 'belt', 8: 'right_ring', 9: 'gloves', 10: 'boots', 11: 'relic' },
            slots: [[{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}]],
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
        fillEquiped(){
            for (let i = 1; i < 12; i++){
                if (this.data_ids.equiped_ids[`${this.equipment[`${i}`]}_id`] != 0) {
                    for (let j = 1; j < this.slots[i].length; j++){
                        if (this.slots[i][j].id == this.data_ids.equiped_ids[`${this.equipment[`${i}`]}_id`]){
                            this.equiped[`${this.equipment[`${i}`]}`] = this.slots[i][j]
                            console.log('второй иф')
                        }
                    }
                }
                console.log(this.slots[i].length)
            }
        }
    },
    beforeMount(){
        this.check_uri()
        this.get_accessories()
        this.get_armour()
        this.get_weapons()
        this.urlers = "http://localhost:3000/build/" + this.ids.id
        this.slots.push(this.heads, this.necks, this.left_hands, this.bodies, this.right_hands, this.rings, this.belts, this.rings, this.gloves, this.boots, this.relics)
    },
    mounted(){
        this.nuxtxdd = 1
    },
    updated(){
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
</style>

