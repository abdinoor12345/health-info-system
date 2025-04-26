<template>
    <div class="flex items-center justify-center  bg-gray-100">
      <div class="text-center p-8 bg-white shadow-lg rounded-lg w-full  lg:w-full">
        <h1 class="text-4xl font-bold text-blue-600">Welcome to Our Health Management System</h1>
        <p class="text-lg text-gray-700 mt-4">A comprehensive solution to manage health programs, clients, and services effectively.</p>
        <p class="text-gray-600 mt-6">Please log in or register to get started with managing health programs.</p>
        <div class="mt-6">
          <router-link to="/login">
            <button class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600 transition duration-300">Login</button>
          </router-link>
          <router-link to="/register" class="ml-4">
            <button class="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-600 transition duration-300">Register</button>
          </router-link>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
   }
  </script>
  
  <style scoped>
   </style>
  