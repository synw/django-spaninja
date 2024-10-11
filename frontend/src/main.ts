import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import PrimeVue from 'primevue/config';
import ToastService from 'primevue/toastservice';
import ConfirmationService from 'primevue/confirmationservice';
import Aura from '@primevue/themes/aura';
import './assets/index.css';
import 'primeicons/primeicons.css';

const app = createApp(App);

app.use(router).use(PrimeVue, {
    theme: {
        preset: Aura,
        options: {
            cssLayer: {
                name: 'primevue',
                order: 'tailwind-base, primevue, tailwind-utilities'
            }
        }
    }
}).use(ToastService).use(ConfirmationService).mount('#app');
