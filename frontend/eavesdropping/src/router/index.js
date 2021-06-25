import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import Simulation from "@/views/Simulation.vue";
import Methods from "@/views/Methods.vue";
import Formalism from "@/views/Formalism.vue";
import Discussion from "@/views/Discussion.vue";
import Encryption from "@/views/Encryption.vue";
import NotFound from "@/views/NotFound.vue";
import References from "@/views/References.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/formalism",
    name: "Formalism",
    component: Formalism,
  },
  {
    path: "/encryption",
    name: "Encryption",
    component: Encryption,
  },
  {
    path: "/methods",
    name: "Methods",
    component: Methods,
  },
  {
    path: "/discussion",
    name: "Discussion",
    component: Discussion,
  },
  {
    path: "/simulation",
    name: "Simulation",
    component: Simulation,
  },
  {
    path: "/references",
    name: "References",
    component: References,
  },
  {
    path: "/:pathMatch(.*)*",
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(),
  base: "/eavesdropping-lamas/",
  routes,
});

export default router;
