<template>
  <div class="static-code">
    <pre><code v-html="parsedCode" style="white-space: pre"></code></pre>
  </div>
</template>

<script setup lang="ts">
import _hljs from 'highlight.js/lib/core';

const props = defineProps({
  code: {
    type: String,
    required: true
  },
  lang: {
    type: String,
    required: true
  },
  hljs: {
    type: Object as () => typeof _hljs,
    required: true
  },
});

const parsedCode = props.hljs.highlight(props.code, { language: props.lang }).value;
</script>