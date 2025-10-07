<template>
  <div class="min-h-screen bg-black text-gray-100">
    <!-- Header -->
    <header class="border-b border-gray-800 bg-black/50 backdrop-blur-sm sticky top-0 z-10">
      <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-8 h-8 bg-emerald-500/10 border border-emerald-500/30 rounded flex items-center justify-center">
            <Shield class="w-5 h-5 text-emerald-500" />
          </div>
          <h1 class="text-xl font-semibold text-white">VXSamples</h1>
        </div>
        <div class="flex items-center gap-4 text-sm text-gray-400">
          <a href="#" class="hover:text-gray-200 transition-colors">Documentation</a>
          <a href="#" class="hover:text-gray-200 transition-colors">API</a>
        </div>
      </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-6xl mx-auto px-4 py-12">
      <!-- Hero Section -->
      <div class="text-center mb-12">
        <h2 class="text-4xl font-bold text-white mb-4 text-balance">
          File Hash Intelligence Lookup
        </h2>
        <p class="text-gray-400 text-lg max-w-2xl mx-auto text-pretty">
          Search across multiple threat intelligence sources to identify file samples and download availability
        </p>
      </div>

      <!-- Search Section -->
      <div class="max-w-3xl mx-auto mb-12">
        <div class="bg-gray-900/50 border border-gray-800 rounded-lg p-6">
          <label class="block text-sm font-medium text-gray-300 mb-3">
            Enter File Hash
          </label>
          <div class="flex gap-3">
            <input
              v-model="hashInput"
              @keyup.enter="searchHash"
              type="text"
              placeholder="MD5, SHA1, or SHA256 hash..."
              class="flex-1 bg-black border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:border-emerald-500 transition-all font-mono text-sm"
            />
            <button
              @click="searchHash"
              :disabled="loading || !hashInput.trim()"
              class="px-6 py-3 bg-emerald-600 hover:bg-emerald-500 disabled:bg-gray-700 disabled:text-gray-500 text-white rounded-lg font-medium transition-all flex items-center gap-2 disabled:cursor-not-allowed"
            >
              <Search class="w-4 h-4" />
              Search
            </button>
          </div>
          
          <!-- Hash Type Indicator -->
          <div v-if="hashType" class="mt-3 flex items-center gap-2 text-sm">
            <span class="text-gray-400">Detected:</span>
            <span class="px-2 py-1 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 rounded font-mono text-xs">
              {{ hashType }}
            </span>
          </div>

          <!-- Error Message -->
          <div v-if="error" class="mt-3 flex items-start gap-2 text-sm text-red-400 bg-red-500/10 border border-red-500/30 rounded-lg p-3">
            <AlertCircle class="w-4 h-4 mt-0.5 flex-shrink-0" />
            <span>{{ error }}</span>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="max-w-3xl mx-auto">
        <div class="bg-gray-900/50 border border-gray-800 rounded-lg p-8 text-center">
          <div class="inline-flex items-center gap-3 text-gray-400">
            <div class="w-5 h-5 border-2 border-gray-600 border-t-emerald-500 rounded-full animate-spin"></div>
            <span>Querying threat intelligence sources...</span>
          </div>
        </div>
      </div>

      <!-- Results Section -->
      <div v-if="results && !loading" class="max-w-3xl mx-auto space-y-6">
        <!-- Summary Card -->
        <div class="bg-gray-900/50 border border-gray-800 rounded-lg p-6">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold text-white">Search Results</h3>
            <span class="text-sm text-gray-400">
              {{ results.matches?.length || 0 }} source{{ (results.matches?.length || 0) !== 1 ? 's' : '' }} found
            </span>
          </div>
          
          <div class="grid grid-cols-3 gap-4 mb-4">
            <div class="bg-black/50 border border-gray-800 rounded-lg p-4">
              <div class="text-2xl font-bold text-white mb-1">{{ results.matches?.length || 0 }}</div>
              <div class="text-xs text-gray-400">Total Matches</div>
            </div>
            <div class="bg-black/50 border border-gray-800 rounded-lg p-4">
              <div class="text-2xl font-bold text-emerald-400 mb-1">
                {{ results.matches?.filter(m => m.downloadable).length || 0 }}
              </div>
              <div class="text-xs text-gray-400">Downloadable</div>
            </div>
            <div class="bg-black/50 border border-gray-800 rounded-lg p-4">
              <div class="text-2xl font-bold text-blue-400 mb-1">
                {{ new Set(results.matches?.map(m => m.source)).size || 0 }}
              </div>
              <div class="text-xs text-gray-400">Unique Sources</div>
            </div>
          </div>

          <!-- Hash Info -->
          <div class="bg-black/50 border border-gray-800 rounded-lg p-4">
            <div class="text-xs text-gray-400 mb-1">Searched Hash</div>
            <div class="font-mono text-sm text-gray-200 break-all">{{ results.hash }}</div>
          </div>
        </div>

        <!-- Matches List -->
        <div class="space-y-3">
          <h4 class="text-sm font-medium text-gray-400 uppercase tracking-wider">
            Source Matches
          </h4>
          
          <div v-if="results.matches && results.matches.length > 0" class="space-y-2">
            <div
              v-for="(match, index) in results.matches"
              :key="index"
              class="bg-gray-900/50 border border-gray-800 rounded-lg p-4 hover:border-gray-700 transition-colors"
            >
              <div class="flex items-start justify-between gap-4">
                <div class="flex-1 min-w-0">
                  <div class="flex items-center gap-3 mb-2">
                    <div class="flex items-center gap-2">
                      <Database class="w-4 h-4 text-gray-400 flex-shrink-0" />
                      <span class="font-medium text-white">{{ match.source }}</span>
                    </div>
                    <span
                      v-if="match.downloadable"
                      class="px-2 py-0.5 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 rounded text-xs font-medium flex items-center gap-1"
                    >
                      <Download class="w-3 h-3" />
                      Downloadable
                    </span>
                  </div>
                  
                  <div v-if="match.filename" class="text-sm text-gray-400 mb-1">
                    <span class="text-gray-500">Filename:</span> 
                    <span class="font-mono">{{ match.filename }}</span>
                  </div>
                  
                  <div v-if="match.detectionRate" class="text-sm text-gray-400">
                    <span class="text-gray-500">Detection:</span> 
                    <span :class="getDetectionColor(match.detectionRate)">
                      {{ match.detectionRate }}
                    </span>
                  </div>
                </div>

                <div class="flex items-center gap-2">
                  <a
                    v-if="match.url"
                    :href="match.url"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="p-2 bg-gray-800 hover:bg-gray-700 border border-gray-700 rounded text-gray-300 hover:text-white transition-colors"
                    title="View on source"
                  >
                    <ExternalLink class="w-4 h-4" />
                  </a>
                </div>
              </div>
            </div>
          </div>

          <div v-else class="bg-gray-900/50 border border-gray-800 rounded-lg p-8 text-center">
            <FileQuestion class="w-12 h-12 text-gray-600 mx-auto mb-3" />
            <p class="text-gray-400">No matches found for this hash</p>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="!results && !loading" class="max-w-3xl mx-auto">
        <div class="bg-gray-900/50 border border-gray-800 rounded-lg p-12 text-center">
          <Shield class="w-16 h-16 text-gray-700 mx-auto mb-4" />
          <h3 class="text-lg font-medium text-gray-300 mb-2">Ready to Search</h3>
          <p class="text-gray-500 text-sm">
            Enter a file hash above to query threat intelligence sources
          </p>
        </div>
      </div>
    </main>

    <!-- Footer -->
    <footer class="border-t border-gray-800 mt-20">
      <div class="max-w-6xl mx-auto px-4 py-6 text-center text-sm text-gray-500">
        <p>VXSamples - File Hash Intelligence Platform</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { Shield, Search, Database, Download, ExternalLink, AlertCircle, FileQuestion } from 'lucide-vue-next'

