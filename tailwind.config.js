/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'Clients/templates/Clients/*.html',
    'base_auth/templates/base_auth/*.html',
    'leads/templates/leads/*.html',
    'dashboard/templates/dashboard/*.html',
    'teams/templates/teams/*.html',
    'templates/*.html',
    'templates/include/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

