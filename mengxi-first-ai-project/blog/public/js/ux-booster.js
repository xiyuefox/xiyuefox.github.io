
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

        if (theme === 'retro') {
            document.body.classList.add('retro-active');
        } else {
            document.body.classList.remove('retro-active');
        }
    }

    function toggleTheme(event) {
        const themes = ['dark', 'light', 'retro'];
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        let currentIndex = themes.indexOf(currentTheme);
        const newTheme = themes[(currentIndex + 1) % themes.length];

        if (!document.startViewTransition || !event || event.type === 'keydown') {
            setTheme(newTheme);
            return;
        }

        const x = event.clientX;
        const y = event.clientY;
        const endRadius = Math.hypot(
            Math.max(x, window.innerWidth - x),
            Math.max(y, window.innerHeight - y)
        );

        const transition = document.startViewTransition(() => {
            setTheme(newTheme);
        });

        transition.ready.then(() => {
            document.documentElement.animate(
                {
                    clipPath: [
                        `circle(0px at ${x}px ${y}px)`,
                        `circle(${endRadius}px at ${x}px ${y}px)`
                    ],
                },
                {
                    duration: 500,
                    easing: 'ease-in-out',
                    pseudoElement: '::view-transition-new(root)',
                }
            );
        });
    }

    function updateToggleButton(theme) {
        const toggleBtn = document.getElementById('theme-toggle');
        if (toggleBtn) {
            const icons = { 'dark': '[ LIGHT ]', 'light': '[ RETRO ]', 'retro': '[ DARK ]' };
            toggleBtn.textContent = icons[theme] || '[ DARK ]';
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
            toggleTheme(e);
        }
    });

    document.addEventListener('keydown', (e) => {
        if (['input', 'textarea'].includes(document.activeElement.tagName.toLowerCase())) return;

        if (e.key.toLowerCase() === 't') {
            toggleTheme(e);
        } else if (e.key.toLowerCase() === 'r') {
            const current = document.documentElement.getAttribute('data-theme');
            setTheme(current === 'retro' ? 'dark' : 'retro');
        }
    });

    // Mouse tracking for spotlight effect
    document.addEventListener('mousemove', (e) => {
        document.documentElement.style.setProperty('--mouse-x', e.clientX + 'px');
        document.documentElement.style.setProperty('--mouse-y', e.clientY + 'px');
    });

});
