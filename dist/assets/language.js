'use strict';
// Only a language choice is persisted; form data never leaves the page.
(() => { if (location.pathname !== '/') return; let saved; try { saved = localStorage.getItem('harnessloop-language'); } catch {} const lang = saved === 'en' || saved === 'zh' ? saved : ((navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en'); if (lang === 'en') location.replace('/en/' + location.search + location.hash); })();
