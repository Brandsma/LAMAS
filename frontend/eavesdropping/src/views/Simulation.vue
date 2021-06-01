<template>
  <div class="blog">
    <p>This is the simulation screen</p>
    <div
      style="
        width: 100%;
        background-color: whitesmoke;
        display: flex;
        justify-content: center;
        padding: 3em;
      "
    >
      *SIMULATION*
      <div class="move obj-hooked">Move me hooked!</div>
      <div class="move obj-straight">Move me straight!</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Simulation",
};
</script>

<style scoped>
.move {
  position: absolute;
  animation: move 4000ms;
}
.obj-straight {
  /* Straight path */
  offset-path: path("M153.398514,240Q146.828314,240,320,240");
}

.obj-hooked {
  /* Hooked path */
  offset-path: path("M159.030113,240L320,240L320,361.360970");
}

@keyframes move {
  100% {
    offset-distance: 100%;
  }
}
</style>
