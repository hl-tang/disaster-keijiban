<template>
  <header class="flex justify-between items-center p-4 bg-white shadow-md">
    <!-- 左侧文字 -->
    <div class="text-3xl font-bold text-gray-800">掲示板アプリ</div>

    <!-- 右侧按钮 -->
    <div v-if="!isLoggedIn">
      <router-link to="/loginregister">
        <button
          class="bg-red-700 text-white font-bold py-3 px-6 rounded-full hover:bg-red-400 transition-colors duration-300">
          ログイン
        </button>
      </router-link>
    </div>

    <div v-else class="flex justify-between items-center space-x-4">
      <!-- 左边部分 -->
      <div class="flex flex-col">
        <div class="text-xl">ようこそ, {{ username }}様</div>
        <div class="text-sm text-gray-500">IP: {{ ip }} {{ city }}</div>
      </div>

      <!-- 右边按钮 -->
      <button @click="logout"
        class="bg-red-700 text-white font-bold py-3 px-6 rounded-full hover:bg-red-600 transition-colors duration-300">
        ログアウト
      </button>
    </div>

  </header>
</template>

<script setup>
import { ref } from "vue";

import AccountIcon from "vue-material-design-icons/Account.vue";
import LogoutVariantIcon from "vue-material-design-icons/LogoutVariant.vue";

import { storeToRefs } from 'pinia'
import { useIsLoggedInStore } from '../stores/isLoggedIn'
const { isLoggedIn, username, userid } = storeToRefs(useIsLoggedInStore())

import { useIpCityStore } from '../stores/ipCity'
const { ip, city } = storeToRefs(useIpCityStore());

import axios from 'axios';
const logout = async () => {
  axios.get('/api/logout/')
    .then(res => {
      isLoggedIn.value = false;
      username.value = "none"
      userid.value = -1
      console.log("Response Data:", res.data);
    })
  router.push('/loginregister');
};

console.log(isLoggedIn.value);
</script>

<style scoped>
/* 根据需要添加其他样式 */
</style>
