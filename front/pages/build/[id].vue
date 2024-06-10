<template>
    <BuildError v-if="error"></BuildError>
    <div v-if="!error">
        {{ ids.id }}
    </div>
</template>

<script setup>
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
                    console.log(json)
                    if(json.detail){
                        this.error = true
                    console.log('xdddd')
        }})
        },
        decode_uri(){
            console.log(decodeURIComponent(escape(window.atob(this.ids.id))))
        }
    },
    beforeMount(){
        this.check_uri()
        this.decode_uri()
    }
}

</script>

<style>

</style>