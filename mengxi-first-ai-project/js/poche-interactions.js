/**
 * 🎮 POCHE-STYLE INTERACTIVE JS
 * Fun, playful interactions for blog
 */

document.addEventListener('DOMContentLoaded', () => {
    initCursorFollower();
    initFloatingElements();
    initCardEffects();
    initThemeToggle();
    initLoader();
});

// ============================================
// 🎯 CUSTOM CURSOR FOLLOWER
// ============================================

function initCursorFollower() {
    // Skip on touch devices
    if ('ontouchstart' in window) return;

    const cursor = document.createElement('div');
    cursor.className = 'cursor-follower';
    document.body.appendChild(cursor);

    // Create trail elements
    const trails = [];
    const trailCount = 5;
    for (let i = 0; i < trailCount; i++) {
        const trail = document.createElement('div');
        trail.className = 'cursor-trail';
        trail.style.opacity = (1 - i / trailCount) * 0.4;
        document.body.appendChild(trail);
        trails.push({ el: trail, x: 0, y: 0 });
    }

    let mouseX = 0, mouseY = 0;
    let cursorX = 0, cursorY = 0;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
    });

    document.addEventListener('mouseover', (e) => {
        if (e.target.closest('.poche-card') ||
            e.target.closest('.poche-nav-link') ||
            e.target.closest('.poche-btn')) {
            cursor.classList.add('hover');
        } else {
            cursor.classList.remove('hover');
        }
    });

    function animateCursor() {
        // Smooth cursor following
        cursorX += (mouseX - cursorX) * 0.15;
        cursorY += (mouseY - cursorY) * 0.15;

        cursor.style.left = cursorX + 'px';
        cursor.style.top = cursorY + 'px';

        // Trail following with delay
        trails.forEach((trail, index) => {
            const targetTrail = trails[index - 1] || { x: cursorX, y: cursorY };
            trail.x += (targetTrail.x - trail.x) * 0.2;
            trail.y += (targetTrail.y - trail.y) * 0.2;
            trail.el.style.left = trail.x + 'px';
            trail.el.style.top = trail.y + 'px';
        });

        requestAnimationFrame(animateCursor);
    }

    animateCursor();
}

// ============================================
// 🎈 FLOATING DECORATIONS
// ============================================

function initFloatingElements() {
    const container = document.createElement('div');
    container.className = 'floating-elements';
    document.body.appendChild(container);

    const emojis = ['🌸', '⭐', '🎨', '📚', '💫', '🚀', '💡', '🎯', '🌈', '🔮'];

    emojis.forEach((emoji, index) => {
        const item = document.createElement('div');
        item.className = 'float-item';
        item.textContent = emoji;
        item.style.left = Math.random() * 90 + '%';
        item.style.top = Math.random() * 80 + 10 + '%';
        item.style.animationDelay = `-${Math.random() * 10}s`;
        item.style.animationDuration = `${15 + Math.random() * 15}s`;
        container.appendChild(item);
    });

    // Add click interaction to float items
    document.querySelectorAll('.float-item').forEach(item => {
        item.style.pointerEvents = 'auto';
        item.style.cursor = 'pointer';
        item.addEventListener('click', () => {
            item.style.transform = 'scale(2) rotate(360deg)';
            item.style.opacity = '0';
            setTimeout(() => {
                item.style.transform = '';
                item.style.opacity = '0.6';
            }, 500);
        });
    });
}

// ============================================
// 📦 CARD EFFECTS
// ============================================

function initCardEffects() {
    const cards = document.querySelectorAll('.poche-card');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
        });
    });

    // Staggered reveal animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, index * 50);
            }
        });
    }, { threshold: 0.1 });

    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(card);
    });
}

// ============================================
// 🎨 THEME TOGGLE
// ============================================

