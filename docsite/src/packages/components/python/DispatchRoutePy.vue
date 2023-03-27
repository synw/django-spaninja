<template>
  <dispatch-route :nav="nav" :hljs="hljs" :url="url" :on-open="onOpen">
    <template #docstring="slotProps">
      <render-py-docstring lang="python" :hljs="hljs" :py="py" v-if="slotProps.data.hasDocstring === true" class="w-full"
        :docstring="slotProps.data.docstring" :title="slotProps.data.name">
        <template v-if="slotProps.data.docstring.extra_md?.header">
          <render-md :hljs="hljs" :source="slotProps.data.docstring.extra_md.header"
            :class="slotProps.data.hasDocstring ? 'mb-3' : ''"></render-md>
        </template>
      </render-py-docstring>
    </template>
  </dispatch-route>
</template>

<script setup lang="ts">
import _hljs from 'highlight.js/lib/core';
import { useNav } from '@docdundee/nav';
import { usePython } from "usepython";
import RenderPyDocstring from './RenderPyDocstring.vue';
import RenderMd from '../markdown/RenderMd.vue';
import DispatchRoute from '../DispatchRoute.vue';

defineProps({
  nav: {
    type: Object as () => ReturnType<typeof useNav>,
    required: true
  },
  url: {
    type: String,
    required: true
  },
  hljs: {
    type: Object as () => typeof _hljs,
    required: true
  },
  py: {
    type: Object as () => ReturnType<typeof usePython>,
    required: true
  },
  onOpen: {
    type: Function,
    required: true
  },
});
</script>