/**
 * Shared JavaScript - Designer Showcase
 * Theme System + Scroll Animations
 */

(function () {
    'use strict';

    // ============================================
    // THEME MANAGEMENT
    // ============================================
    const THEME_KEY = 'designer-showcase-theme';

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
    }

    function toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    }

    function updateToggleButton(theme) {
        const toggleBtn = document.querySelector('.theme-toggle');
        if (toggleBtn) {
            toggleBtn.textContent = theme === 'dark' ? 'LIGHT_MODE' : 'DARK_MODE';
        }
    }

    function initTheme() {
        const savedTheme = getSavedTheme();
        const theme = savedTheme || 'dark'; // Default to dark
        setTheme(theme);

        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', (e) => {
            if (!getSavedTheme()) {
                setTheme(e.matches ? 'light' : 'dark');
            }
        });

        // Setup toggle button
        document.querySelectorAll('.theme-toggle').forEach(btn => {
            btn.addEventListener('click', toggleTheme);
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
