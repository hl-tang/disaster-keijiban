<template>
  <div>
    <h1>IP 信息</h1>
    <p>IP 地址: {{ ip }}</p>
    <p>国家: {{ country }}</p>
    <p>地区: {{ region }}</p>
    <p>城市: {{ city }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// 定义 ref 变量来存储获取到的信息
const ip = ref('');
const country = ref('');
const region = ref('');
const city = ref('');

// 使用 fetch 获取数据并保存到变量中
fetch('https://ipinfo.io/json')
  .then(response => response.json())
  .then(data => {
    ip.value = data.ip;
    country.value = data.country;
    region.value = data.region;
    city.value = data.city;
  })
  .catch(error => console.error('Error fetching location data:', error));
</script>

<style scoped></style>