import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '@/Pages/Dashboard.vue';
import ProgramsData from '@/Pages/Programs/ProgramsData.vue';
import RegisterClients from '@/Pages/Clients/RegisterClients.vue';
import Profile from '@/Pages/Profile.vue';
import EnrollClientPrograms from '@/Pages/Clients/EnrollClientPrograms.vue';
  const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        { path: '/', name: 'home', component: Dashboard },
        { path: '/programs', name: 'programs', component: ProgramsData },
        { path: '/clients', name: 'clients', component: RegisterClients },
        { path: '/programmings', name: 'programmings', component: Dashboard },
        {
          path: '/profile/:id',
          name: 'client-profile',
          component: Profile,
          props: true,  
        },
         { path: '/enrollments', name: 'enrollments', component:EnrollClientPrograms },
         
         { path: '/dashboard', name: 'dashboard', component: Dashboard },
      ]
      });
    export default router;
