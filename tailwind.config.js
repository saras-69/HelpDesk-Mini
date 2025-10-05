/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './*/templates/**/*.html',
    './static/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        'help-blue': '#3B82F6',
        'help-green': '#10B981',
        'help-yellow': '#F59E0B',
        'help-red': '#EF4444',
        'help-gray': '#6B7280',
      }
    },
  },
  plugins: [],
}