const hashInput = ref('')
const loading = ref(false)
const results = ref(null)
const error = ref('')

// Detect hash type based on length
const hashType = computed(() => {
  const cleaned = hashInput.value.trim().toLowerCase()
  if (!/^[a-f0-9]+$/.test(cleaned)) return null
  
  if (cleaned.length === 32) return 'MD5'
  if (cleaned.length === 40) return 'SHA1'
  if (cleaned.length === 64) return 'SHA256'
  return null
})

// Clear error when input changes
watch(hashInput, () => {
  error.value = ''
})

// Search function
const searchHash = async () => {
  const hash = hashInput.value.trim()
  
  if (!hash) {
    error.value = 'Please enter a hash value'
    return
  }
  
  if (!hashType.value) {
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
        type: hashType.value
      })
    })
    
    if (!response.ok) {
      throw new Error(`API error: ${response.status}`)
    }
    
    const data = await response.json()
    results.value = data
  } catch (err) {
    error.value = `Failed to query API: ${err.message}`
    console.error('Search error:', err)
  } finally {
    loading.value = false
  }
}

// Helper function for detection rate coloring
const getDetectionColor = (rate) => {
  if (!rate) return 'text-gray-400'
  
  const match = rate.match(/(\d+)\/(\d+)/)
  if (!match) return 'text-gray-400'
  
  const detected = parseInt(match[1])
  const total = parseInt(match[2])
  const percentage = (detected / total) * 100
  
  if (percentage === 0) return 'text-emerald-400'
  if (percentage < 30) return 'text-yellow-400'
  return 'text-red-400'
}
</script>

<style scoped>
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