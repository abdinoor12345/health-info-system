<template>
    <div class="max-w-6xl mx-auto p-6 bg-gray-50 rounded-xl">
      <h2 class="text-3xl md:text-4xl font-extrabold text-center text-gray-800 mb-10 tracking-tight">
        Available Data
      </h2>
  
      <div v-if="loading" class="text-center text-gray-600">Loading program entries...</div>
      <div v-else-if="error" class="text-center text-red-500">{{ error }}</div>
      <div v-else-if="ProgramList.length === 0" class="text-center text-gray-500">No program entries found.</div>
  
      <div v-else class="overflow-x-auto bg-white rounded-lg shadow-lg">
        <table class="min-w-full table-auto">
          <thead>
            <tr class="bg-gray-100">
              <th class="py-3 px-6 text-left text-gray-800">Program Name</th>
              <th class="py-3 px-6 text-left text-gray-800">Description</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="program in ProgramList" :key="program.id" class="border-b hover:bg-gray-50">
              <td class="py-3 px-6">{{ program.title }}</td>
              <td class="py-3 px-6">{{ program.description.slice(0, 100) }}...</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const ProgramList = ref([])
  const loading = ref(true)
  const error = ref(null)
  
  const fetchprogram = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/health_programs/')
      ProgramList.value = response.data
    } catch (err) {
      error.value = 'Failed to load program entries. Please try again later.'
    } finally {
      loading.value = false
    }
  }
  
  onMounted(fetchprogram)
  </script>
  
  <style scoped>
  </style>
  