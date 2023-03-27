<template>
  <div v-if="isReady">
    <slot name="docstring" :data="page.data"></slot>
    <render-md :hljs="hljs" v-if="page.data.docstring?.extra_md" :source="page.data.docstring.extra_md.footer"
      :class="page.data.hasDocstring ? 'mt-5' : ''"></render-md>
    <render-md :hljs="hljs" v-if="page.data.hasMarkdown" :source="page.data.markdown"></render-md>
    <div v-if="page.data.autoIndex" class="w-full">
      <div>
        <div class="prosed">
          <h1>{{ page.data.title }}</h1>
        </div>
        <auto-index :node="page.data.node" :on-open="onOpen"></auto-index>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { watchEffect, ref, reactive } from 'vue';
import _hljs from 'highlight.js/lib/core';
import { RouteDataPayload, useNav } from '@docdundee/nav';
import RenderMd from './markdown/RenderMd.vue';
import AutoIndex from '../widgets/AutoIndex.vue';

const props = defineProps({
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
  onOpen: {
    type: Function,
    required: true
  },
  baseTitle: {
    type: String,
  },
  handlePageTitle: {
    type: Boolean,
    default: true
  }
});

const page = reactive<{ data: RouteDataPayload }>({ data: {} as RouteDataPayload });
const isReady = ref(false);

watchEffect(async () => {
  isReady.value = false;
  page.data = await props.nav.loadFromRoutePath(props.url);
  isReady.value = true;
  if (props.handlePageTitle) {
    if (props.baseTitle) {
      document.title = `${props.baseTitle} - ${page.data.title}`
    } else {
      document.title = `${page.data.title}`
    }
  }
})
</script>