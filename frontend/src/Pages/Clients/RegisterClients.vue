<template>
  <div class="max-w-6xl mx-auto p-6 bg-gray-50 rounded-xl">
    <h2 class="text-3xl md:text-4xl font-extrabold text-center text-gray-800 mb-10 tracking-tight">
      Registered Clients
    </h2>

     <div class="mb-6 flex items-center justify-between">
      <form @submit.prevent="searchClients" class="flex items-center space-x-2 w-full max-w-md">
        <div class="relative flex-grow">
          <input
            v-model="searchQuery"
            class="w-full pl-10 pr-4 text-black py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            type="text"
            placeholder="Search by name, phone, email..."
          >
          <div class="absolute left-3 top-2.5 text-gray-400">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
          </div>
        </div>
        <button 
          type="submit" 
          class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded transition-colors"
        >
          Search
        </button>
      </form>

      <button 
        @click="showForm = !showForm" 
        class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded transition-colors"
      >
        {{ showForm ? 'Cancel' : 'Register Client' }}
      </button>
    </div>

     <div v-if="successMessage" class="text-center text-green-500 mb-4">
      {{ successMessage }}
    </div>

     <div v-if="loading" class="text-center text-gray-600">Loading client entries...</div>
    <div v-else-if="error" class="text-center text-red-500">{{ error }}</div>

    <div v-else>
       <div v-if="showForm" class="bg-white p-6 rounded-lg shadow-md mb-8">
        <form @submit.prevent="createClient" class="space-y-4">
          <div>
            <label class="block text-gray-700 mb-1">First Name</label>
            <input v-model="newClient.first_name" type="text" class="w-full border rounded p-2 border-amber-200" required />
          </div>
          <div>
            <label class="block text-gray-700 mb-1">Last Name</label>
            <input v-model="newClient.last_name" type="text" class="w-full border rounded p-2 border-amber-200" required />
          </div>
          <div>
            <label class="block text-gray-700 mb-1">Gender</label>
            <select v-model="newClient.gender" class="w-full border rounded p-2 border-amber-200 text-black" required>
              <option value="">Select Gender</option>
              <option value="M">Male</option>
              <option value="F">Female</option>
              <option value="O">Other</option>
            </select>
          </div>
          <div>
            <label class="block text-gray-700 mb-1">Date of Birth</label>
            <input v-model="newClient.date_of_birth" type="date" class="w-full border rounded border-amber-200 text-black  p-2" required />
          </div>
          <div>
            <label class="block text-gray-700 mb-1">Contact Number</label>
            <input v-model="newClient.contact_number" type="text" class="w-full border border-amber-200 rounded p-2" required />
          </div>
          <div>
            <label class="block text-gray-700 mb-1">Email</label>
            <input v-model="newClient.email" type="email" class="w-full border border-amber-100 rounded p-2" />
          </div>
          <div>
            <label class="block text-gray-700 mb-1">Address</label>
            <textarea v-model="newClient.address" class="w-full border rounded p-2 border-amber-100"></textarea>
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
              <th class="py-3 px-6 text-left text-gray-800">Name</th>
              <th class="py-3 px-6 text-left text-gray-800">Gender</th>
              <th class="py-3 px-6 text-left text-gray-800">Phone</th>
              <th class="py-3 px-6 text-left text-gray-800">Email</th>
              <th class="py-3 px-6 text-left text-gray-800">Address</th>
              <th class="py-3 px-6 text-left text-gray-800">Date of Birth</th>
              <th  class="py-3 px-6 text-left text-gray-800">Profile</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="client in ClientList" :key="client.id" class="border-b hover:bg-gray-50">
              <td class="py-3 px-6 font-bold text-gray-700">
                {{ client.first_name }} {{ client.last_name }}
              </td>
              <td class="py-3 px-6 text-gray-500">{{ client.gender }}</td>
              <td class="py-3 px-6 text-gray-500">{{ client.contact_number }}</td>
              <td class="py-3 px-6 text-gray-500">{{ client.email }}</td>
              <td class="py-3 px-6 text-gray-500">{{ client.address }}</td>
              <td class="py-3 px-6 text-gray-500">{{ client.date_of_birth }}</td>
              <td class="py-3 px-6 text-gray-500">
                <router-link class="text-black bg-green-400 p-2 mt-6 rounded" :to="`/profile/${client.id}`">
                  <i class="fas fa-user-circle text-2xl text-gray-600"></i> <!-- Icon instead of text -->
                </router-link>
              </td>
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
import apiClient from '@/utils/axios'

const ClientList = ref([])
const loading = ref(true)
const error = ref(null)
const successMessage = ref(null)  
const showForm = ref(false)
const searchQuery = ref('')

const newClient = ref({
  first_name: '',
  last_name: '',
  gender: '',
  date_of_birth: '',
  contact_number: '',
  email: '',
  address: ''
})

const searchClients = async () => {
  try {
    loading.value = true
    error.value = null
    successMessage.value = null  

    const response = await axios.get('http://localhost:8000/api/clients/search/', {
      params: {
        search: searchQuery.value  
      }
    })
    
    ClientList.value = response.data || []
  } catch (err) {
    error.value = 'Failed to search clients. Please try again later.'
    console.error('Search error:', err)
  } finally {
    loading.value = false
  }
}


const fetchClients = async () => {
  try {
    loading.value = true
    const response = await axios.get('http://localhost:8000/api/clients/')
    ClientList.value = response.data.results || response.data
  } catch (err) {
    error.value = 'Failed to load client entries. Please try again later.'
    console.error('Fetch error:', err)
  } finally {
    loading.value = false
  }
}

const createClient = async () => {
  try {
    loading.value = true
    await axios.post('http://localhost:8000/api/clients/', newClient.value)
    successMessage.value = 'Client successfully registered!' // Set success message

    Object.assign(newClient.value, {
      first_name: '',
      last_name: '',
      gender: '',
      date_of_birth: '',
      contact_number: '',
      email: '',
      address: ''
    })
    showForm.value = false
    await fetchClients()
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to register client. Please check fields and try again.'
    console.error('Create error:', err)
  } finally {
    loading.value = false
  }
}

onMounted(fetchClients)
</script>
<style scoped></style>