<template>
  <AppHeader />

  <div class="ml-1 text-xl bg-gray-100 p-4 rounded-lg shadow">
    <span class="font-semibold text-gray-700">{{ disaster_name }}</span>

  </div>

  <nav class="bg-red-700 text-white text-xl py-4">
    <ul class="flex justify-center space-x-8">
      <li>
        <router-link to="/" class="hover:underline">Home</router-link>
      </li>
      <li>
        <!-- <router-link to="/search" class="hover:underline">投稿閲覧</router-link> -->
        <div class="hover:underline">投稿閲覧</div>
      </li>
      <li>
        <router-link to="/postform" class="hover:underline">投稿作成</router-link>
      </li>
    </ul>
  </nav>


  <div class="flex items-center justify-center p-4">
    <!-- 搜索框 -->
    <input v-model="keyword" type="text" placeholder="検索キーワードを入力"
      class="w-full max-w-md p-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500" />

    <!-- 搜索按钮 -->
    <button @click="fetchPosts"
      class="ml-4 bg-blue-600 text-white font-bold py-2 px-6 rounded-lg hover:bg-blue-700 transition-all duration-300">
      検索
    </button>
  </div>

  <!-- <Post /> -->
  <div v-for="post in posts" :key="post.id">
    <Post :title="post.title" :content="post.content" :user_name="post.user_name" />
  </div>


</template>


<script setup>
import AppHeader from '../components/AppHeader.vue';
import Post from '../components/Post.vue';

import { storeToRefs } from 'pinia'
import { useIpCityStore } from '../stores/ipCity'
const { ip, city } = storeToRefs(useIpCityStore());

import { useDisasterInfoStore } from '../stores/disasterInfo'
const { disaster_id, disaster_name, allow_areas } = storeToRefs(useDisasterInfoStore());


import { ref, onMounted } from 'vue';
import axios from 'axios';

// 定义数据
const posts = ref([]);
const keyword = ref("");

// 获取数据 一个请求函数把有无关键词检索的两个case都覆盖了
const fetchPosts = async () => {
  try {
    const response = await axios.get('/api/post_search/', {
      params: {
        disaster_id: disaster_id.value,
        keyword: keyword.value
      }
    });
    posts.value = response.data;
  } catch (error) {
    console.error('Error fetching posts:', error);
  }
};

// 在组件挂载后调用获取数据的函数
onMounted(fetchPosts);

</script>


<style scoped></style>