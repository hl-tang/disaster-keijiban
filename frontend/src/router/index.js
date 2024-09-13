import { createRouter, createWebHistory } from "vue-router";

import Home from "../pages/Home.vue";
import LoginRegister from "../pages/LoginRegister.vue";
import ShowIP from "../pages/ShowIP.vue";
import Admin from "../pages/Admin.vue";
import Search from "../pages/Search.vue";
import PostForm from "../pages/PostForm.vue";
// import Play from "../pages/Play.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/loginregister",
    name: "LoginRegister",
    component: LoginRegister,
  },
  {
    path: "/showip",
    name: "ShowIP",
    component: ShowIP,
  },
  {
    path: "/admin",
    name: "Admin",
    component: Admin,
  },
  // {
  //   path: "/search",
  //   name: "Search",
  //   component: Search,
  // },
  {
    path: "/search/:id",
    name: "Search",
    component: Search,
  },
  {
    path: "/postform",
    name: "PostForm",
    component: PostForm,
  },
  // {
  //   path: "/play",
  //   component: Play,
  // },
];

const router = createRouter({
  // history: createWebHistory(process.env.BASE_URL),
  // vite不用process.env
  // 报错看developer tool的Console的error
  // https://vitejs.dev/guide/env-and-mode.html 写法看文档
  // 其实createWebHistory() 小括号里空着也行
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
