<template>
  <div>
    <header class="header navbar-fixed-top">
      <!-- Navbar -->
      <nav class="navbar" role="navigation">
        <div class="container">
          <!-- Brand and toggle get grouped for better mobile display -->
          <div class="menu-container js_nav-item"></div>
          <!-- HAMBURGER MENU ICON -->
          <input
            class="toggle-button"
            type="checkbox"
            name="toggle"
            id="toggle"
          />
          <label for="navbar-toggle"></label>
          <!-- Collect the nav links, forms, and other content for toggling -->
          <div class="menu-mobile">
            <div class="collapse navbar-collapse nav-collapse">
              <div class="menu-container">
                <ul class="nav navbar-nav container-right">
                  <li class="js_nav-item nav-item">
                    <router-link
                      :class="{
                        'nav-item-child': true,
                        activebutton: $route.name === 'Home',
                      }"
                      :to="{ name: 'Home' }"
                      >Home</router-link
                    >
                  </li>
                  <li class="js_nav-item nav-item">
                    <router-link
                      :class="{
                        'nav-item-child': true,
                        activebutton: $route.name === 'Encryption',
                      }"
                      :to="{ name: 'Encryption' }"
                      >Encryption</router-link
                    >
                  </li>
                  <li class="js_nav-item nav-item">
                    <router-link
                      :class="{
                        'nav-item-child': true,
                        activebutton: $route.name === 'Methods',
                      }"
                      :to="{ name: 'Methods' }"
                      >Methods</router-link
                    >
                  </li>
                  <li class="js_nav-item nav-item">
                    <router-link
                      :class="{
                        'nav-item-child': true,
                        activebutton: $route.name === 'Formalism',
                      }"
                      :to="{ name: 'Formalism' }"
                      >Formalism</router-link
                    >
                  </li>
                  <li class="js_nav-item nav-item">
                    <router-link
                      :class="{
                        'nav-item-child': true,
                        activebutton: $route.name === 'Simulation',
                      }"
                      :to="{ name: 'Simulation' }"
                      >Simulation</router-link
                    >
                  </li>
                  <li class="js_nav-item nav-item">
                    <router-link
                      :class="{
                        'nav-item-child': true,
                        activebutton: $route.name === 'Discussion',
                      }"
                      :to="{ name: 'Discussion' }"
                      >Discussion</router-link
                    >
                  </li>
                  <li class="js_nav-item nav-item">
                    <router-link
                      :class="{
                        'nav-item-child': true,
                        activebutton: $route.name === 'References',
                      }"
                      :to="{ name: 'References' }"
                      >References</router-link
                    >
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </header>
    <div class="view">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="in-out">
          <component :is="Component"></component>
        </transition>
      </router-view>
      <!-- <transition name="fade" mode="out-in">
        <router-view></router-view>
      </transition> -->
    </div>
    <img src="./assets/img/incognito_logo.png" class="bottom-right" />
  </div>
</template>

<script>
export default {
  name: "App",
  mounted() {
    let mathjaxScript = document.createElement("script");
    mathjaxScript.setAttribute(
      "src",
      "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
    );
    mathjaxScript.setAttribute("id", "MathJax-script");
    mathjaxScript.async = true;
    document.head.appendChild(mathjaxScript);

    window.MathJax = {
      tex: {
        inlineMath: [
          ["$", "$"],
          ["\\(", "\\)"],
        ],
      },
      svg: {
        fontCache: "global",
      },
    };
  },
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
  line-height: 1.5em;
}

h1 {
  margin: 0.5em;
}
h2 {
  margin: 1.5em;
}
h3 {
  margin: 1em;
}
h4 {
  margin: 1em;
}

it {
  font-style: italic;
}

.blog {
  display: flex;
  width: 100%;
  padding-top: 100px;
  justify-content: center;
  align-items: center;
  flex: 1;
  flex-direction: column;
  background-color: white;
}

.blog > p {
  width: 60%;
  padding: 0.5em 6em;
}
.blog > ul {
  width: 60%;
  padding: 1em 9em;
}
.blog > ul > li {
  width: 60%;
  /* padding: 1em 9em; */
  margin-bottom: 0.5em;
}
.blog > ol {
  width: 60%;
  padding: 1em 7em;
}

