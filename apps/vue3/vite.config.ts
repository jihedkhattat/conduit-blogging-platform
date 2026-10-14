import process from 'node:process'
import { URL, fileURLToPath } from 'node:url'

import { defineConfig } from 'vite'
import Vue from '@vitejs/plugin-vue'
import Layouts from 'vite-plugin-vue-layouts'
import VueRouter from 'unplugin-vue-router/vite'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { VueRouterAutoImports, getPascalCaseRouteName } from 'unplugin-vue-router'

export default defineConfig({
  plugins: [
    VueRouter({ getRouteName: getPascalCaseRouteName }),
    Vue(),
    Layouts(),
    Components({ dts: true }),
    AutoImport({
      dts: true,
      vueTemplate: true,
      imports: ['vue', 'pinia', VueRouterAutoImports],
    }),
  ],
  server: {
    host: false,
    open: !process.env.CI, // don't try to open a browser in CI
    proxy: {
      '/api': {
        changeOrigin: true,
        target: 'http://localhost:8081', // '^http:\/\/(localhost|127\.0\.0\.1|api)(:\d+)?',
        rewrite: path => path.replace(/^\/api/, ''),
      },
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
