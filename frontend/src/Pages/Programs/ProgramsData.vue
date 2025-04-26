<template>
    <div class="max-w-6xl mx-auto p-6 bg-gray-50 rounded-xl">
      <h2 class="text-3xl md:text-4xl font-extrabold text-center text-gray-800 mb-10 tracking-tight">
        Available Programs
      </h2>
  
      <div v-if="loading" class="text-center text-gray-600">Loading program entries...</div>
      <div v-else-if="error" class="text-center text-red-500">{{ error }}</div>
      <div v-else>
        <div class="ml-6 mb-6">
          <button @click="showForm = !showForm" class="bg-green-600 text-white p-2 rounded">
            {{ showForm ? 'Cancel' : 'Create Program' }}
          </button>
        </div>
  
        <div v-if="showForm" class="bg-white p-6 rounded-lg shadow-md mb-8">
          <form @submit.prevent="createProgram" class="space-y-4">
            <div>
              <label class="block text-gray-700 mb-1">Program Name</label>
              <input v-model="newProgram.name" type="text" class="w-full border rounded p-2 text-gray-300" required />
            </div>
            <div>
              <label class="block text-gray-700 mb-1">Description</label>
              <textarea v-model="newProgram.description" class="w-full border rounded p-2 text-gray-500" rows="4" required></textarea>
            </div>
            <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
              Submit
            </button>
          </form>
        </div>
  
        <div class="overflow-x-auto bg-white rounded-lg shadow-lg">
          <table class="min-w-full table-auto">
            <thead>
              <tr class="bg-gray-100">
                <th class="py-3 px-6 text-left text-gray-800">Program Name</th>
                <th class="py-3 px-6 text-left text-gray-800">Description</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="program in ProgramList" :key="program.id" class="border-b hover:bg-gray-50">
                <td class="py-3 px-6 text-gray-600 font-bold">{{ program.name }}</td>
                <td class="py-3 px-6 text-gray-500">{{ program.description.slice(0, 200) }}...</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const ProgramList = ref([])
  const loading = ref(true)
  const error = ref(null)
  const showForm = ref(false)
  
  const newProgram = ref({
    name: '',
    description: ''
  })
  
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
  
  const createProgram = async () => {
    try {
      await axios.post('http://localhost:8000/api/health_programs/', newProgram.value)
      newProgram.value.name = ''
      newProgram.value.description = ''
      showForm.value = false
      fetchprogram()
    } catch (err) {
      error.value = 'Failed to create program. Please try again.'
    }
  }
  
  onMounted(fetchprogram)
  </script>
  
  <style scoped>
  </style>
  