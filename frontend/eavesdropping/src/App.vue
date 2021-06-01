<template>
  <div class="navbar topBottomBordersIn">
    <router-link
      :class="{ button: true, activebutton: $route.name === 'Home' }"
      :to="{ name: 'Home' }"
      >Home</router-link
    >
    |
    <router-link
      :class="{ button: true, activebutton: $route.name === 'Simulation' }"
      :to="{ name: 'Simulation' }"
      >Simulation</router-link
    >
  </div>
  <div class="view">
    <transition name="fade" mode="out-in">
      <router-view />
    </transition>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

html,
body {
  width: 100%;
  height: 100%;
  margin: 0px;
  padding: 0px;
  overflow-x: hidden;
}

.blog {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
  flex-direction: column;
  padding: 3em 6em;
  background-color: white;
}

.image {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  max-width: 100%;
  height: auto;
}

.navbar {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin: 0 auto;
  padding: 0.5em 0.5em;
  width: 100%;
  height: 15%;
  background: #3f51b5;
}

.navbar a {
  text-decoration: none;
  font: 20px Raleway;
  margin: 0px 10px;
  padding: 10px 10px;
  position: relative;
  z-index: 0;
  cursor: pointer;
}

div.topBottomBordersIn a:before,
div.topBottomBordersIn a:after {
  position: absolute;
  left: 0px;
  width: 100%;
  height: 2px;
  background: #fff;
  content: "";
  opacity: 0;
  transition: all 0.3s;
}

div.topBottomBordersIn a:before {
  top: 0px;
  transform: translateY(-10px);
}

div.topBottomBordersIn a:after {
  bottom: 0px;
  transform: translateY(10px);
}

div.topBottomBordersIn a:hover:before,
div.topBottomBordersIn a:hover:after {
  opacity: 1;
  transform: translateY(0px);
}

.button {
  color: white;
}

.activebutton {
  color: red;
}
</style>
