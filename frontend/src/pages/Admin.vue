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
              <input
                type="checkbox"
                :value="prefecture"
                @change="togglePrefecture(prefecture)"
                class="form-checkbox text-blue-600"
              />
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
const prefectureMap = {
  '北海道': 'Hokkaido',
  '青森県': 'Aomori',
  '岩手県': 'Iwate',
  '宮城県': 'Miyagi',
  '秋田県': 'Akita',
  '山形県': 'Yamagata',
  '福島県': 'Fukushima',
  '茨城県': 'Ibaraki',
  '栃木県': 'Tochigi',
  '群馬県': 'Gunma',
  '埼玉県': 'Saitama',
  '千葉県': 'Chiba',
  '東京都': 'Tokyo',
  '神奈川県': 'Kanagawa',
  '新潟県': 'Niigata',
  '富山県': 'Toyama',
  '石川県': 'Ishikawa',
  '福井県': 'Fukui',
  '山梨県': 'Yamanashi',
  '長野県': 'Nagano',
  '岐阜県': 'Gifu',
  '静岡県': 'Shizuoka',
  '愛知県': 'Aichi',
  '三重県': 'Mie',
  '滋賀県': 'Shiga',
  '京都府': 'Kyoto',
  '大阪府': 'Osaka',
  '兵庫県': 'Hyogo',
  '奈良県': 'Nara',
  '和歌山県': 'Wakayama',
  '鳥取県': 'Tottori',
  '島根県': 'Shimane',
  '岡山県': 'Okayama',
  '広島県': 'Hiroshima',
  '山口県': 'Yamaguchi',
  '徳島県': 'Tokushima',
  '香川県': 'Kagawa',
  '愛媛県': 'Ehime',
  '高知県': 'Kochi',
  '福岡県': 'Fukuoka',
  '佐賀県': 'Saga',
  '長崎県': 'Nagasaki',
  '熊本県': 'Kumamoto',
  '大分県': 'Oita',
  '宮崎県': 'Miyazaki',
  '鹿児島県': 'Kagoshima',
  '沖縄県': 'Okinawa'
};

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

const togglePrefecture = (prefecture) => {
  const englishName = prefectureMap[prefecture];
  const index = allow_areas.value.indexOf(englishName);
  
  if (index > -1) {
    // もし英語名が既に配列に存在すれば、取り除く
    allow_areas.value.splice(index, 1);
  } else {
    // それ以外の場合は追加
    allow_areas.value.push(englishName);
  }
};
import axios from 'axios'

// const submitForm = () => {
//   const formData = new FormData();
//   formData.append('disaster_name', title.value);
//   formData.append('allow_areas', JSON.stringify(allow_areas.value));

//   /* fetch('/api/disaster_create/', {
//     method: 'POST',
//     body: formData,
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       console.log('Success:', data);
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     }); */

//     axios.post('/api/disaster_create/', formData)
//     .then((response) => {
//       console.log('Success:', response.data);
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     });
// };

const submitForm = () => {
  const requestData = {
    disaster_name: title.value,  // 假设 `title` 是你表单中用于输入灾害名称的变量
    allow_areas: allow_areas.value,  // `allow_areas` 是包含选中区域的数组
  };

  axios.post('/api/disaster_create/', requestData, {
    headers: {
      'Content-Type': 'application/json',  // 明确指定发送 JSON 格式
    }
  })
  .then((response) => {
    console.log('Success:', response.data);
    alert("success")
  })
  .catch((error) => {
    console.error('Error:', error.response ? error.response.data : error.message);
  });
};

const cancelForm = () => {
  title.value = '';
  allow_areas.value = [];
  router.push('/'); // ホームにリダイレクト
};

console.log(allow_areas.value);
</script>

<style scoped>
/* Tailwind CSS が既にスタイルをカバーしているため、特別なカスタムCSSは不要です */
</style>
