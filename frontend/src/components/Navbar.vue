<template>
    <nav class="bg-black text-white shadow-md top-0">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16 items-center py-12">
          <!-- Logo -->
          <div class="text-2xl font-bold text-amber-200 font-serif">WellCare Sytem</div>
  
          <!-- Desktop Menu -->
          <div class="hidden md:flex space-x-6 mt-0">
            <RouterLink to="/" class="hover:text-gray-300">Home</RouterLink>
            <RouterLink to="/programs" class="hover:text-gray-300">Programs</RouterLink>
            <RouterLink to="/clients" class="hover:text-gray-300">Clients</RouterLink>
             <RouterLink to="/enrollments" class="hover:text-gray-300">Enroll Clients</RouterLink>
              <button v-if="isAuthenticated" @click="logout" class="text-red-500 hover:text-red-700">Logout</button>
          </div>
  
          <!-- Mobile Menu Button -->
          <button @click="toggleMenu" class="md:hidden text-white focus:outline-none">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"
                 xmlns="http://www.w3.org/2000/svg">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M4 6h16M4 12h16m-7 6h7"/>
            </svg>
          </button>
        </div>
      </div>
  
      <!-- Mobile Menu -->
      <div v-if="isOpen" class="md:hidden bg-blue-200">
        <RouterLink to="/" class="block px-4 py-2 hover:bg-blue-500">Home</RouterLink>
        <RouterLink to="/softwaredata" class="block px-4 py-2 hover:bg-blue-500">   Programs</RouterLink>
        <RouterLink to="/hardwares" class="block px-4 py-2 hover:bg-blue-500">Clients</RouterLink>
        <RouterLink to="/programmings" class="block px-4 py-2 hover:bg-blue-500">Register Clients</RouterLink>
        <RouterLink to="/trendingtech" class="block px-4 py-2 hover:bg-blue-500">Enroll Clients</RouterLink>
         
         <button v-if="isAuthenticated" @click="logout" class="block w-full text-left px-4 py-2 text-red-500 hover:bg-red-100">Logout</button>
      </div>
    </nav>
  </template>
  <script>
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import apiClient from '../utils/axios'
  
  export default {
    setup() {
      const isOpen = ref(false)
      const isAuthenticated = ref(false)
      const router = useRouter()
  
      const checkAuth = () => {
        isAuthenticated.value = !!localStorage.getItem('token')
      }
  
      onMounted(() => {
        checkAuth()
      })
  
      const toggleMenu = () => {
        isOpen.value = !isOpen.value
      }
  
      const logout = async () => {
        try {
          await apiClient.post('logout/')
          localStorage.removeItem('token')
          isAuthenticated.value = false
          router.push('/login')
        } catch (error) {
          console.error('Logout failed', error)
        }
      }
  
      return {
        isOpen,
        toggleMenu,
        logout,
        isAuthenticated,
      }
    }
  }
  </script>
  