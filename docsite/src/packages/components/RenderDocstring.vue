<template>
  <div class="docstring prosed">
    <h1 v-if="title">{{ title }}</h1>
    <slot></slot>
    <p v-html="docstring.description"></p>
    <p class="codedef not-prose">
    <pre class="w-max"><code v-html="parsedCode" style="white-space: pre"></code></pre>
    </p>
    <p v-if="docstring.long_description" v-html="docstring.long_description"> </p>
    <template v-if="Object.keys(docstring.params).length > 0">
      <h3>Parameters</h3>
      <ul class="params-list">
        <li v-for="param in Object.keys(docstring.params)">
          <kbd class="param-name" v-html="param"></kbd> <span class="hljs-built_in"
            v-html="docstring.params[param].type"></span>:
          <span v-html="docstring.params[param].description"></span>
        </li>
      </ul>
    </template>
    <template v-if="docstring?.returns?.type">
      <h3>Returns</h3>
      <p class="hljs-built_in" v-html="docstring.returns.type"></p>
    </template>
    <div class="mt-5" v-if="Object.keys(docstring.raises).length > 0">
      <h3>Raises</h3>
      <div class="mt-3" v-for="raise in docstring.raises">
        <span class="hljs-built_in" v-html="raise.type"></span>:
        <span v-html="raise.description"></span>
      </div>
    </div>
    <div class="mt-5" v-if="docstring.example">
      <div class="mt-3" v-if="docstring.example.is_executable">
        <h2>Executable example</h2>
        <slot name="executable-example" :code="docstring.example.code"></slot>
      </div>
      <div class="mt-3" v-else>
        <h2>Example</h2>
        <static-code-block :hljs="hljs" :lang="lang" class="w-full static-code not-prose"
          :code="docstring.example.code"></static-code-block>
      </div>
    </div>
    <div class="mt-5" v-if="docstring.extra_examples">
      <div v-for="example in docstring.extra_examples">
        <div class="mt-3" v-if="example.is_executable">
          <h2>Executable example</h2>
          <slot name="extra-executable-example" :code="example.code"></slot>
        </div>
        <div class="mt-3" v-else>
          <h2>Example</h2>
          <static-code-block :hljs="hljs" :lang="lang" class="w-full static-code not-prose"
            :code="example.code"></static-code-block>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watchEffect } from 'vue';
import _hljs from 'highlight.js/lib/core';
import { ParsedDocstring } from '@docdundee/nav';
import StaticCodeBlock from './StaticCodeBlock.vue';

const props = defineProps({
  docstring: {
    type: Object as () => ParsedDocstring,
    required: true
  },
  title: {
    type: String,
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

const parsedCode = ref("");

function load() {
  parsedCode.value = props.hljs.highlight(props.docstring.funcdef, { language: props.lang }).value;
  //console.log(JSON.stringify(props.docstring, null, "  "))
}

watchEffect(() => load())
</script>
