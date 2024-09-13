import { defineStore } from "pinia";
import { ref } from "vue";

export const useDisasterInfoStore = defineStore(
  "disaster-info",
  () => {
    const disaster_id = ref();
    const disaster_name = ref("");
    const allow_areas = ref([]);

    return {
      disaster_id,
      disaster_name,
      allow_areas,
    };
  },
  {
    persist: true,
  }
);
