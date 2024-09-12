import { defineStore } from "pinia";
import { ref } from "vue";

export const useIpCityStore = defineStore(
  "ip-city",
  () => {
    const ip = ref("");
    const city = ref("");

    return {
      ip,
      city,
    };
  },
  {
    persist: true,
  }
);
