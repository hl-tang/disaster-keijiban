<template>
  <AppHeader />
  <!-- <div class="ml-4 text-xl">{{ disaster_name }} 投稿できる地方:{{ allow_areas }}</div> -->

  <div class="ml-1 text-xl bg-gray-100 p-4 rounded-lg shadow">
    <span class="font-semibold text-gray-700">{{ disaster_name }}</span> 
    
    <span class="text-gray-600 ml-3">投稿できる地方: {{ formattedAreas }}</span>
  </div>

  <nav class="bg-red-700 text-white text-xl py-4">
    <ul class="flex justify-center space-x-8">
      <li>
        <router-link to="/" class="hover:underline">Home</router-link>
      </li>
      <li>
        <!-- <router-link to="/search" class="hover:underline">投稿閲覧</router-link> -->
        <router-link :to="{name: 'Search', params: {id: disaster_id}}" class="hover:underline">投稿閲覧</router-link>
      </li>
      <li>
        <router-link to="/postform" class="hover:underline">投稿作成</router-link>
      </li>
    </ul>
  </nav>


  <div class="mt-8 p-4 max-w-md mx-auto bg-white border border-gray-300 rounded-lg shadow-lg">
    <h2 class="text-2xl font-bold text-gray-900 mb-4">投稿を作成</h2>
    
    <!-- 标题输入框 -->
    <div class="mb-4">
      <label for="title" class="block text-gray-700 font-medium mb-1">タイトル</label>
      <input
        v-model="title"
        type="text"
        id="title"
        placeholder="タイトルを入力"
        class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:border-red-500"
      />
    </div>
    
    <!-- 内容输入框 -->
    <div class="mb-4">
      <label for="content" class="block text-gray-700 font-medium mb-1">内容</label>
      <textarea
        v-model="content"
        id="content"
        rows="4"
        placeholder="内容を入力"
        class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:border-red-500"
      ></textarea>
    </div>
    
    <!-- 确定按钮 -->
    <button
      @click="create_post"
      class="w-full bg-red-600 text-white font-bold py-2 px-4 rounded-lg hover:bg-red-700 transition-all duration-300"
    >
      投稿する
    </button>
  </div>


</template>


<script setup>
import AppHeader from '../components/AppHeader.vue';

import { storeToRefs } from 'pinia'
import { useIpCityStore } from '../stores/ipCity'
const {ip, city} = storeToRefs(useIpCityStore());

import { useDisasterInfoStore } from '../stores/disasterInfo'
const {disaster_id, disaster_name, allow_areas} = storeToRefs(useDisasterInfoStore());

import { useIsLoggedInStore } from '../stores/isLoggedIn'
const { isLoggedIn, username, userid } = storeToRefs(useIsLoggedInStore())

import { ref, computed } from 'vue';
// 英日翻译字典
const areaMap = {
  Hokkaido: "北海道",
  Aomori: "青森県",
  Iwate: "岩手県",
  Miyagi: "宮城県",
  Akita: "秋田県",
  Yamagata: "山形県",
  Fukushima: "福島県",
  Ibaraki: "茨城県",
  Tochigi: "栃木県",
  Gunma: "群馬県",
  Saitama: "埼玉県",
  Chiba: "千葉県",
  Tokyo: "東京",
  Kanagawa: "神奈川県",
  Niigata: "新潟県",
  Toyama: "富山県",
  Ishikawa: "石川県",
  Fukui: "福井県",
  Yamanashi: "山梨県",
  Nagano: "長野県",
  Gifu: "岐阜県",
  Shizuoka: "静岡県",
  Aichi: "愛知県",
  Mie: "三重県",
  Shiga: "滋賀県",
  Kyoto: "京都府",
  Osaka: "大阪府",
  Hyogo: "兵庫県",
  Nara: "奈良県",
  Wakayama: "和歌山県",
  Tottori: "鳥取県",
  Shimane: "島根県",
  Okayama: "岡山県",
  Hiroshima: "広島県",
  Yamaguchi: "山口県",
  Tokushima: "徳島県",
  Kagawa: "香川県",
  Ehime: "愛媛県",
  Kochi: "高知県",
  Fukuoka: "福岡県",
  Saga: "佐賀県",
  Nagasaki: "長崎県",
  Kumamoto: "熊本県",
  Oita: "大分県",
  Miyazaki: "宮崎県",
  Kagoshima: "鹿児島県",
  Okinawa: "沖縄県"
};

// 格式化后的区域
const formattedAreas = computed(() => {
  return allow_areas.value
    .map(area => areaMap[area] || area) // 将英文地名转为日文
    .join('、'); // 使用日文顿号“、”连接
});


import axios from 'axios';

// 输入框的ref
const title = ref('');
const content = ref('');

// 创建投稿函数
const create_post = async () => {
  if (!isLoggedIn.value) {
    alert("please login");
    return;
  }

  // 检查 city 是否在 allow_areas 中
  if (!allow_areas.value.includes(city.value)) {
    alert("IP not allowed");
    return;
  }

  const postData = {
    title: title.value,
    content: content.value,
    disaster_id: disaster_id.value,
    user_name: username.value
  };

  try {
    const response = await axios.post('/api/post_create/', postData);
    console.log('投稿成功:', response.data);
    alert("投稿成功")
    // 在这里可以添加成功后的处理逻辑，例如清空表单或显示提示
  } catch (error) {
    console.error('投稿失败:', error);
    alert("投稿失败")
    // 在这里可以添加失败后的处理逻辑，例如显示错误提示
  }
};

</script>


<style scoped></style>