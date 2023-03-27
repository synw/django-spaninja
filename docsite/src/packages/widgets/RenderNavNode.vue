<template>
  <div class="flat-navnode">
    <template v-if="node.content.length > 0">
      <div v-for="doc in node.content">
        <button v-if="doc.type != 'directory'" class="nn-title" v-html="doc.title" @click="onClick(doc.url)"></button>
      </div>
    </template>
    <template v-if="node.docstrings.length > 0">
      <div v-for="ds in node.docstrings">
        <button class="nn-title" v-html="ds.title" @click="onClick(node.url + '/' + ds.name)"></button>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
import { DirNavListing } from '@docdundee/nav';

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

function onClick(url: string) {
  props.onOpen(url)
}
</script>