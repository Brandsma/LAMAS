import { createWebHistory, createRouter } from "vue-router";

const routes = [
    {
      path: "/home",
      name: "home",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/Home.vue"),
      meta: {
        visible: true
      }
    },
    {
      path: "/simulation",
      name: "simulation",
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/Simulation.vue"),
      meta: {
        visible: true
      }
    },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;