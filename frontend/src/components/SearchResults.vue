<template>
  <!-- Loading State -->
  <div v-if="loading" class="max-w-3xl mx-auto">
    <div class="bg-gray-900/50 border border-gray-800 rounded-lg p-8 text-center">
      <div class="inline-flex items-center gap-3 text-gray-400">
        <div
          class="w-5 h-5 border-2 border-gray-600 border-t-emerald-500 rounded-full animate-spin"
        ></div>
        <span>Querying threat intelligence sources...</span>
      </div>
    </div>
  </div>

  <!-- Results Section -->
  <div v-else-if="results" class="max-w-3xl mx-auto space-y-6">
    <!-- Summary Card -->
    <div class="bg-gray-900/50 border border-gray-800 rounded-lg p-6">
      <div class="flex items-center justify-between mb-4">
        <h3 class="text-lg font-semibold text-white">Search Results</h3>
        <span class="text-sm text-gray-400">
          {{ results.matches?.length || 0 }} source{{
            (results.matches?.length || 0) !== 1 ? 's' : ''
          }}
          found
        </span>
      </div>

      <div class="grid grid-cols-3 gap-4 mb-4">
        <div class="bg-black/50 border border-gray-800 rounded-lg p-4">
          <div class="text-2xl font-bold text-white mb-1">{{ results.matches?.length || 0 }}</div>
          <div class="text-xs text-gray-400">Total Matches</div>
        </div>
        <div class="bg-black/50 border border-gray-800 rounded-lg p-4">
          <div class="text-2xl font-bold text-emerald-400 mb-1">
            {{ results.matches?.filter((m) => m.downloadable).length || 0 }}
          </div>
          <div class="text-xs text-gray-400">Downloadable</div>
        </div>
        <div class="bg-black/50 border border-gray-800 rounded-lg p-4">
          <div class="text-2xl font-bold text-blue-400 mb-1">
            {{ new Set(results.matches?.map((m) => m.source)).size || 0 }}
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
      <h4 class="text-sm font-medium text-gray-400 uppercase tracking-wider">Source Matches</h4>

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
                  class="px-2 py-0.5 bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 rounded text-xs font-medium flex items-center"
                >
                  <Download class="w-3 h-3 mx-1" />
                  Downloadable
                </span>
              </div>

              <div v-if="match.filename" class="text-sm text-gray-400 mb-1">
                <span class="text-gray-500">Filename:</span>
                <span class="font-mono ml-1">{{ match.filename }}</span>
              </div>

              <div v-if="match.detectionRate" class="text-sm text-gray-400">
                <span class="text-gray-500">Detection:</span>
                <span :class="getDetectionColor(match.detectionRate)" class="ml-1">
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
  <div v-else class="max-w-3xl mx-auto">
    <div class="bg-gray-900/50 border border-gray-800 rounded-lg p-12 text-center">
      <Shield class="w-16 h-16 text-gray-700 mx-auto mb-4" />
      <h3 class="text-lg font-medium text-gray-300 mb-2">Ready to Search</h3>
      <p class="text-gray-500 text-sm">
        Enter a file hash above to query threat intelligence sources
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Database, Download, ExternalLink, FileQuestion, Shield } from 'lucide-vue-next'

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

interface Props {
  loading?: boolean
  results?: SearchResultsData | null
}

defineProps<Props>()

// Helper function for detection rate coloring
const getDetectionColor = (rate: string | undefined) => {
  if (!rate) return 'text-gray-400'

  const match = rate.match(/(\d+)\/(\d+)/)
  if (!match) return 'text-gray-400'

  const detected = parseInt(match[1]!)
  const total = parseInt(match[2]!)
  const percentage = (detected / total) * 100

  if (percentage === 0) return 'text-emerald-400'
  if (percentage < 30) return 'text-yellow-400'
  return 'text-red-400'
}
</script>

