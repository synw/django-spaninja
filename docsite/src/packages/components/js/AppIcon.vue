<template>
  <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" preserveAspectRatio="xMidYMid meet"
    :viewBox="icon.viewbox">
    <path fill="currentColor" :d="icon.path" />
  </svg>
</template>

<script setup lang="ts">
import { onBeforeMount, reactive } from "vue";

const props = defineProps({
  name: {
    type: String,
    required: true
  }
})

const icon = reactive<SvgIcon>({ path: "", viewbox: "" });

interface SvgIcon {
  viewbox: string;
  path: string;
}

function getIcon(name: string): SvgIcon {
  let icon: SvgIcon = { viewbox: "0 0 512 512", path: "" };
  switch (name) {
    case "play":
      icon.path = 'M444.4 235.236L132.275 49.449A24 24 0 0 0 96 70.072v364.142a24.017 24.017 0 0 0 35.907 20.839L444.03 276.7a24 24 0 0 0 .367-41.461ZM128 420.429V84.144l288.244 171.574Z';
      break;
    case "typescript":
      icon.path = 'M357.333 402c-16.933-1.555-38.666-4.833-59.67-27.772v47.19c38.587 25.082 104.951 20.478 128.087-9.668c13.75-17.917 19.417-41.917 9.237-69.099C411 294.333 354 291.333 337.424 260.822c-18.313-49.418 57.212-58.347 93.498-25.054v-44.36c-15.46-9.985-40.044-11.058-57.29-10.126c-45.511 2.457-76.094 28.901-75.638 68.293c-1.96 54.987 60.83 69.145 92.359 94.592c21.413 18.17 19.88 62.235-33.02 57.833zm-179.691 31.514V220.025h-68.778v-35.303h175.655v35.303h-68.921v213.489h-37.956zM480 32v448H32V32h448zm32-32H0v512h512V0z'
      break;
    case "clear":
      icon.path = 'M19 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2m0 16H5V5h14v14M17 8.4L13.4 12l3.6 3.6l-1.4 1.4l-3.6-3.6L8.4 17L7 15.6l3.6-3.6L7 8.4L8.4 7l3.6 3.6L15.6 7L17 8.4Z'
      icon.viewbox = '0 0 24 24'
      break;
    default:
      throw new Error(`Unknown icon ${name}`)
  }
  return icon
}

onBeforeMount(() => {
  const _ic = getIcon(props.name);
  icon.viewbox = _ic.viewbox;
  icon.path = _ic.path;
})
</script>