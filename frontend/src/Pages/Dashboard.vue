<template>
  <div class="flex items-center justify-center   bg-gray-100 mt-10">
    <div class="text-center p-8 bg-white shadow-xl rounded-lg w-full max-w-8xl">
      
      <h1 class="text-4xl font-bold text-blue-600 mb-4">
        Welcome to Our Health Management System
      </h1>

      <p class="text-lg text-gray-700 mb-6">
        A comprehensive solution to manage health programs, enroll clients, and deliver quality healthcare services.
      </p>

      <div class="border-t pt-6">
        <h2 class="text-2xl font-semibold text-indigo-600 mb-2">Key Features</h2>
        <ul class="text-gray-700 list-disc list-inside space-y-2">
          <li>Effortless Client Enrollment into Health Programs</li>
          <li>Track Client Health Records and Progress</li>
          <li>Manage Multiple Health Programs Efficiently</li>
          <li>Secure and Easy-to-Use Platform</li>
        </ul>
      </div>

      <div class="mt-8">
        <p class="text-gray-600 mb-4">Please log in or register to start managing your health programs.</p>
        <div class="flex justify-center gap-4">
          <router-link to="/login">
            <button class="bg-blue-500 text-white px-6 py-2 rounded-md hover:bg-blue-600 transition duration-300">
              Login
            </button>
          </router-link>
          <router-link to="/register">
            <button class="bg-green-500 text-white px-6 py-2 rounded-md hover:bg-green-600 transition duration-300">
              Register
            </button>
          </router-link>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
</style>
