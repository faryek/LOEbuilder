<template>
    <div class="flex flex-row justify-evenly">
        <select name="" id="" class="selector border-shine">
            <option value="Мать" class="selector">Все</option>
            <option value="Мать" class="selector">не все</option>
            <option value="Мать" class="selector">Светка</option>
            <option value="Мать" class="selector">Колька</option>
        </select>
        <select name="" id="" class="selector border-shine">
            <option value="Мать" class="selector">Стартер</option>
            <option value="Мать" class="selector">Эндгейм</option>
        </select>
        <select name="" id="" class="selector border-shine">
            <option value="Мать" class="selector">Боссинг</option>
            <option value="Мать" class="selector">Маппинг</option>
        </select>
    </div>
    <div class="container character_selector mt-8" style="min-height: 8vw;">
        <div class="wrapper flex flex-row relative justify-between">
            <button class="icon char_icon1 flex flex-col-reverse border-shine" v-for="i in 8" @click="icon_click = i"
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
                <p class="text-xl font text-center">Дата создания</p>
        </div>
            <BuildCardBig v-for="i in 8" :league="'Первое бытие'" :build_class="classes[i-1]" :build_class_name="classes_ru[i - 1]" :build_lvl="100"
                :build_name="'Билд ' + `${i}`" :build_ehp="'10000'" :build_dps="'10кк'" :id="i"
                :build_date="'09.11.2001'" :more="more" :selected = "selected" class="border-shine" @click="() => {selected = i; if(selected == i){more = true}else{more=false}}"></BuildCardBig>
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
            classes: ['Antihrist', 'Bogatir', 'Bogolub', 'Zastrel', 'Medvesh', 'Pahan', 'Skomoroh', 'Yazich'],
            classes_ru: ['Антихрист', 'Богатырь', 'Боголюб', 'Застрельщица', 'Налетчик', 'Богохульник', 'Скоморох', 'Язычница'],
            decoded:[]
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
                        encoded.push(json[i].name)
                        for(let j = 0;j<5;j++){
                            encoded[i] = encoded[i].replace('%slash%','/')
                        }
                        encoded[i] = decodeURIComponent(atob(encoded[i]))
                        encoded[i] = JSON.parse(encoded[i])
                        // for(let j = 0;j <=5;j++){
                        //     if(j in [0,1,4,5]){
                                
                        //     }
                        // }
                        // this.decoded[i].name = encoded[i]
                    }
                    console.log(encoded)
                    console.log(this.decoded)
                })
            return null
        },
    },
    beforeMount(){
        this.get_urls()
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