function initThemeToggle() {
    const THEME_KEY = 'poche-theme';
    const themes = ['light', 'dark', 'retro'];
    const themeIcons = {
        light: '🌞',
        dark: '🌙',
        retro: '🕹️'
    };

    function getSavedTheme() {
        return localStorage.getItem(THEME_KEY) || 'light';
    }

    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem(THEME_KEY, theme);

        const toggle = document.getElementById('poche-theme-toggle');
        if (toggle) {
            toggle.textContent = themeIcons[theme];
        }
    }

    // Create custom toggle button
    const existingToggle = document.getElementById('theme-toggle');
    if (existingToggle) {
        existingToggle.style.display = 'none';
    }

    const nav = document.querySelector('.poche-nav') || document.querySelector('.hn-nav');
    if (nav) {
        const toggleBtn = document.createElement('button');
        toggleBtn.id = 'poche-theme-toggle';
        toggleBtn.className = 'poche-theme-toggle';
        toggleBtn.textContent = themeIcons[getSavedTheme()];
        toggleBtn.ariaLabel = 'Toggle theme';
        nav.appendChild(toggleBtn);

        toggleBtn.addEventListener('click', () => {
            const current = getSavedTheme();
            const currentIndex = themes.indexOf(current);
            const nextTheme = themes[(currentIndex + 1) % themes.length];

            // Animate theme transition
            toggleBtn.style.transform = 'rotate(360deg) scale(0.8)';
            setTimeout(() => {
                setTheme(nextTheme);
                toggleBtn.style.transform = '';
            }, 200);
        });

        // Keyboard shortcut
        document.addEventListener('keydown', (e) => {
            if (e.key.toLowerCase() === 't' && !['input', 'textarea'].includes(document.activeElement.tagName.toLowerCase())) {
                const current = getSavedTheme();
                const currentIndex = themes.indexOf(current);
                const nextTheme = themes[(currentIndex + 1) % themes.length];
                setTheme(nextTheme);
            }
        });
    }

    setTheme(getSavedTheme());
}

// ============================================
// 🚀 LOADING ANIMATION
// ============================================

function initLoader() {
    const loader = document.createElement('div');
    loader.className = 'poche-loader';
    loader.innerHTML = `
        <div class="poche-loader-content">
            <div class="poche-loader-bounce">
                <span></span>
                <span></span>
                <span></span>
            </div>
            <span class="poche-loader-text">Loading your adventure...</span>
        </div>
    `;
    document.body.appendChild(loader);

    setTimeout(() => {
        loader.classList.add('hidden');
        setTimeout(() => loader.remove(), 500);
    }, 800);
}

// ============================================
// 🔍 ENHANCED SEARCH
// ============================================

function enhanceSearch() {
    const searchInput = document.querySelector('.hn-search-input') || document.querySelector('.poche-search');
    if (!searchInput) return;

    // Add sound effect placeholder
    searchInput.addEventListener('focus', () => {
        // Could add a subtle sound here
        searchInput.parentElement.style.transform = 'scale(1.02)';
    });

    searchInput.addEventListener('blur', () => {
        searchInput.parentElement.style.transform = '';
    });
}

// ============================================
// 📊 PARTICLE EFFECT ON CLICK
// ============================================

document.addEventListener('click', (e) => {
    createParticleBurst(e.clientX, e.clientY);
});

function createParticleBurst(x, y) {
    const colors = ['#ff6b6b', '#4ecdc4', '#a855f7', '#ffd93d', '#ff6b9d'];

    for (let i = 0; i < 8; i++) {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: fixed;
            left: ${x}px;
            top: ${y}px;
            width: 8px;
            height: 8px;
            background: ${colors[Math.floor(Math.random() * colors.length)]};
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            transition: all 0.5s ease-out;
        `;
        document.body.appendChild(particle);

        const angle = (i / 8) * Math.PI * 2;
        const distance = 30 + Math.random() * 30;
        const endX = Math.cos(angle) * distance;
        const endY = Math.sin(angle) * distance;

        requestAnimationFrame(() => {
            particle.style.transform = `translate(${endX}px, ${endY}px) scale(0)`;
            particle.style.opacity = '0';
        });

        setTimeout(() => particle.remove(), 500);
    }
}

// ============================================
// 📜 SCROLL PROGRESS WITH POCHE STYLE
// ============================================

const progressBar = document.createElement('div');
progressBar.style.cssText = `
    position: fixed;
    top: 0;
    left: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--poche-accent), var(--poche-pink));
    z-index: 10000;
    transition: width 0.1s ease;
`;
document.body.appendChild(progressBar);

window.addEventListener('scroll', () => {
    const scrollTop = document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (scrollTop / scrollHeight) * 100;
    progressBar.style.width = progress + '%';
});

// ============================================
// 🎲 RANDOM FUN FACTS
// ============================================

const funFacts = [
    'Did you know? 🤔',
    'Keep exploring! 🗺️',
    'You\'re doing great! ⭐',
    'Stay curious! 💡',
    'Knowledge is power! 📚',
    'Almost there! 🎯',
];

function showRandomFact() {
    const fact = funFacts[Math.floor(Math.random() * funFacts.length)];
    console.log(fact);
}

// ============================================
// 🎪 UTILITY FUNCTIONS
// ============================================

// Debounce function for performance
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Random number in range
function randomRange(min, max) {
    return Math.random() * (max - min) + min;
}

// Random element from array
function randomChoice(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

// Export for use in other scripts
window.Poche = {
    createParticleBurst,
    randomRange,
    randomChoice,
    funFacts
};
