import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), vueDevTools()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },

  // Proxy server for development
  server: {
    //allowedHosts: "vxsamples.com",
    host: true,
    port: 5173,
    origin: 'http://vxsamples.com',

    // proxy all requests to 127.0.0.1:5173/api to port
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:9000',
        changeOrigin: false, // Don't spoof the origin
        headers: {
          Host: 'vxsamples.com',
        },
      },
    },
  },
})
