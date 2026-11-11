module.exports = {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'sans-serif'],
        display: ['"Plus Jakarta Sans"', 'Inter', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
      boxShadow: {
        '2xs': '0 1px 2px 0 rgba(15, 23, 42, 0.04)',
        xs: '0 1px 3px 0 rgba(15, 23, 42, 0.07), 0 1px 2px -1px rgba(15, 23, 42, 0.05)',
        soft: '0 12px 32px -10px rgba(10, 84, 130, 0.14)',
      },
      backdropBlur: {
        xs: '2px',
      },
      spacing: {
        '4.5': '1.125rem',
        '13': '3.25rem',
        '15': '3.75rem',
        '18': '4.5rem',
      },
      opacity: {
        '12': '0.12',
        '15': '0.15',
        '22': '0.22',
        '35': '0.35',
        '65': '0.65',
        '85': '0.85',
      },
    },
  },
  plugins: [],
};

