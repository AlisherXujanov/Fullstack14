// HMR  =>  Hot Module Replacement
//          This means that - when we save the file in the editor,
//          then, the browser reloads the page automatically.
// RU: Это означает, что - когда мы сохраняем файл в редакторе,
//     тогда браузер автоматически перезагружает страницу.


import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
})
