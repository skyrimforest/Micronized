import './assets/main.css'

// 引入pinia
import { createPinia } from 'pinia'

// 引入router
import router from './router'

// 引入element-plus
import ElementPlus from 'element-plus'
import { ElMessage } from 'element-plus';
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

import { createApp } from 'vue'
import App from './App.vue'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ElementPlus)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.mount('#app')
