<template>
  <AppHeader />

  <nav class="bg-red-700 text-white text-xl py-4">
    <ul class="flex justify-center space-x-8">
      <li>
        <router-link to="/" class="hover:underline">Home</router-link>
      </li>
      <!-- <li>
        <router-link to="/posts" class="hover:underline">投稿閲覧</router-link>
      </li>
      <li>
        <router-link to="/create" class="hover:underline">投稿作成</router-link>
      </li> -->
    </ul>
  </nav>

  <div class="container">

    <!-- メインコンテンツ -->
    <div class="main-content">
      <div class="page-header">
        <div class="page-title">災害情報共有掲示板</div>
      </div>
      <div class="board-list">
        <!-- 静的な方法
            <div v-for="board in boards" :key="board.id" class="board-item"  @click="navigateToPage(board.id)">
            {{ board.name }}-->

        <!--　動的に掲示板の名前を変更する-->
        <div v-for="disaster in disasters" :key="disaster.id" class="board-item" @click="navigateToPage(disaster)">
          {{ disaster.disaster_name }}
          <!-- {{disaster.id}} -->
        </div>

      </div>
    </div>
  </div>
</template>


<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import AppHeader from '../components/AppHeader.vue';

import { storeToRefs } from 'pinia'
import { useIpCityStore } from '../stores/ipCity'
const {ip, city} = storeToRefs(useIpCityStore());

import { useDisasterInfoStore } from '../stores/disasterInfo'
const {disaster_id, disaster_name, allow_areas} = storeToRefs(useDisasterInfoStore());

fetch('https://ipinfo.io/json')
  .then(response => response.json())
  .then(data => {
    ip.value = data.ip;
    // country.value = data.country;
    city.value = data.region; // Aichi是region，nagoya是city. 应该按照region来，但代码已经写了好多city了就将错就错
    // city.value = data.city;
  })
  .catch(error => console.error('Error fetching location data:', error));

const router = useRouter();


import axios from 'axios'
const disasters = ref([]);
axios.get('/api/disasters/')
  .then(res => {
    console.log(res.data)
    disasters.value = res.data
    console.log(disasters.value)
  })
  .catch((err) => {
    console.log(err)
  })


const navigateToPage = (disaster) => {
  disaster_id.value = disaster.id;
  disaster_name.value = disaster.disaster_name
  allow_areas.value = disaster.allow_areas
  router.push(`/search/${disaster.id}`);
};
</script>


<style scoped>
/* 全体レイアウト */
.container {
  display: flex;
  flex-direction: column;
  background-color: #f9fafb;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.login-button {
  padding: 10px 20px;
  background-color: #BF0000;
  /* 楽天の赤色 */
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.login-button:hover {
  background-color: #a00000;
}

.login-button:focus {
  outline: none;
}


/* メインコンテンツ */
.main-content {
  flex-grow: 1;
  margin-left: 20px;
}

.main-content h1 {
  text-align: left;
  font-size: 24px;
  color: #333;
  background-color: #ffffff;
  padding: 10px;
  border-radius: 10px;
}

.board-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* ボタンを中央に寄せる */
  gap: 20px;
  margin-top: 20px;
}

/* 各掲示板リンクのスタイル */
.board-item {
  width: 50%;
  /* 画面の半分の長さ */
  background-color: white;
  /* 楽天の赤色 */
  padding: 20px;
  border-radius: 15px;
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  border: 2px solid #BF0000;
  ;
  color: black;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}

.board-item:hover {
  transform: scale(1.05);
  cursor: pointer;
}


.page-title {
  font-size: 36px;
  font-weight: bold;
  color: #333;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
  font-family: 'Arial Black', sans-serif;
}

/* フォーム全体 */
.form-container {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.page-header {
  width: 100%;
  text-align: left;
  margin-bottom: 20px;
}


/* レスポンシブ対応 */
@media screen and (max-width: 768px) {
  .container {
    flex-direction: column;
  }

  .main-content {
    margin-left: 0;
  }

  .board-list {
    gap: 10px;
  }

  .board-item {
    width: 80%;
    /* モバイル向けで画面幅を縮小 */
  }

  .header {
    top: 15px;
    right: 15px;
  }

}
</style>