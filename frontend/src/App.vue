<template>
  <div class="min-h-screen bg-black text-gray-100">
    <!-- Header -->
    <Header />

    <!-- Main Content -->
    <main class="max-w-6xl mx-auto px-4 py-12">
      <!-- Hero Section -->
      <HeroSection />

      <!-- Search Section -->
      <HashSearchForm :loading="loading" :error="error" @search="handleSearch" />

      <!-- Results Section -->
      <SearchResults :loading="loading" :results="results" />
    </main>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import Header from './components/Header.vue'
import HeroSection from './components/HeroSection.vue'
import HashSearchForm from './components/HashSearchForm.vue'
import SearchResults from './components/SearchResults.vue'
import Footer from './components/Footer.vue'

interface Match {
  source: string
  downloadable?: boolean
  filename?: string
  detectionRate?: string
  url?: string
}

interface SearchResultsData {
  hash: string
  matches?: Match[]
}

const loading = ref(false)
const results = ref<SearchResultsData | null>(null)
const error = ref('')

// Search function
const handleSearch = async (hash: string, type: string) => {
  if (!hash) {
    error.value = ''
    results.value = null
    return
  }

  if (!type) {
    error.value = 'Invalid hash format. Please enter a valid MD5, SHA1, or SHA256 hash'
    return
  }

  loading.value = true
  error.value = ''
  results.value = null

  try {
    const response = await fetch(`/api/lookup`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        hash: hash.toLowerCase(),
        type: type,
      }),
    })

    if (!response.ok) {
      throw new Error(`API error: ${response.status}`)
    }

    const data = await response.json()
    results.value = data
  } catch (err) {
    error.value = `Failed to query API: ${err instanceof Error ? err.message : 'Unknown error'}`
    console.error('Search error:', err)
  } finally {
    loading.value = false
  }
}
</script>

<style>
/* Global CSS Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
  background-color: #000000;
  color: #f3f4f6;
  font-family:
    -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell',
    'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  min-height: 100vh;
  background-color: #000000;
}

/* Main app layout */
.min-h-screen {
  min-height: 100vh;
}

.bg-black {
  background-color: #000000;
}

.text-gray-100 {
  color: #f3f4f6;
}

/* Layout utilities */
.max-w-6xl {
  max-width: 72rem;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-12 {
  padding-top: 3rem;
  padding-bottom: 3rem;
}

.mt-20 {
  margin-top: 5rem;
}

/* Custom scrollbar for dark theme */
:deep(*) {
  scrollbar-width: thin;
  scrollbar-color: #374151 #111827;
}

:deep(*::-webkit-scrollbar) {
  width: 8px;
  height: 8px;
}

:deep(*::-webkit-scrollbar-track) {
  background: #111827;
}

:deep(*::-webkit-scrollbar-thumb) {
  background: #374151;
  border-radius: 4px;
}

:deep(*::-webkit-scrollbar-thumb:hover) {
  background: #4b5563;
}
</style>
