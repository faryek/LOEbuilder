<template>
    <div class="container flex flex-col">
        <div class="border-shine-create flex flex-row px-10 py-10 gap-10 top justify-evenly">
            <img src="public/img/classes/Antihrist/Medium.png" class="class-img" alt="">
            <div class="flex flex-col justify-evenly col">
                <select class="selector selector-create border-shine" name="" id="">
                    <option value="1" class="selector selector-create">Первое бытие</option>
                    <option value="2" class="selector selector-create">Второе житие</option>
                </select>
                <select name="" id="" class="selector selector-create border-shine">
                    <option value="" class="selector selector-create">Антихрист</option>
                    <option value="" class="selector selector-create">Богатырь</option>
                    <option value="" class="selector selector-create">Боголюб</option>
                    <option value="" class="selector selector-create">Застрельщица</option>
                    <option value="" class="selector selector-create">Налетчик</option>
                    <option value="" class="selector selector-create">Богохульник</option>
                    <option value="" class="selector selector-create">Скоморох</option>
                    <option value="" class="selector selector-create">Язычница</option>
                </select>
                <div class="flex flex-row gap-5">
                    <p class="font font-create">Уровень:</p>
                    <input type="text" class="font font-create input-field px-4" placeholder="100">
                </div>
            </div>
            <div class="flex flex-col justify-evenly col">
                <input type="text" class="font font-create input-field px-4" placeholder="Фулл понос">
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
        <div class="mid flex flex-row justify-between mt-5">
            <div class="border-shine-create p-10">
                <div class="item-col flex flex-col">
                    <div class="item-row flex flex-row justify-end align-bottom">
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/head_placeholder.png" alt="">
                            </div>
                        </a>
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/neck_placeholder.png" alt="">
                            </div>
                        </a>
                    </div>
                    <div class="item-row flex flex-row">
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/weapon_placeholder.png" alt="">
                            </div>
                        </a>
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/body_placeholder.png" alt="">
                            </div>
                        </a>
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/shield_placeholder.png" alt="">
                            </div>
                        </a>
                    </div>
                    <div class="item-row flex flex-row">
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/ring_placeholder.png" alt="">
                            </div>
                        </a>
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/belt_placeholder.png" alt="">
                            </div>
                        </a>
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/ring_placeholder.png" alt="">
                            </div>
                        </a>
                    </div>
                    <div class="item-row flex flex-row">
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/gloves_placeholder.png" alt="">
                            </div>
                        </a>
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/boots_placeholder.png" alt="">
                            </div>
                        </a>
                        <a href="">
                            <div class="slot">
                                <img src="public/img/items/relic_placeholder.png" alt="">
                            </div>
                        </a>
                    </div>
                </div>
            </div>
            <div class="border-shine-create p-10">

            </div>
        </div>
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
            classes: [],
            error: false,
            authorized: false
        }
    },
    methods: {
        get_weapons(token) {
            fetch('http://127.0.0.1:8000/weapons', {
                method: 'GET',
                headers: {
                    Authorization: `Bearer ${token}`,
                }
                }).then(response => response.json())
                .then(json =>{
                    if(json.detail){
                        this.error = true
                    }
                    for(let i =0;i < json.length;i++){
                        this.weapons.push(json[i])
                    }
                })
        },
        get_armour(token) {
            fetch('http://127.0.0.1:8000/armour', {
                method: 'GET',
                headers: {
                    Authorization: `Bearer ${token}`,
                }
                }).then(response => response.json())
                .then(json =>{
                    if(json.detail){
                        this.error = true
                    }
                    for(let i =0;i < json.length;i++){
                        this.armour.push(json[i])
                    }
                })
        },
        get_accessories(token) {
            fetch('http://127.0.0.1:8000/accessory', {
                method: 'GET',
                headers: {
                    Authorization: `Bearer ${token}`,
                }
                }).then(response => response.json())
                .then(json =>{
                    if(json.detail){
                        this.error = true
                    }
                    for(let i =0;i < json.length;i++){
                        this.accessories.push(json[i])
                    }
                })
        },
        get_affixes(token) {
            fetch('http://127.0.0.1:8000/affixes', {
                method: 'GET',
                headers: {
                    Authorization: `Bearer ${token}`,
                }
                }).then(response => response.json())
                .then(json =>{
                    if(json.detail){
                        this.error = true
                    }
                    for(let i =0;i < json.length;i++){
                        this.affixes.push(json[i])
                    }
                })
        },
        get_passives(token) {
            fetch('http://127.0.0.1:8000/passives', {
                method: 'GET',
                headers: {
                    Authorization: `Bearer ${token}`,
                }
                }).then(response => response.json())
                .then(json =>{
                    if(json.detail){
                        this.error = true
                    }
                    for(let i =0;i < json.length;i++){
                        this.passives.push(json[i])
                    }
                })
        },
        get_classes(token) {
            fetch('http://127.0.0.1:8000/classes', {
                method: 'GET',
                headers: {
                    Authorization: `Bearer ${token}`,
                }
                }).then(response => response.json())
                .then(json =>{
                    if(json.detail){
                        this.error = true
                    }
                    for(let i =0;i < json.length;i++){
                        this.classes.push(json[i])
                    }
                })
        }
    },
    mounted(){
        let token = localStorage.getItem('token')
        if(token){
            this.authorized = true
        }
        this.get_weapons(token)
        this.get_armour(token)
        this.get_accessories(token)
        this.get_affixes(token)
        this.get_passives(token)
        this.get_classes(token)
    }
}
</script>

<style>
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
    background-color: rgb(0, 0, 0);
    width: 100%;
    text-align: start;
}
</style>