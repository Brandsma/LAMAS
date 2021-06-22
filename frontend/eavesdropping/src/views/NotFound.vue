<template>
  <div
    style="
      display: flex;
      padding-top: 100px;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    "
  >
    <div>
      <h1>Error 404 - Page not found</h1>
    </div>
    <div>
      <h2>
        Perhaps you are looking for
        <router-link :to="{ name: 'Home' }">home?</router-link>
      </h2>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style scoped></style>
