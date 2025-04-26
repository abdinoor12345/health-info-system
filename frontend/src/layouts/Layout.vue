<template>
    <div class="min-h-screen flex flex-col">
      <!-- Navbar -->
      <Navbar />
   <!-- Main Content -->
  <main class="flex-grow container mx-auto p-4  text-white">
     
    <slot />
    <!-- This renders the page content -->
  </main>
  
  <Foter />
  </div>
  </template>
  
  <script>
  import Navbar from '@/components/Navbar.vue'
  import Foter from '@/components/Footer.vue'
  
  export default {
    components: { Navbar, Foter },
  }
  </script>
  <style scoped>
  body{
    overflow-x:hidden;
  }
  .min-h-screen {
    display: flex;
    flex-direction: column;
  }
  .bg-gray-600 {
    background-color: #4b5563;
    color: white;
    overflow-x: scroll;
    display: flex;
    flex-direction: row;
    gap: 16px;
    margin-top: 24px;
  }
  
  p {
    margin: 0 16px;
    font-size: 18px;
  }
  
  /* Assigning different fonts */
  p:nth-child(1) { font-family: 'Roboto', sans-serif; }
  p:nth-child(2) { font-family: 'Lora', serif; }
  p:nth-child(3) { font-family: 'Montserrat', sans-serif; }
  
  </style>
  