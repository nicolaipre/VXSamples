<template>
  <header class="border-b border-gray-800 bg-black/50 backdrop-blur-sm sticky top-0 z-10">
    <div class="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <div
          class="w-8 h-8 bg-emerald-500/10 border border-emerald-500/30 rounded flex items-center justify-center"
        >
          <Shield class="w-5 h-5 text-emerald-500 m-0.5" />
        </div>
        <h1 class="text-xl font-semibold text-white">VXSamples</h1>
      </div>
      <div class="flex items-center gap-4 text-sm text-gray-400">
        <a href="#" class="hover:text-gray-200 transition-colors">Documentation</a>
        <a href="#" class="hover:text-gray-200 transition-colors">API</a>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { Shield } from 'lucide-vue-next'
</script>

<style scoped>
/* Header styles */
header {
  border-bottom: 1px solid #1f2937;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
  position: sticky;
  top: 0;
  z-index: 10;
}

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

.py-4 {
  padding-top: 1rem;
  padding-bottom: 1rem;
}

.flex {
  display: flex;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.justify-between {
  justify-content: space-between;
}

.gap-3 {
  gap: 0.75rem;
}

.gap-4 {
  gap: 1rem;
}

.w-8 {
  width: 2rem;
}

.h-8 {
  height: 2rem;
}

.w-5 {
  width: 1.25rem;
}

.h-5 {
  height: 1.25rem;
}

.bg-emerald-500\/10 {
  background-color: rgba(16, 185, 129, 0.1);
}

.border-emerald-500\/30 {
  border: 1px solid rgba(16, 185, 129, 0.3);
}

.rounded {
  border-radius: 0.25rem;
}

.text-emerald-500 {
  color: #10b981;
}

.text-xl {
  font-size: 1.25rem;
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

.text-gray-400 {
  color: #9ca3af;
}

/* Link styles - override browser defaults */
a {
  color: #9ca3af !important;
  text-decoration: none;
  transition: color 0.15s ease-in-out;
}

a:hover {
  color: #e5e7eb !important;
}

.transition-colors {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}
</style>
