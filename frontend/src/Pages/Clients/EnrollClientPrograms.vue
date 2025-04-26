<template>
  <div class="p-6 bg-gray-50 min-h-screen">
    <h1 class="text-3xl font-bold mb-6 text-indigo-700">Enroll Clients to Programs</h1>

    <div v-if="loading" class="text-center text-gray-500">Loading clients and programs...</div>

    <div v-else>
      <div 
        v-for="client in clients" 
        :key="client.id" 
        class="mb-6 p-6 border rounded-lg bg-white shadow hover:shadow-md transition-shadow"
      >
        <div class="text-lg font-semibold text-gray-800">
          {{ client.first_name }} {{ client.last_name }}
        </div>

        <div class="mt-4 flex items-center">
          <label for="program-select" class="text-gray-600 mr-2">Select Program:</label>
          
          <select 
            v-model="selectedPrograms[client.id]" 
            :id="'program-select-' + client.id"
            class="border p-2 rounded text-gray-700 bg-gray-50 focus:ring-2 focus:ring-blue-300"
          >
            <option disabled value="" class="text-gray-400">-- Select Program --</option>
            <option 
              v-for="program in programs" 
              :key="program.id" 
              :value="program.id"
              class="text-gray-800"
            >
              {{ program.name }}
            </option>
          </select>

          <button 
            @click="enrollClient(client.id)" 
            class="ml-4 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
          >
            Enroll
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const clients = ref([]);
const programs = ref([]);
const selectedPrograms = ref({});
const loading = ref(true);

const fetchClientsAndPrograms = async () => {
  try {
    const [clientResponse, programResponse] = await Promise.all([
      axios.get('http://localhost:8000/api/clients/'),
      axios.get('http://localhost:8000/api/health_programs/')
    ]);
    clients.value = clientResponse.data;
    programs.value = programResponse.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    alert('Failed to load clients or programs.');
  } finally {
    loading.value = false;
  }
};

const enrollClient = async (clientId) => {
  const programId = selectedPrograms.value[clientId];

  if (!programId) {
    alert('Please select a program first.');
    return;
  }

  try {
    await axios.post('http://localhost:8000/api/enrollments/', {
      client: clientId,
      program: programId
    });
    alert('Client successfully enrolled to program!');
    selectedPrograms.value[clientId] = '';  
  } catch (error) {
    console.error('Error enrolling client:', error.response?.data || error.message);
    alert('Enrollment failed. Please try again.');
  }
};

onMounted(fetchClientsAndPrograms);
</script>
