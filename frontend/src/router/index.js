import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '@/Pages/Dashboard.vue';
import ProgramsData from '@/Pages/Programs/ProgramsData.vue';
 const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        { path: '/', name: 'home', component: Dashboard },
        { path: '/programs', name: 'softwaredata', component: ProgramsData },
        { path: '/hardwares', name: 'hardwares', component: Dashboard },
        { path: '/programmings', name: 'programmings', component: Dashboard },
        { path: '/trendingtech', name: 'trendingtech', component: Dashboard },
        { path: '/explore', name: 'explore', component: Dashboard },
        { path: '/login', name: 'login', component: Dashboard },
        { path: '/dashboard', name: 'dashboard', component: Dashboard },
      ]
      });
    export default router;
