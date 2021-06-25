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
        path: "/LAMAS/",
        name: "Home",
        component: Home,
    },
    {
        path: "/LAMAS/formalism",
        name: "Formalism",
        component: Formalism,
    },
    {
        path: "/LAMAS/encryption",
        name: "Encryption",
        component: Encryption,
    },
    {
        path: "/LAMAS/methods",
        name: "Methods",
        component: Methods,
    },
    {
        path: "/LAMAS/discussion",
        name: "Discussion",
        component: Discussion,
    },
    {
        path: "/LAMAS/simulation",
        name: "Simulation",
        component: Simulation,
    },
    {
        path: "/LAMAS/references",
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
    routes,
});

export default router;
