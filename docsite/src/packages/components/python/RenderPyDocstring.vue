<template>
  <render-docstring :docstring="docstring" :hljs="hljs" :lang="lang" :title="title">
    <template #executable-example="slotProps">
      <py-code-block class="not-prose" :controls="true" id="example_0" :py="py" :code="slotProps.code"
        :theme="darkMode ? 'dark' : 'light'">
      </py-code-block>
    </template>
    <template #extra-executable-example="slotProps">
      <py-code-block class="not-prose" :controls="true" :id="'example_' + Date()" :py="py" :code="slotProps.code"
        :theme="darkMode ? 'dark' : 'light'">
      </py-code-block>
    </template>
  </render-docstring>
</template>

<script setup lang="ts">
import RenderDocstring from '../RenderDocstring.vue';
import _hljs from 'highlight.js/lib/core';
import { ParsedDocstring } from '@docdundee/nav';
import { usePython } from "usepython";
import { PyCodeBlock } from 'vuepython';

defineProps({
  docstring: {
    type: Object as () => ParsedDocstring,
    required: true
  },
  title: {
    type: String,
    required: true
  },
  py: {
    type: Object as () => ReturnType<typeof usePython>,
    required: true
  },
  darkMode: {
    type: Boolean,
    default: false
  },
  hljs: {
    type: Object as () => typeof _hljs,
    required: true
  },
  lang: {
    type: String,
    required: true
  },
});
</script>