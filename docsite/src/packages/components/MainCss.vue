<template>
</template>

<style lang="sass">
.prosed:not(.not-prose)
  @apply prose dark:prose-invert max-w-none prose-h1:txt-light prose-h2:txt-light prose-h3:txt-light prose-h2:mt-3
  @apply max-w-[52rem] xl:min-w-[52rem]
.md-content.prosed:not(.not-prose)
  & p
    @apply text-justify
  & pre
    @apply bg-gray-100 text-black dark:bg-black dark:text-neutral-200 p-3 rounded-md overflow-x-auto border border-gray-200 dark:border-neutral-800
em
  @apply font-semibold txt-light not-italic
.codedef
  @apply ml-8
kbd
  @apply px-2 py-1 font-semibold text-gray-800 bg-gray-100 border border-gray-200 rounded-lg dark:bg-gray-600 dark:text-gray-100 dark:border-gray-500
.static-code:not(.raw)
  @apply p-3 bg-gray-100 dark:bg-black dark:text-neutral-200 rounded-md overflow-x-auto border border-gray-200 dark:border-neutral-800
.hljs-built_in
  & a, a:visited
    color: #b75501 !important
// nav
.nav-item-hspace
  @apply ml-8
.nav-panel
  & .navnode-0
    > .navnode-header
      @apply bg-neutral-200 text-neutral-600 border-neutral-400 border rounded-t-md py-3 pl-5
      @apply dark:text-neutral-200 dark:bg-neutral-800 dark:border-neutral-600
    > .navnode-header.navheader-opened
      @apply rounded-b-none border-b-neutral-300
      @apply dark:border-b-neutral-700
    > .navnode-header.navheader-closed
      @apply rounded-b-md
    > .navnode-content
      @apply bg-neutral-100 text-neutral-600 rounded-b-md border border-t-0 border-neutral-400
      @apply dark:text-neutral-200 dark:bg-neutral-700 dark:border-neutral-600
    > .navnode-content.navnode-opened
      @apply pb-2
    > .navnode-content.navnode-closed
      @apply border-y-0
  & .navnode-item, .navnode-header.navnode-opened
    @apply hover:bg-neutral-200 hover:rounded-none focus:bg-neutral-300 w-full text-left
    @apply dark:focus:bg-neutral-800 dark:hover:bg-neutral-600
.navnode
  & .navnode-header
    @apply flex items-center btn w-full
  & .navnode-title
    @apply ml-2
  & .navnode-closed
    max-height: 0
    overflow-y: hidden
    transition-property: max-height
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1)
    transition-duration: 300ms
  & .navnode-opened
    @apply duration-100
    max-height: 1000px
    transition-property: max-height
    transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1)
    transition-duration: 300ms
  & .navnode-item
    @apply focus:ring-0 btn truncate
  & .navnode-content
    @apply flex flex-col
.autonav
  @apply flex flex-col space-y-1
.flat-navnode
  & .nn-title
    @apply px-1 text-left truncate cursor-pointer btn
.autoindex
  @apply w-max
  & .inode
    @apply p-3 border rounded-md bord-light lighter
// docstrings
.docstring
  & .params-list
    @apply space-y-2
  & .param-name
    @apply mr-1 font-bold
// generic
.igrid
    @apply grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-3 m-auto
.mt-3
  margin-top: 0.75rem
.mt-5
  margin-top: 1.25rem
.w-max 
  width: max-content
.w-full
  width: 100%
.pycode-block
  & .code-editor
    @apply max-w-[52rem] xl:min-w-[52rem]
</style>