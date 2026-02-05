
// UX Booster Pack Scripts
document.addEventListener('DOMContentLoaded', () => {

    // 1. Reading Progress Bar
    const progressBar = document.createElement('div');
    progressBar.id = 'progress-bar';
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', () => {
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (scrollTop / scrollHeight) * 100;
        progressBar.style.width = scrolled + '%';

        // 2. Back To Top Visibility
        const backToTopBtn = document.getElementById('back-to-top');
        if (backToTopBtn) {
            if (scrollTop > 300) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        }
    });

    // 2. Back To Top Button Injection
    const backBtn = document.createElement('button');
    backBtn.id = 'back-to-top';
    backBtn.innerHTML = '↑';
    backBtn.ariaLabel = "Back to Top";
    backBtn.onclick = () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };
    document.body.appendChild(backBtn);


    // 3. Theme Management
    const THEME_KEY = 'site-theme';

    function getSavedTheme() {
        return localStorage.getItem(THEME_KEY);
    }

    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem(THEME_KEY, theme);
        updateToggleButton(theme);
    }

    function toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    }

    function updateToggleButton(theme) {
        const toggleBtn = document.getElementById('theme-toggle');
        if (toggleBtn) {
            toggleBtn.textContent = theme === 'dark' ? '[ LIGHT ]' : '[ DARK ]';
        }
    }

    const savedTheme = getSavedTheme();
    if (savedTheme) {
        setTheme(savedTheme);
    } else {
        const systemTheme = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
        setTheme(systemTheme);
    }

    document.addEventListener('click', (e) => {
        if (e.target.id === 'theme-toggle' || e.target.closest('#theme-toggle')) {
            toggleTheme();
        }
    });

});
