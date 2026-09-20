import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#0F172A",
        foreground: "#F8FAFC",
        primary: {
          DEFAULT: "#38BDF8",
          foreground: "#0F172A",
        },
        card: {
          DEFAULT: "#1E293B",
          foreground: "#F8FAFC",
        },
        accent: {
          DEFAULT: "#818CF8",
          foreground: "#FFFFFF",
        },
        muted: {
          DEFAULT: "#334155",
          foreground: "#94A3B8",
        },
      },
    },
  },
  plugins: [],
};

export default config;