.method-img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  max-width: 100%;
  height: auto;
  padding: 1em;
}

.img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  max-width: 100%;
  height: auto;
  -webkit-transition: all 0.2s ease-in;
  -moz-transition: all 0.2s ease-in;
  -ms-transition: all 0.2s ease-in;
  -o-transition: all 0.2s ease-in;
  transition: all 0.2s ease-in;
}

.img:hover {
  -webkit-transition: all 0.3s ease-in;
  -moz-transition: all 0.3s ease-in;
  -ms-transition: all 0.3s ease-in;
  -o-transition: all 0.3s ease-in;
  transition: all 0.3s ease-in;
  opacity: 1;
  transform: scale(1.3);
  -ms-transform: scale(1.3); /* IE 9 */
  -webkit-transform: scale(1.3); /* Safari and Chrome */
}

.img:active {
  -webkit-transition: all 0.3s ease-in;
  -moz-transition: all 0.3s ease-in;
  -ms-transition: all 0.3s ease-in;
  -o-transition: all 0.3s ease-in;
  transition: all 0.3s ease-in;
  opacity: 1;
  transform: scale(1.3);
  -ms-transform: scale(1.3); /* IE 9 */
  -webkit-transform: scale(1.3); /* Safari and Chrome */
}

.bottom-right {
  position: fixed;
  width: 3%;
  height: auto;
  bottom: 5px;
  left: 5px;
  transition: width 100ms ease-out 100ms;
  -webkit-animation-duration: 5s;
  animation-duration: 5s;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}

.bottom-right:hover {
  width: 4%;
}

/* Header fixed and background colors */

.header {
  position: fixed;
  top: 0px;
  max-height: 100px;
  z-index: 999;
  width: 100%;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  opacity: 1;
}

/* UL element Navigation Main Menu */

.navbar-collapse {
  max-height: 100%;
  padding-left: 0;
  padding-right: 0;
  transition-duration: 0.3s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.7, 1, 0.7, 1);
}

.header .navbar {
  margin-bottom: 0;
  background-color: #003366;
  border-radius: 0px;
  transition-duration: 0.3s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.7, 1, 0.7, 1);
}

.header .navbar-nav {
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
}

.header .navbar {
  margin-bottom: 0;
  background-color: #1a1a44;
  border-bottom: 3px #ae952e solid;
  transition-duration: 0.3s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.7, 1, 0.7, 1);
  position: relative;
  min-height: 100px;
  margin-bottom: 20px;
}

.navbar-nav {
  padding-right: 30px;
  display: flex;
}

/* Menu LI items and children */

.navbar-nav {
  list-style: none;
  margin-top: 20px;
  padding-right: 20px;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-content: center;
}

li.nav-item {
  /* position: relative; */
  font-size: 1em;
  font-weight: bold;
  float: left;
  height: 50px;

  /* padding-left: 30px; */
}

a.nav-item-child {
  font-size: 1em;
  font-family: "Oswald", sans-serif !important;
  color: #fff;
  line-height: 25px;
  transition-duration: 0.3s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.7, 1, 0.7, 1);
}

.navbar-nav > li.nav-item > a:hover {
  margin-bottom: 10px;
  border-bottom: 2px solid #ae952e;
  padding-bottom: 3px;
  color: #ccc;
}

header .nav-item-child:focus,
.header .nav-item-child:hover {
  background: inherit;
}

/* MAX-WIDTH 767px */
@media (max-width: 767px) {
  .header .menu-container {
    padding-left: 15px;
    padding-right: 15px;
    margin-left: 0;
    margin-right: 0;
  }

  .header .navbar > .container,
  .header .navbar > .container > .nav-collapse {
    padding-left: 0;
    padding-right: 0;
    margin-left: 0;
    margin-right: 0;
  }

  .header .navbar > .container {
    width: auto;
  }
}

.header .nav-item-hover:after,
.link:after,
.work .work-overlay:before {
  content: " ";
}

.header .navbar-toggle {
  width: 45px;
  height: 35px;
  border: none;
  margin: 35px 0;
  position: relative;
  float: right;
  padding: 9px 10px;
  margin-top: 31px;
  margin-right: 35px;
  margin-bottom: 8px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 4px;
}

