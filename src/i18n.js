import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const en = require('./locales/en.json');
const th = require('./locales/th.json');

i18n.use(initReactI18next).init({
  resources: {
    en: { translation: en },
    th: { translation: th }
  },
  lng: 'th',
  fallbackLng: 'en',
  interpolation: {
    escapeValue: false
  }
});

export default i18n;