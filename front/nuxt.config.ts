// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@formkit/auto-animate/nuxt', "@nuxt/image"],
  app: {
    head: {
      title: 'LOEbuilder'
    }
  }
})