<template>
  <div class="bg-white m-2 p-6 rounded-lg shadow-md border border-gray-400 hover:border-red-600 hover:shadow-lg transition-all duration-300 max-w-md mx-auto">
    <!-- 投稿タイトル -->
    <h2 class="text-3xl font-bold text-red-600 mb-4">
      {{ title }}
    </h2>

    <!-- 投稿内容 -->
    <div class="text-gray-800 text-lg mb-6">
      {{ content }}
    </div>

    <!-- 投稿者 -->
    <div class="text-sm text-gray-500 text-right">
      投稿者: {{ user_name }}
    </div>
  </div>
</template>

<script setup>
import { toRefs, ref } from 'vue';

import { defineProps } from 'vue';

// 定义组件的 props
const props = defineProps({
  title: String,
  content: String,
  user_name: String
});

// 投稿データのサンプル
// const title = ref('掲示板アプリの新機能について');
// const content = ref('掲示板アプリに新しい機能を追加しました。詳細は次のリリースで発表されます。');
// const user_name = ref('John Doe');
</script>

<style scoped>
</style>
