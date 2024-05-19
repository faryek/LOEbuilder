// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss',
    '@formkit/auto-animate/nuxt'
  ],
  app: {
    head: {
      title: 'LOEbuilder'
    }
  }
})
