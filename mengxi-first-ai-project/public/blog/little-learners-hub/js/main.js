// Simple interactions for the website
// Language Switching functionality with localStorage support
document.addEventListener('DOMContentLoaded', () => {
    // Check for the new style language toggle
    const languageToggle = document.getElementById('language-toggle');

    // If new style toggle exists (used in 0-12-months.html)
    if (languageToggle) {
        const zhLang = languageToggle.querySelector('[data-lang="zh"]');
        const enLang = languageToggle.querySelector('[data-lang="en"]');

        // Load saved language preference or default to English
        const savedLanguage = localStorage.getItem('llh-language') || 'en';

        // Set initial language
        if (savedLanguage === 'en') {
            document.body.classList.remove('lang-zh');
            enLang.classList.add('active-lang');
            zhLang.classList.remove('active-lang');
        } else {
            document.body.classList.add('lang-zh');
            zhLang.classList.add('active-lang');
            enLang.classList.remove('active-lang');
        }

        // Language toggle event
        languageToggle.addEventListener('click', (e) => {
            if (e.target.hasAttribute('data-lang')) {
                const targetLang = e.target.getAttribute('data-lang');

                // Update body class for CSS transitions
                if (targetLang === 'en') {
                    document.body.classList.remove('lang-zh');
                    enLang.classList.add('active-lang');
                    zhLang.classList.remove('active-lang');
                    localStorage.setItem('llh-language', 'en');
                } else {
                    document.body.classList.add('lang-zh');
                    zhLang.classList.add('active-lang');
                    enLang.classList.remove('active-lang');
                    localStorage.setItem('llh-language', 'zh');
                }
            }
        });
    }
    // Existing language toggle support for backward compatibility
    else {
        const languageToggleOld = document.querySelector('.language-toggle');
        const enBtn = document.querySelector('.toggle-btn.en');
        const zhBtn = document.querySelector('.toggle-btn.zh');

        // Check if we're on a bilingual page with old style toggle
        if (languageToggleOld && enBtn && zhBtn) {
            // Load saved language preference or default to English
            const savedLanguage = localStorage.getItem('llh-language') || 'en';

            // Set initial language
            if (savedLanguage === 'en') {
                enBtn.classList.add('active');
                zhBtn.classList.remove('active');
                document.body.classList.remove('lang-zh');
            } else {
                zhBtn.classList.add('active');
                enBtn.classList.remove('active');
                document.body.classList.add('lang-zh');
            }

            // Language toggle event
            languageToggleOld.addEventListener('click', (e) => {
                if (e.target.classList.contains('toggle-btn')) {
                    const targetLang = e.target.classList.contains('en') ? 'en' : 'zh';

                    // Update buttons
                    enBtn.classList.toggle('active', targetLang === 'en');
                    zhBtn.classList.toggle('active', targetLang === 'zh');

                    // Update body class
                    if (targetLang === 'en') {
                        document.body.classList.remove('lang-zh');
                    } else {
                        document.body.classList.add('lang-zh');
                    }

                    // Save preference
                    localStorage.setItem('llh-language', targetLang);
                }
            });
        }
    }
});

// Mobile hamburger menu
const hamburger = document.querySelector('.hamburger');
const navMobile = document.querySelector('.nav-mobile');

if (hamburger && navMobile) {
    hamburger.addEventListener('click', () => {
        navMobile.style.display = navMobile.style.display === 'flex' ? 'none' : 'flex';
        navMobile.style.flexDirection = 'column';
        navMobile.style.position = 'absolute';
        navMobile.style.top = '100%';
        navMobile.style.left = '0';
        navMobile.style.width = '100%';
        navMobile.style.background = 'white';
        navMobile.style.boxShadow = '0 4px 16px rgba(45, 106, 79, 0.15)';
        navMobile.style.padding = '1rem';
        navMobile.style.gap = '1rem';
    });
}

// Smooth scroll for anchor links
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                const headerOffset = 60; // Adjust based on header height
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });

                // Close mobile menu if open
                if (navMobile && navMobile.style.display === 'flex') {
                    navMobile.style.display = 'none';
                }
            }
        });
    });
});

// Activity filter functionality (if filters exist)
document.addEventListener('DOMContentLoaded', () => {
    const filters = document.querySelectorAll('.activity-filter');
    const activities = document.querySelectorAll('.activity');

    if (filters.length > 0 && activities.length > 0) {
        filters.forEach(filter => {
            filter.addEventListener('click', () => {
                // Remove active class from all filters
                filters.forEach(f => f.classList.remove('active'));

                // Add active class to the clicked filter
                filter.classList.add('active');

                const filterValue = filter.getAttribute('data-filter');

                // Show/hide activities based on filter
                activities.forEach(activity => {
                    if (filterValue === 'all' || activity.getAttribute('data-age') === filterValue) {
                        activity.style.display = 'block';
                    } else {
                        activity.style.display = 'none';
                    }
                });
            });
        });
    }
});
