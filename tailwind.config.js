/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      colors: {
        'green-glessi': '#006400',
        'yellow-glessi': '#F8E110',
        'red-glessi': '#E60606',
        'orange-glessi' : '#FF8B04',
        'blue-glessi' : '#0062BC',
        'famer-color' : '#573625'
      },
    },
  },
  plugins: [],
}

