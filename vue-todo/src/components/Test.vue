<script setup lang="ts">
import { getTodos } from '../apis/api'

getTodos().then(res => {
  console.log(res)
})
</script>

<template>
</template>

<style scoped></style>