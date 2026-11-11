// static/js/script.js
(function initTheme() {
  const root = document.documentElement;
  const savedTheme = localStorage.getItem('portfolio-theme') || 'dark';

  function applyTheme(theme) {
    root.setAttribute('data-theme', theme);
    root.setAttribute('data-bs-theme', theme);

    if (document.body) {
      document.body.setAttribute('data-theme', theme);
      document.body.setAttribute('data-bs-theme', theme);
    }

    const themeIcon = document.getElementById('themeIcon');
    if (themeIcon) {
      themeIcon.className = theme === 'dark' ? 'bi bi-moon-stars-fill' : 'bi bi-sun-fill';
    }

    localStorage.setItem('portfolio-theme', theme);
  }

  // Turant apply karein
  applyTheme(savedTheme);

  document.addEventListener('DOMContentLoaded', function () {
    const themeBtn = document.getElementById('themeToggle');
    if (themeBtn) {
      themeBtn.addEventListener('click', function () {
        const currentTheme = root.getAttribute('data-theme') || 'dark';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        applyTheme(newTheme);
      });
    }

    // Keyboard ⌘K shortcut
    document.addEventListener('keydown', function (e) {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        const searchModal = document.getElementById('searchModal');
        if (searchModal && window.bootstrap) {
          const bsModal = bootstrap.Modal.getOrCreateInstance(searchModal);
          bsModal.toggle();
        }
      }
    });
  });
})();