<template>
  <div class="autonav">
    <div v-for="node in nodes">
      <auto-nav-node :node="node" :start-state="startState" :on-open="onOpen"></auto-nav-node>
    </div>
  </div>
</template>

<script setup lang="ts">
import { DirNavListing } from '@docdundee/nav';
import AutoNavNode from './AutoNavNode.vue';

defineProps({
  nodes: {
    type: Object as () => Array<DirNavListing>,
    required: true
  },
  startState: {
    type: String as () => "collapsed" | "all" | "one",
    default: "one"
  },
  onOpen: {
    type: Function,
    required: true
  }
})
</script>