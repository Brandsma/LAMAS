<template>
  <span ref="mathJaxEl" v-html="formula" class="e-mathjax"></span>
</template>

<style>
</style>

<script type="text/javascript">
export default {
  props: ["formula"],
};
</script>