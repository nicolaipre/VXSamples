<template>
  <div class="max-w-3xl mx-auto mb-12">
    <div class="bg-gray-900/50 border border-gray-800 rounded-lg p-6">
      <label class="block text-sm font-medium text-gray-300 mb-3"> Enter File Hash </label>
      <div class="flex gap-3">
        <input
          v-model="hashInput"
          @keyup.enter="handleSearch"
          type="text"
          placeholder="MD5, SHA1, or SHA256 hash..."
          class="flex-1 bg-black border border-gray-700 rounded-lg px-4 py-3 text-white placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:border-emerald-500 transition-all font-mono text-sm"
        />
        <button
          @click="handleSearch"
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
        <span
          class="px-2 py-1 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 rounded font-mono text-xs"
        >
          {{ hashType }}
        </span>
      </div>

      <!-- Error Message -->
      <div
        v-if="error"
        class="mt-3 flex items-start gap-2 text-sm text-red-400 bg-red-500/10 border border-red-500/30 rounded-lg p-3"
      >
        <AlertCircle class="w-4 h-4 mt-0.5 flex-shrink-0" />
        <span>{{ error }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { Search, AlertCircle } from 'lucide-vue-next'

interface Props {
  loading?: boolean
  error?: string
}

interface Emits {
  (e: 'search', hash: string, type: string): void
}

const props = defineProps<Props>()
const emit = defineEmits<Emits>()

const hashInput = ref('')

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
  if (props.error) {
    emit('search', '', '') // Clear error by emitting empty search
  }
})

// Search function
const handleSearch = () => {
  const hash = hashInput.value.trim()

  if (!hash) {
    emit('search', '', '')
    return
  }

  if (!hashType.value) {
    emit('search', '', '')
    return
  }

  emit('search', hash.toLowerCase(), hashType.value)
}
</script>

<style scoped>
/* Search form styles */
.max-w-3xl {
  max-width: 48rem;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.mb-12 {
  margin-bottom: 3rem;
}

.bg-gray-900\/50 {
  background-color: rgba(17, 24, 39, 0.5);
}

.border {
  border: 1px solid #1f2937;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.p-6 {
  padding: 1.5rem;
}

.block {
  display: block;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.font-medium {
  font-weight: 500;
}

.text-gray-300 {
  color: #d1d5db;
}

.mb-3 {
  margin-bottom: 0.75rem;
}

.flex {
  display: flex;
}

.gap-3 {
  gap: 0.75rem;
}

.flex-1 {
  flex: 1 1 0%;
}

.bg-black {
  background-color: #000000;
}

.border-gray-700 {
  border-color: #374151;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.py-3 {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}

.text-white {
  color: #ffffff;
}

.placeholder-gray-500::placeholder {
  color: #6b7280;
}

.focus\:outline-none:focus {
  outline: none;
}

.focus\:ring-2:focus {
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.5);
}

.focus\:ring-emerald-500\/50:focus {
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.5);
}

.focus\:border-emerald-500:focus {
  border-color: #10b981;
}

.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.font-mono {
  font-family:
    ui-monospace, SFMono-Regular, 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace;
}

.px-6 {
  padding-left: 1.5rem;
  padding-right: 1.5rem;
}

.bg-emerald-600 {
  background-color: #059669;
}

.hover\:bg-emerald-500:hover {
  background-color: #047857;
}

.disabled\:bg-gray-700:disabled {
  background-color: #374151;
}

.disabled\:text-gray-500:disabled {
  color: #6b7280;
}

.text-white {
  color: #ffffff;
}

.font-medium {
  font-weight: 500;
}

.flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.gap-2 {
  gap: 0.5rem;
}

.disabled\:cursor-not-allowed:disabled {
  cursor: not-allowed;
}

.w-4 {
  width: 1rem;
}

.h-4 {
  height: 1rem;
}

.mt-3 {
  margin-top: 0.75rem;
}

.text-gray-400 {
  color: #9ca3af;
}

.py-1 {
  padding-top: 0.25rem;
  padding-bottom: 0.25rem;
}

.px-2 {
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}

.bg-emerald-500\/10 {
  background-color: rgba(16, 185, 129, 0.1);
}

.border-emerald-500\/30 {
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.text-emerald-400 {
  color: #34d399;
}

.rounded {
  border-radius: 0.25rem;
}

.text-xs {
  font-size: 0.75rem;
  line-height: 1rem;
}

/* Hash type indicator - just ensure proper text alignment */
.bg-emerald-500\/10 {
  line-height: 1.2;
}

.items-start {
  align-items: flex-start;
}

.text-red-400 {
  color: #f87171;
}

.bg-red-500\/10 {
  background-color: rgba(239, 68, 68, 0.1);
}

.border-red-500\/30 {
  border: 1px solid rgba(239, 68, 68, 0.3);
}

.p-3 {
  padding: 0.75rem;
}

.mt-0\.5 {
  margin-top: 0.125rem;
}

.flex-shrink-0 {
  flex-shrink: 0;
}

/* Input styles */
input {
  background-color: #000000;
  border: 1px solid #374151;
  border-radius: 0.5rem;
  padding: 0.75rem 1rem;
  color: #ffffff;
  font-family:
    ui-monospace, SFMono-Regular, 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace;
  font-size: 0.875rem;
  line-height: 1.25rem;
  transition: all 0.15s ease-in-out;
}

input:focus {
  outline: none;
  border-color: #10b981;
  box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.5);
}

input::placeholder {
  color: #6b7280;
}

/* Button styles */
button {
  padding: 0.75rem 1.5rem;
  background-color: #059669;
  color: #ffffff;
  border-radius: 0.5rem;
  font-weight: 500;
  transition: all 0.15s ease-in-out;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

button:hover:not(:disabled) {
  background-color: #047857;
}

button:disabled {
  background-color: #374151;
  color: #6b7280;
  cursor: not-allowed;
}
</style>
