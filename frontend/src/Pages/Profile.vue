<template>
  <div class="client-profile">
    <h1 class="text-2xl font-bold mb-4">Client Profile</h1>

     <div v-if="loading" class="text-center">Loading...</div>
    <div v-if="error" class="text-red-500 text-center">{{ error }}</div>

     <div v-if="client" class="p-4 text-black mb-4 leading-4">
      <p class="text-blue-700 text-center mb-4 text-2xl font-bold leading-6">{{ client.first_name }} {{ client.last_name }}</p>
      
      <p class="text-black text-xl mb-5 font-bold">Gender: {{ client.gender }}</p>
      <p class="text-black text-xl mb-5 font-bold">Date of Birth: {{ client.date_of_birth }}</p>
      <p class="text-black text-xl mb-5 font-bold">Contact Number: {{ client.contact_number }}</p>
      <p class="text-black text-xl mb-5 font-bold">Email: {{ client.email }}</p>
      <p class="text-black text-xl mb-5 font-bold">Address: {{ client.address }}</p>

      <p class="text-black text-xl font-bold">Programs Enrolled:</p>
      <ul class="text-black text-lg mb-5">
        <li v-for="program in client.programs" :key="program.id">
          {{ program.name }}: {{ program.description }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  props: ['id'], 
  data() {
    return {
      client: null,
      loading: true,
      error: null,
    };
  },
  mounted() {
    this.fetchClientProfile();
  },
  methods: {
    async fetchClientProfile() {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/profile/${this.id}/`);
        if (!response.ok) {
          throw new Error('Failed to fetch client profile');
        }
        const data = await response.json();
        this.client = data.client;  
      } catch (error) {
        this.error = error.message;
        console.error(error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.client-profile {
  padding: 20px;
}

.client-profile h1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.client-profile .p-4 {
  font-size: 16px;
  line-height: 1.5;
}

.client-profile .text-red-500 {
  color: #f56565;
}

.client-profile .text-center {
  text-align: center;
}

.client-profile .text-black {
  color: #000;
}

.client-profile .text-blue-700 {
  color: #2b6cb0;
}

.client-profile .font-bold {
  font-weight: bold;
}

.client-profile .leading-relaxed {
  line-height: 2.75;
}
</style>
