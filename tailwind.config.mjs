/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        sans: [
          '-apple-system',
          'BlinkMacSystemFont',
          '"PingFang SC"',
          '"Hiragino Sans GB"',
          '"Microsoft YaHei"',
          '"Noto Sans SC"',
          'system-ui',
          'sans-serif',
        ],
        serif: [
          '"Source Han Serif SC"',
          '"Noto Serif SC"',
          'Songti SC',
          'SimSun',
          'serif',
        ],
        mono: [
          'ui-monospace',
          'SFMono-Regular',
          'Menlo',
          'Monaco',
          'Consolas',
          'monospace',
        ],
      },
      colors: {
        brand: {
          50: '#eef2ff',
          100: '#e0e7ff',
          200: '#c7d2fe',
          500: '#6366f1',
          600: '#4f46e5',
          700: '#4338ca',
        },
        paper: {
          50: '#faf9f6',
          100: '#f5f4ef',
          200: '#eae8df',
          300: '#dcd9ce',
          700: '#2a2e33',
          800: '#1e2124',
          900: '#141618',
          950: '#0d0f11',
        },
      },
    },
  },
  plugins: [],
};
