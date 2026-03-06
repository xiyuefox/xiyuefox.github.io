/**
 * Shared JavaScript - Designer Showcase
 * Theme System + Scroll Animations
 */

(function () {
    'use strict';

    // ============================================
    // THEME MANAGEMENT
    // ============================================
    const THEME_KEY = 'site-theme';

    function getSystemTheme() {
        return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
    }

    function getSavedTheme() {
        return localStorage.getItem(THEME_KEY);
    }

    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem(THEME_KEY, theme);
        updateToggleButton(theme);

        // Disable body contrast filter if transition API is doing heavy lifting
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
        document.querySelectorAll('.theme-toggle, .theme-toggle-btn, #page-theme-toggle').forEach(btn => {
            const icons = { 'dark': 'LIGHT_MODE', 'light': 'RETRO_VIBE', 'retro': 'DARK_MODE' };
            btn.textContent = icons[theme] || 'DARK_MODE';
        });
    }

    function initTheme() {
        const savedTheme = getSavedTheme();
        const theme = savedTheme || 'dark'; // Default to dark
        setTheme(theme);

        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', (e) => {
            if (!localStorage.getItem(THEME_KEY)) {
                setTheme(e.matches ? 'light' : 'dark');
            }
        });

        // Setup toggle button
        document.addEventListener('click', (e) => {
            if (e.target.closest('.theme-toggle') || e.target.closest('.theme-toggle-btn') || e.target.id === 'page-theme-toggle') {
                toggleTheme(e);
            }
        });

        // Keyboard Shortcut: T to toggle theme, R for retro
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
    }

    // ============================================
    // SCROLL REVEAL ANIMATIONS
    // ============================================
    function initRevealAnimations() {
        const reveals = document.querySelectorAll('.reveal');

        if (!reveals.length) return;

        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    // Stagger animation
                    setTimeout(() => {
                        entry.target.classList.add('active');
                    }, index * 50);
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        reveals.forEach(el => observer.observe(el));
    }

    // ============================================
    // SMOOTH SCROLL FOR ANCHOR LINKS
    // ============================================
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    // ============================================
    // PARALLAX BACKGROUND (Optional)
    // ============================================
    function initParallaxBackground() {
        const grid = document.querySelector('.bg-grid');
        if (!grid) return;

        // Only on desktop
        if (window.innerWidth < 768) return;

        let ticking = false;

        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    const scrolled = window.pageYOffset;
                    grid.style.transform = `translateY(${scrolled * 0.1}px)`;
                    ticking = false;
                });
                ticking = true;
            }
        });
    }

    // ============================================
    // MOBILE NAVIGATION HANDLING
    // ============================================
    function initMobileNav() {
        const navBar = document.querySelector('.nav-bar');
        if (!navBar) return;

        let lastScrollTop = 0;
        let ticking = false;

        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

                    if (scrollTop > lastScrollTop && scrollTop > 100) {
                        // Scrolling down - hide nav on mobile
                        if (window.innerWidth < 768) {
                            navBar.style.transform = 'translateY(-100%)';
                        }
                    } else {
                        // Scrolling up - show nav
                        navBar.style.transform = 'translateY(0)';
                    }

                    lastScrollTop = scrollTop;
                    ticking = false;
                });
                ticking = true;
            }
        });
    }

    // ============================================
    // CARD HOVER EFFECTS
    // ============================================
    function initCardEffects() {
        const cards = document.querySelectorAll('.designer-card');

        cards.forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.zIndex = '10';
            });

            card.addEventListener('mouseleave', () => {
                card.style.zIndex = '';
            });
        });
    }

    // ============================================
    // KEYBOARD NAVIGATION
    // ============================================
    function initKeyboardNav() {
        document.addEventListener('keydown', (e) => {
            // Toggle theme with 'T' key
            if (e.key === 't' || e.key === 'T') {
                if (!e.ctrlKey && !e.metaKey && !e.altKey) {
                    const activeElement = document.activeElement;
                    const isInputField = activeElement.tagName === 'INPUT' ||
                        activeElement.tagName === 'TEXTAREA' ||
                        activeElement.isContentEditable;

                    if (!isInputField) {
                        toggleTheme();
                    }
                }
            }
        });
    }

    // ============================================
    // INITIALIZE
    // ============================================
    function init() {
        initTheme();
        initRevealAnimations();
        initSmoothScroll();
        initParallaxBackground();
        initMobileNav();
        initCardEffects();
        initKeyboardNav();
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Expose theme toggle function globally
    window.DesignerShowcase = {
        toggleTheme: toggleTheme,
        setTheme: setTheme
    };
})();
