import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'https://ai-daily.pages.dev',
  server: {
    port: 3000,
    host: true,
  },
  integrations: [
    tailwind({
      applyBaseStyles: false,
    }),
  ],
});
