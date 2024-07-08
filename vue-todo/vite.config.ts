import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import UnoCSS from 'unocss/vite'

export default defineConfig({
  plugins: [
    vue(),
    UnoCSS(),
  ],
  server: {
    proxy: {
      '/api/': {
        target: 'http://127.0.0.1:8000/',
      }
    }
  }
})
