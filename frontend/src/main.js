import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";

const app = createApp(App);

import router from "./router";
app.use(router);

import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
app.use(pinia);

import axios from "axios";
// axios.defaults.baseURL = "http://127.0.0.1:8000"; //浏览器刷新后cookie丢失,但localhost却可以
axios.defaults.baseURL = "http://localhost:8000";

axios.defaults.withCredentials = true;

import VueCookies from "vue-cookies";
app.use(VueCookies);

app.mount("#app");
