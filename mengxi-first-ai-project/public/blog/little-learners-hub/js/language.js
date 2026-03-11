// Language Toggle System for Little Learners Hub

(function() {
  'use strict';

  const STORAGE_KEY = 'little-learners-lang';

  // Get saved language or default to English
  function getSavedLanguage() {
    return localStorage.getItem(STORAGE_KEY) || 'en';
  }

  // Save language preference
  function saveLanguage(lang) {
    localStorage.setItem(STORAGE_KEY, lang);
  }

  // Apply language to page
  function applyLanguage(lang) {
    const body = document.body;

    if (lang === 'zh') {
      body.classList.add('lang-zh');
    } else {
      body.classList.remove('lang-zh');
    }

    // Update toggle buttons
    document.querySelectorAll('.language-toggle button').forEach(btn => {
      btn.classList.remove('active');
      if (btn.dataset.lang === lang) {
        btn.classList.add('active');
      }
    });
  }

  // Initialize on page load
  function init() {
    const savedLang = getSavedLanguage();
    applyLanguage(savedLang);

    // Add click handlers to toggle buttons
    document.querySelectorAll('.language-toggle button').forEach(btn => {
      btn.addEventListener('click', function() {
        const lang = this.dataset.lang;
        saveLanguage(lang);
        applyLanguage(lang);
      });
    });
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
