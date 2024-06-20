Планнер билда для воображаемой ARPG игры
Для установки установки зависимость для сервера прописать команду

pip install -r requirements.txt

для заполнения таблиц базовыми значениями прописать в консоль разработчика(нужно находится в папке back)

py seed.py

Для запуска сервера прописать в консоль(нужно находится в папке back)

uvicorn main:app --reload

Для установки модулей, необходимых для Фронтенда, вевести команды в консоль

npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
npm install @formkit/auto-animate
npm i floating-vue
npx nuxi@latest module add image

После добавить в файл nuxt.config.ts строку

modules: ['@nuxtjs/tailwindcss', '@formkit/auto-animate/nuxt', "@nuxt/image", 'floating-vue/nuxt'],

*Пример итогового файла*

*// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss', '@formkit/auto-animate/nuxt', "@nuxt/image", 'floating-vue/nuxt'],
  app: {
    head: {
      title: 'LOEbuilder',
      charset: 'utf-8',
    }
  }
})*

После установки модулей, для запуска сервера, пропписать в консоль(нужно находится в папке front)

npm run dev