.header .navbar-toggle .toggle-icon {
  position: relative;
  width: 21px;
  height: 1px;
  display: inline-block;
  background: #fff;
  transition-duration: 0.3s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.7, 1, 0.7, 1);
}

.header .navbar-toggle .toggle-icon:after,
.header .navbar-toggle .toggle-icon:before {
  position: absolute;
  left: 0;
  background: #fff;
  content: " ";
}

.header .navbar-toggle .toggle-icon:before {
  width: 10px;
  height: 1px;
  bottom: 10px;
  -webkit-transform: rotate(0);
  -moz-transform: rotate(0);
  transform: rotate(0);
  transition-duration: 0.3s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.7, 1, 0.7, 1);
}

.header .navbar-toggle .toggle-icon:after {
  width: 16px;
  height: 1px;
  top: -5px;
  -webkit-transform: rotate(0);
  -moz-transform: rotate(0);
  transform: rotate(0);
  transition-duration: 0.3s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.7, 1, 0.7, 1);
}

.header .navbar-toggle:hover .toggle-icon {
  background: #ae952e;
  transition-duration: 0.3s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.7, 1, 0.7, 1);
}

.header .navbar-toggle:hover .toggle-icon:after,
.header .navbar-toggle:hover .toggle-icon:before {
  width: 21px;
  height: 1px;
  background: #ae952e;
  transition-duration: 0.3s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.7, 1, 0.7, 1);
}

.header .header .logo-img-main,
.header .nav-item.active .nav-item-hover:after,
.header .nav-item:hover .nav-item-hover:after {
  transition-duration: 0.4s;
  transition-property: all;
  transition-timing-function: cubic-bezier(0.7, 1, 0.7, 1);
}

.header .navbar-toggle:hover .toggle-icon.is-clicked {
  background: rgba(81, 87, 105, 0);
}

/* MIN-WIDTH 768px */
@media (min-width: 768px) {
  .navbar-toggle {
    display: none;
  }
  .toggle-button {
    visibility: hidden;
  }
}

/* MAX-WIDTH 991px */
@media (max-width: 991px) {
  .header .navbar-nav {
    margin: 0;
    float: none;
    flex-direction: column;
  }

  .header .navbar-nav .nav-item {
    float: none;
  }

  .header .menu-container:after,
  .header .menu-container:before {
    content: " ";
    display: table;
  }

  .header .menu-container:after {
    clear: both;
  }

  .header .logo .logo-img-main {
    display: none;
  }

  .header .logo .logo-img-active {
    display: inline-block;
  }

  .header .nav-item-child {
    line-height: 1.4;
    padding: 12px 12px 12px 15px;
  }

  .header .nav-item-hover:after {
    position: absolute;
    top: 19px;
  }

  /*======= TOGGLE MENU ======*/

  #toggle,
  #toggle + label {
    display: inherit;
  }

  #toggle {
    width: 45px;
    height: 40px;
    opacity: 0;
    border: none;
    margin: 35px 0;
    position: absolute;
    top: 0px;
    right: 0px;
    z-index: 1000;
    float: right;
    padding: 9px 10px;
    margin-top: 31px;
    margin-right: 35px;
    margin-bottom: 8px;
    background-color: transparent;
    background-image: none;
    border: 1px solid transparent;
    border-radius: 4px;
    cursor: pointer;
  }

  .menu-mobile {
    padding-top: 90px;
    text-align: center;
    background: #1a1a44;
    color: #fff;
    width: 100%;
    height: 0px;
    overflow: hidden;
    transition: height 300ms cubic-bezier(0.17, 0.04, 0.03, 0.94);
  }

  #toggle:checked ~ .menu-mobile {
    height: 350px;
  }

  #toggle + label {
    position: absolute;
    top: 27px;
    right: 50px;
    border: none;
    color: #ffffff;
    background-color: transparent;
    background-image: none;
    border: 1px solid transparent;
    border-radius: 4px;
  }

  #toggle + label:after {
    content: "\2630";
    font-size: 1.7em;
  }

  #toggle:hover + label {
    color: #ae952e;
  }

  #toggle:checked ~ .message {
    height: 150px;
  }

  #toggle:checked + label:after {
    content: "\2573";
    font-size: 1.4em;
  }
}

/* MIN-WIDTH 992px */
@media (min-width: 992px) {
  .header .navbar-nav-right {
    float: right;
  }
}
</style>
