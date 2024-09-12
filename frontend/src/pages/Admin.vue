<template>
  <!-- ヘッダーのテンプレここから -->
  <AppHeader />
  <!-- ヘッダーのテンプレートはここまで -->

  <div class="bg-gray-100 p-8 rounded-lg shadow-md">
    <div class="mb-6">
      <h2 class="text-4xl font-extrabold text-gray-800">管理者ページ(新規掲示板追加)</h2>
    </div>

    <div class="mb-4">
      <label for="title" class="block text-lg font-semibold text-gray-700 mb-2">掲示板名</label>
      <input type="text" id="title" v-model="title" class="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
    </div>  

    <div class="mb-4">
      <label for="title" class="block text-lg font-semibold text-gray-700 mb-2">行方不明ページの閲覧可能な都道府県</label>
      <div v-for="(area, index) in areas" :key="index" class="mb-4">
        <div class="font-bold text-lg text-gray-800 mb-2">{{ area.name }}</div>
        <div class="grid grid-cols-3 gap-2">
          <div v-for="prefecture in area.prefectures" :key="prefecture">
            <label class="inline-flex items-center">
              <input type="checkbox" :value="prefecture" v-model="allow_areas" class="form-checkbox text-blue-600" />
              <span class="ml-2">{{ prefecture }}</span>
            </label>
          </div>
        </div>
      </div>
    </div>

    <div class="flex gap-4">
      <button @click="submitForm" class="bg-red-600 text-white font-bold py-2 px-6 rounded hover:bg-red-700">
        掲示板作成
      </button>
      <button @click="cancelForm" class="bg-white text-red-600 border border-red-600 font-bold py-2 px-6 rounded hover:bg-gray-200">
        キャンセル
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import AppHeader from '../components/AppHeader.vue';

const router = useRouter();

const title = ref('');
const allow_areas = ref([]);
const areas = ref([
  {
    name: '北海道・東北地方',
    prefectures: ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県']
  },
  {
    name: '関東地方',
    prefectures: ['茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県']
  },
  {
    name: '中部地方',
    prefectures: ['新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県']
  },
  {
    name: '近畿地方',
    prefectures: ['三重県', '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県']
  },
  {
    name: '中国・四国地方',
    prefectures: ['鳥取県', '島根県', '岡山県', '広島県', '山口県', '徳島県', '香川県', '愛媛県', '高知県']
  },
  {
    name: '九州・沖縄地方',
    prefectures: ['福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']
  }
]);

const submitForm = () => {
  const formData = new FormData();
  formData.append('title', title.value);
  formData.append('allow_areas', JSON.stringify(allow_areas.value));

  fetch('/api/post', {
    method: 'POST',
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

const cancelForm = () => {
  title.value = '';
  allow_areas.value = [];
  router.push('/'); // ホームにリダイレクト
};
</script>

<style scoped>
</style>
