<template>
  <div class="autoindex">
    <div class="icontent igrid">
      <render-nav-node v-if="renderNodeContent" :node="node" :on-open="onOpen" class="inode"></render-nav-node>
      <auto-nav-node v-if="node.docstrings.length > 0" :node="node" :on-open="onOpen" start-state="all"
        class="inode"></auto-nav-node>
      <div v-for="child in node.children" class="inode">
        <auto-nav-node :node="child" :on-open="onOpen" start-state="all"></auto-nav-node>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { DirNavListing } from '@docdundee/nav';
import AutoNavNode from "./AutoNavNode.vue"
import RenderNavNode from './RenderNavNode.vue';

const props = defineProps({
  node: {
    type: Object as () => DirNavListing,
    required: true
  },
  onOpen: {
    type: Function,
    required: true
  }
});

const renderNodeContent = ref(false);

onBeforeMount(() => {
  for (const n of props.node.content) {
    if (n.type != "directory") {
      renderNodeContent.value = true;
      break
    }
  }
})
</script>