<style scoped>
/* Search results styles */
.max-w-3xl {
  max-width: 48rem;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.bg-gray-900\/50 {
  background-color: rgba(17, 24, 39, 0.5);
}

.border {
  border-width: 1px;
}

.border-gray-800 {
  border-color: #1f2937;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.p-8 {
  padding: 2rem;
}

.text-center {
  text-align: center;
}

.inline-flex {
  display: inline-flex;
}

.items-center {
  align-items: center;
}

.gap-3 {
  gap: 0.75rem;
}

.text-gray-400 {
  color: #9ca3af;
}

.w-5 {
  width: 1.25rem;
}

.h-5 {
  height: 1.25rem;
}

.border-2 {
  border-width: 2px;
}

.border-gray-600 {
  border-color: #4b5563;
}

.border-t-emerald-500 {
  border-top-color: #10b981;
}

.rounded-full {
  border-radius: 9999px;
}

.animate-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.space-y-6 > * + * {
  margin-top: 1.5rem;
}

.p-6 {
  padding: 1.5rem;
}

.flex {
  display: flex;
}

.justify-between {
  justify-content: space-between;
}

.mb-4 {
  margin-bottom: 1rem;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.font-semibold {
  font-weight: 600;
}

.text-white {
  color: #ffffff;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.grid {
  display: grid;
}

.grid-cols-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.gap-4 {
  gap: 1rem;
}

.bg-black\/50 {
  background-color: rgba(0, 0, 0, 0.5);
}

.p-4 {
  padding: 1rem;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2rem;
}

.font-bold {
  font-weight: 700;
}

.mb-1 {
  margin-bottom: 0.25rem;
}

.text-xs {
  font-size: 0.75rem;
  line-height: 1rem;
}

.text-emerald-400 {
  color: #34d399;
}

.text-blue-400 {
  color: #60a5fa;
}

.font-mono {
  font-family:
    ui-monospace, SFMono-Regular, 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace;
}

.text-gray-200 {
  color: #e5e7eb;
}

.break-all {
  word-break: break-all;
}

.space-y-3 > * + * {
  margin-top: 0.75rem;
}

.font-medium {
  font-weight: 500;
}

.uppercase {
  text-transform: uppercase;
}

.tracking-wider {
  letter-spacing: 0.05em;
}

.space-y-2 > * + * {
  margin-top: 0.5rem;
}

.hover\:border-gray-700:hover {
  border-color: #374151;
}

.transition-colors {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.items-start {
  align-items: flex-start;
}

.gap-4 {
  gap: 1rem;
}

.flex-1 {
  flex: 1 1 0%;
}

.min-w-0 {
  min-width: 0px;
}

.gap-2 {
  gap: 0.5rem;
}

.w-4 {
  width: 1rem;
}

.h-4 {
  height: 1rem;
}

.flex-shrink-0 {
  flex-shrink: 0;
}

.text-gray-500 {
  color: #6b7280;
}

.mb-2 {
  margin-bottom: 0.5rem;
}

.mb-1 {
  margin-bottom: 0.25rem;
}

.py-0\.5 {
  padding-top: 0.125rem;
  padding-bottom: 0.125rem;
}

.bg-emerald-500\/10 {
  background-color: rgba(16, 185, 129, 0.1);
}

.border-emerald-500\/30 {
  border-color: rgba(16, 185, 129, 0.3);
}

.rounded {
  border-radius: 0.25rem;
}

.w-3 {
  width: 0.75rem;
}

.h-3 {
  height: 0.75rem;
}

.bg-gray-800 {
  background-color: #1f2937;
}

.hover\:bg-gray-700:hover {
  background-color: #4b5563;
}

.border-gray-700 {
  border-color: #374151;
}

.text-gray-300 {
  color: #d1d5db;
}

.hover\:text-white:hover {
  color: #ffffff;
}

.w-12 {
  width: 3rem;
}

.h-12 {
  height: 3rem;
}

.text-gray-600 {
  color: #4b5563;
}

.p-12 {
  padding: 3rem;
}

.w-16 {
  width: 4rem;
}

.h-16 {
  height: 4rem;
}

.text-gray-700 {
  color: #374151;
}

.text-gray-300 {
  color: #d1d5db;
}

.text-gray-500 {
  color: #6b7280;
}

/* Color classes for detection rates */
.text-emerald-400 {
  color: #34d399;
}

.text-yellow-400 {
  color: #facc15;
}

.text-red-400 {
  color: #f87171;
}

.ml-1 {
  margin-left: 0.25rem;
}

.mx-1 {
  margin-left: 0.25rem;
  margin-right: 0.25rem;
}
</style>
