import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import Simulation from "@/views/Simulation.vue";
import NotFound from "@/views/NotFound.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home,
    },
    {
        path: "/simulation",
        name: "Simulation",
        component: Simulation,
    },
    {
        path: '/:pathMatch(.*)*',
        component: NotFound,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
