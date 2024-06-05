<template>
    <BuildError v-if="error"></BuildError>
    <div v-if="!error">

    </div>
</template>

<script setup>
const {id} = useRoute().params
</script>

<script>
export default {
    data() {
        return {
            ids: useRoute().params,
            error: false
            
        }
    },
    methods:{
        check_uri(){
            let credetentials = {
                name: this.encoded,
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
                    console.log('xdddd')
        }})
        }
    }
}

</script>

<style>

</style>