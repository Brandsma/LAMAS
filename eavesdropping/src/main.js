import { createApp } from 'vue'
import App from './App.vue'
import "./styles/globals.scss"

import router from "./router/index.js"

createApp(App).use(router).mount('#app')
