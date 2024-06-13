<template>
    <AuthError v-if="!authorized && error"></AuthError>
    <CommonError v-if="error && authorized"></CommonError>
    <CommonError v-if="error_on_choose"></CommonError>
    <div v-if="authorized && !error" class="container flex flex-col" @change="addButton()">
        <div class="top border-shine-create flex flex-col px-10 py-10 gap-10 justify-evenly">
            <div class="flex flex-row justify-evenly gap-10">
                <img :src="`../img/classes/${classes_en[choose_class]}/Medium.png`" class="class-img" alt="">
                <div class="flex flex-col justify-evenly col">
                    <select class="selector selector-create border-shine" name="" id="cycle">
                        <option value="0" class="selector selector-create">Первое бытие</option>
                        <option value="1" class="selector selector-create">Второе житие</option>
                    </select>
                    <select name="" id="class" class="selector selector-create border-shine" @change="() => {get_class()}">
                        <option v-for="i in classes.length" :value="i - 1" class="selector selector-create">{{classes[i - 1].name }}</option>
                    </select>
                    <div class="flex flex-row gap-5">
                        <p class="font font-create">Уровень:</p>
                        <input 
                            type="text"
                            class="font font-create input-field px-4 selector selector-create border-shine"
                            placeholder="100"
                            v-model="level" 
                            @change="set_level_stats()">
                    </div>
                    <p class="font font-create text-center">Ссылка на билд</p>
                </div>
                <div class="flex flex-col justify-evenly col">
                    <input type="text" class="font font-create input-field px-4 selector selector-create border-shine" id="name"
                        placeholder="Фулл понос" v-model="build_info.name">
                    <select name="" id="type" class="selector selector-create border-shine">
                        <option value="0" class="selector selector-create">Стартер</option>
                        <option value="1" class="selector selector-create">Эндгейм</option>
                    </select>
                    <select name="" id="purpose" class="selector selector-create border-shine">
                        <option value="0" class="selector selector-create">Маппинг</option>
                        <option value="1" class="selector selector-create">Боссинг</option>
                    </select>
                    <input type="text" class="font font-create input-field px-4 selector selector-create border-shine"
                        placeholder="" v-model="urlers">
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
                <NuxtLink to="/build/" class="font font-create border-shine-create special-btn text-center" @click="()=>{
                    if(stats.strength.base == 0){
                        error_on_choose = true
                    }
                    else{
                        save_build()
                    }
                }" style="width: 45%;">Создать</NuxtLink>
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
                            <VTooltip>
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
                                <img class="item-img border-shine w-24 slot" :src="equiped.relic.image" alt="" @click="choose_item = 11">
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
        <!-- <div class="bot border-shine-create flex flex-row justify-between mt-5 gap-10 p-10" style="height: 15rem;">
            <div v-for="j in 5" class="1st-col flex flex-col">
                <img v-for="i in 3" :src="passives[i-1 + (j-1)*3].image" class="item-img border-shine-passive" style="width: 50px;">
            </div>
        </div> -->
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
            slots: [[{'id' : 1, 'name' : 'Накст Моча', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': {'effect': 'тест_еффект', 'value_start': 'тест_значение_старт', 'value_end': 'тест_значение_конец'}}]],
            classes: [{ "id": 1, "name": "Богатырь", "main_atr": "Сила", "base_atrs": "60, 20, 20", "base_hp": 1000, "base_mp": 50, "base_armour": 50, "base_evade": 10, "base_elem_res": 30, "base_phys_res": 50 }],
            classes_en: ['Bogatir', 'Antihrist', 'Bogolub', 'Medvesh', 'Pahan', 'Skomoroh', 'Yazich', 'Zastrel'],
            classes_ru: ['Богатырь', 'Антихрист', 'Боголюб', 'Налётчик', 'Богохульник', 'Скоморох', 'Язычница', 'Застрельщица'],
            cycles: ['Первое житие', 'Второе бытие'],
            types: ['Стартер', 'Эндгейм'],
            purposes: ['Маппинг', 'Боссинг'],
            error: false,
            authorized: false,
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
            equiped_ids: {
                head_id: 1,
                neck_id: 1,
                left_hand_id:  1,
                body_id: 1,
                right_hand_id: 1,
                left_ring_id: 1, 
                belt_id: 1,
                right_ring_id: 1,
                gloves_id: 1,
                boots_id: 1,
                relic_id: 1,
            },
            equiped_affixes:{
                1 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
                2 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
                3 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
                4 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
                5 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
                6 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
                7 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
                8 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
                9 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
                10 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
                11 : [{'value_end': 10, 'tag': 'phys_damage'}, {'value_end': 10, 'tag': 'phys_damage'}], 
            },
            equiped_affixes_ids:{
                1 : [1, 2], 
                2 : [1, 2],  
                3 : [1, 2], 
                4 : [1, 2], 
                5 : [1, 2], 
                6 : [1, 2], 
                7 : [1, 2], 
                8 : [1, 2], 
                9 : [1, 2], 
                10 : [1, 2],  
                11 : [1, 2],  
            },
            choose_item: 0,
            show_item: { 'id': 0, 'name': 'Сиракузиан', 'image': '/img/items/one_hand_sword_1.png', 'sub_id': { 'name': 'Сайко', 'item_implicits': [{ 'effect': 'фулл понос', 'value_start': 1, 'value_end': 2, 'tag': 'phys_damage' }] } },
            choose_class: 0,
            level: 1,
			stats:{
                strength:{
                    base: 60,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level: 0,
                },
                dexterity:{
                    base: 20,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                intelligence:{
                    base: 20,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                hp:{
                    base: 1000,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                mp:{
                    base: 50,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                armour:{
                    base: 50,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                phys_res:{
                    base: 0,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                elem_res:{
                    base: 0,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                vamp:{
                    base: 0,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                critical_chance:{
                    base: 0,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                critical_damage:{
                    base: 200,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                phys_damage:{
                    base: 50,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                elem_damage:{
                    base: 30,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                },
                evade:{
                    base: 10,
                    implicits: 0,
                    affixes: 0,
                    passives: 0,
                    level:0,
                }
            },
            stats_export: {
                strength: 1,
                dexterity: 1,
                intelligence: 1,
                hp: 1,
                mp: 1,
                armour: 1,
                phys_res: 1,
                elem_res: 1,
                vamp: 1,
                critical_chance: 1,
                critical_damage: 1,
                phys_damage: 1,
                elem_damage: 1,
                evade: 1,
            },
            stats_dict : {
                1 : 'strength',
                2 : 'dexterity',
                3 : 'intelligence',
                4 : 'hp',
                5 : 'mp',
                6 : 'armour',
                7 : 'phys_res',
                8 : 'elem_res',
                9 : 'vamp',
                10 : 'critical_chance',
                11 : 'critical_damage',
                12 : 'phys_damage',
                13 : 'elem_damage',
                14 : 'evade'
            },
            build_info: {
                cycle: 'none',
                name: '',
                class: 'Богатырь',
                type: 'kys',
                purpose: 'kms',
                lvl: 99,
            },
            save: ['Сохранить'],
            saved: 1,
            encoded: '',
            urlers: `http://localhost:3000/build/`,
            build_name: '',
            error_on_choose: false
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
        save_all(){
            for (let i = 1; i < 12; i++) {
                this.equiped_ids[`${this.equipment[`${i}`]}_id`] = this.equiped[`${this.equipment[`${i}`]}`].id
                this.equiped_affixes_ids[`${i}`] = this.equiped_affixes[`${i}`]
            }
            for (let i = 1; i < 15; i++) {
                this.stats_export[`${this.stats_dict[`${i}`]}`] = this.get_stat(this.stats_dict[`${i}`])
            }
            this.build_info.cycle = this.cycles[document.getElementById('cycle').value]
            this.build_info.type = this.types[document.getElementById('type').value]
            this.build_info.purpose = this.purposes[document.getElementById('purpose').value]
            this.build_info.lvl = this.level
            this.build_info.class = this.classes_ru[document.getElementById('class').value]
        },
        removeButton(btn){
            this.save_all()
            this.save.pop()
            this.saved = 0
            this.encode()
        },
        addButton() {
            if (this.saved < 1)
            {
                this.save.push('Сохранить')
            }
            this.saved++
        },
        encode(){
            var obj = {equiped_ids: this.equiped_ids, equiped_affixes_ids: this.equiped_affixes_ids, top_inputs: this.build_info, stats: this.stats_export};
            if(this.stats.strength == 0){
                this.error_on_choose = true
                return null
            }
            this.encoded = btoa(unescape(encodeURIComponent(JSON.stringify(obj))))
            for(let i = 0;i<5;i++)
            {
                this.encoded = this.encoded.replace('/','%slash%')
            }
            console.log(this.encoded)
        },
        get_stat(name){
            return +this.stats[`${name}`].base + +this.stats[`${name}`].level + +this.stats[`${name}`].affixes + +this.stats[`${name}`].implicits
        },
        set_implicits_stat() {
            for (let j = 1; j < 15; j++) {
                this.stats[`${this.stats_dict[`${j}`]}`].implicits = 0
                for (let i = 1; i < 12; i++) {
                    if (this.stats_dict[`${j}`] == this.equiped[`${this.equipment[`${i}`]}`].sub_id.item_implicits[0].tag) {
                        this.stats[`${this.stats_dict[`${j}`]}`].implicits = this.stats[`${this.stats_dict[`${j}`]}`].implicits + this.equiped[`${this.equipment[`${i}`]}`].sub_id.item_implicits[0].value_end
                    }
                }
            }
        },
        set_prefix_stat(){
            for (let j = 1; j < 15; j++) {
                this.stats[`${this.stats_dict[`${j}`]}`].affixes = 0
                for (let i = 1; i < 12; i++) {
                    if (this.stats_dict[`${j}`] == this.equiped_affixes[`${i}`][0].tag) {
                        this.stats[`${this.stats_dict[`${j}`]}`].affixes += this.equiped_affixes[`${i}`][0].value_end
                    }
                }
            }
        },
        set_suffix_stat() {
            for (let j = 1; j < 15; j++) {
                this.stats[`${this.stats_dict[`${j}`]}`].affixes = 0
                for (let i = 1; i < 12; i++) {
                    if (this.stats_dict[`${j}`] == this.equiped_affixes[`${i}`][1].tag) {
                        this.stats[`${this.stats_dict[`${j}`]}`].affixes += this.equiped_affixes[`${i}`][1].value_end
                    }
                }
            }
        },
        set_level_stats() {
            if (+this.level > 100) this.level = 100
            else if (+this.level < 1) this.level = 1
            this.stats.armour.level = this.level*this.classes[this.choose_class].base_armour/5 + 5
            this.stats.hp.level = this.level*this.classes[this.choose_class].base_hp/10 + 12
            this.stats.mp.level = this.level*this.classes[this.choose_class].base_mp/10 + 3
            this.stats.strength.level = this.level*this.classes[this.choose_class].base_atrs.split(', ')[0]/10
            this.stats.dexterity.level = this.level*this.classes[this.choose_class].base_atrs.split(', ')[1]/10
            this.stats.intelligence.level = this.level*this.classes[this.choose_class].base_atrs.split(', ')[2]/10
        },
        set_base_stats(){
            this.stats.hp.base = this.classes[this.choose_class].base_hp
            this.stats.mp.base = this.classes[this.choose_class].base_mp
            this.stats.armour.base = this.classes[this.choose_class].base_armour
            this.stats.evade.base = this.classes[this.choose_class].base_evade
            this.stats.elem_res.base = this.classes[this.choose_class].base_elem_res
            this.stats.phys_res.base = this.classes[this.choose_class].base_phys_res
            this.stats.strength.base = this.classes[this.choose_class].base_atrs.split(', ')[0]
            this.stats.dexterity.base = this.classes[this.choose_class].base_atrs.split(', ')[1]
            this.stats.intelligence.base = this.classes[this.choose_class].base_atrs.split(', ')[2]
        },
        get_class() {
            this.choose_class = document.getElementById('class').value
            this.set_base_stats()
            console.log(this.stats)
        },
        get_item(j) {
            this.equiped[`${this.equipment[`${this.choose_item}`]}`] = this.slots[this.choose_item][j]
            this.show_item = this.slots[this.choose_item][j]
            this.set_implicits_stat()
            this.choose_item = 0
            this.addButton()
        },
        save_build(){
            let token = localStorage.getItem('token')
            let credetentials = {
                name: this.encoded,
                build_name: this.build_info.name,
                class_id: this.choose_class.class_id - 1,
            }
            fetch('http://127.0.0.1:8000/build/url_create', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify(credetentials)
            })
                .then(response => response.json())
                .then(json => {
                    if(json.detail){
                        this.error = true
                    console.log('xdddd')
        }});
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
                    this.passives = []
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

