<template>
  <div class="pycode-block">
    <div class="code-editor not-prose">
      <code-editor :code="props.code" lang="typescript" @edit="codeChange($event)" :hljs="hljs"></code-editor>
    </div>
    <button class="border code-exec-btn btn neuro focus:ring-0" :class="!isExecuting ? 'cursor-pointer' : 'cursor-wait'"
      @click="runCode()">
      <template v-if="!isExecuting">
        <app-icon name="play" class="inline-block text-xl txt-success"></app-icon>
      </template>
      <template v-else>
        <app-icon name="typescript" class="inline-block text-xl txt-danger"></app-icon>
      </template>
      &nbsp;Execute
    </button>
    <button class="ml-2 border code-exec-btn btn neuro focus:ring-0 txt-light" v-if="!isExecuting && result.length > 0"
      @click="result = ''">
      <app-icon name="clear" class="inline-block text-xl"></app-icon>&nbsp;Clear
    </button>
    <div class="p-3 mt-5 rounded-md w-max not-prose" v-if="result.length > 0">
      <div v-html="result"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { CodeEditor } from "vuecodit";
import AppIcon from "./AppIcon.vue";
import "vuecodit/style.css";
import _hljs from 'highlight.js/lib/core';

const props = defineProps({
  code: {
    type: String,
    required: true
  },
  hljs: {
    type: Object as () => typeof _hljs,
    required: true
  },
  onRun: {
    type: Function,
    required: true
  }
});

let editedCode = ref("");
const result = ref("");
const isExecuting = ref(false);

function codeChange(e: string) {
  // update the code
  editedCode.value = e;
}
async function runCode() {
  // execute the code
  isExecuting.value = true;
  result.value = props.onRun(editedCode.value);
  isExecuting.value = false;
}
</script>