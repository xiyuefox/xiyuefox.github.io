// ========================================
// DIALOGUE JOURNEY INTERACTIONS
// Pudding-inspired mother-baby conversation scrollytelling
// ========================================

// Wait for DOM to be ready
document.addEventListener('DOMContentLoaded', () => {
    initializeScrollAnimations();
    initializeTimelineTracking();
});

// ========================================
// SCROLL-TRIGGERED FADE-IN ANIMATIONS
// ========================================

function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.2,
        rootMargin: '0px 0px -100px 0px'
    };

    const fadeObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observe all fade-in elements
    const fadeElements = document.querySelectorAll('.fade-in-on-scroll');
    fadeElements.forEach(el => fadeObserver.observe(el));

    // Observe dialogue exchanges with staggered delays
    const dialogueExchanges = document.querySelectorAll('.dialogue-exchange');
    dialogueExchanges.forEach((exchange, index) => {
        // Add stagger delay based on position within scene
        const sceneExchanges = Array.from(exchange.parentElement.querySelectorAll('.dialogue-exchange'));
        const indexInScene = sceneExchanges.indexOf(exchange);
        exchange.style.transitionDelay = `${indexInScene * 0.2}s`;

        fadeObserver.observe(exchange);
    });
}

// ========================================
// TIMELINE PROGRESS TRACKING
// ========================================

let lastActiveAge = null;

function initializeTimelineTracking() {
    const scenes = document.querySelectorAll('.dialogue-scene');
    const timelineFill = document.getElementById('timelineFill');
    const stageMarkers = document.querySelectorAll('.stage-marker');

    // Map ages to progress percentages
    const ageToProgress = {
        '0m': 0,
        '3m': 25,
        '6m': 50,
        '12m': 75,
        '24m': 100
    };

    const sceneObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const sceneAge = entry.target.getAttribute('data-age');

                if (sceneAge && sceneAge !== lastActiveAge) {
                    lastActiveAge = sceneAge;

                    // Update progress bar
                    const progress = ageToProgress[sceneAge] || 0;
                    if (timelineFill) {
                        timelineFill.style.width = `${progress}%`;
                    }

                    // Update active marker
                    stageMarkers.forEach(marker => {
                        const markerAge = marker.getAttribute('data-age');
                        if (markerAge === sceneAge) {
                            marker.classList.add('active');
                        } else {
                            marker.classList.remove('active');
                        }
                    });

                    // Log for debugging
                    console.log(`📍 Now viewing: ${sceneAge} (${progress}% progress)`);
                }
            }
        });
    }, {
        threshold: 0.5
    });

    // Observe all dialogue scenes
    scenes.forEach(scene => sceneObserver.observe(scene));

    // Handle intro section separately
    const introSection = document.querySelector('.dialogue-intro');
    if (introSection) {
        const introObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if (timelineFill) {
                        timelineFill.style.width = '0%';
                    }
                    stageMarkers.forEach(marker => marker.classList.remove('active'));
                    lastActiveAge = null;
                }
            });
        }, { threshold: 0.3 });

        introObserver.observe(introSection);
    }
}

// ========================================
// SMOOTH SCROLL TO SECTIONS (Optional Enhancement)
// ========================================

// Allow clicking on stage markers to jump to that age
document.addEventListener('DOMContentLoaded', () => {
    const stageMarkers = document.querySelectorAll('.stage-marker');

    stageMarkers.forEach(marker => {
        marker.style.cursor = 'pointer';

        marker.addEventListener('click', () => {
            const targetAge = marker.getAttribute('data-age');
            const targetScene = document.querySelector(`[data-age="${targetAge}"]`);

            if (targetScene) {
                targetScene.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
            }
        });

        // Add hover hint
        marker.setAttribute('title', `Jump to ${marker.textContent}`);
    });
});

// ========================================
// SPEECH BUBBLE ANIMATIONS (Subtle pulse)
// ========================================

function addSpeechBubbleEffects() {
    const bubbles = document.querySelectorAll('.speech-bubble');

    bubbles.forEach((bubble, index) => {
        // Random subtle pulse animation
        const delay = Math.random() * 2;
        bubble.style.animationDelay = `${delay}s`;
    });
}

// Call after DOM loads
document.addEventListener('DOMContentLoaded', addSpeechBubbleEffects);

// ========================================
// TRACK USER ENGAGEMENT (Analytics-ready)
// ========================================

let viewedScenes = new Set();

function trackSceneView(sceneAge) {
    if (!viewedScenes.has(sceneAge)) {
        viewedScenes.add(sceneAge);
        console.log(`📊 User viewed scene: ${sceneAge}`);

        // This is where you'd send analytics events
        // Example: gtag('event', 'scene_view', { scene_age: sceneAge });
    }
}

// Integrate with scene observer
document.addEventListener('DOMContentLoaded', () => {
    const scenes = document.querySelectorAll('.dialogue-scene');

    const trackingObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const sceneAge = entry.target.getAttribute('data-age');
                if (sceneAge) {
                    trackSceneView(sceneAge);
                }
            }
        });
    }, {
        threshold: 0.3
    });

    scenes.forEach(scene => trackingObserver.observe(scene));
});

// ========================================
// PERFORMANCE OPTIMIZATION
// ========================================

// Reduce animations on low-end devices
if (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 2) {
    document.body.style.setProperty('--animation-duration', '0.3s');
    console.log('⚡ Reduced animation complexity for performance');
}

// ========================================
// SCROLL PROGRESS INDICATOR (Alternative visualization)
// ========================================

function updateScrollProgress() {
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrolled = window.scrollY;
    const progress = (scrolled / scrollHeight) * 100;

    // Could be used for an additional progress bar if needed
    // For now, just log it
    if (scrolled / scrollHeight > 0.9) {
        console.log('🎉 User reached the end of the dialogue journey!');
    }
}

// Throttled scroll listener
let scrollTimeout;
window.addEventListener('scroll', () => {
    if (scrollTimeout) {
        window.cancelAnimationFrame(scrollTimeout);
    }

    scrollTimeout = window.requestAnimationFrame(() => {
        updateScrollProgress();
    });
});

// ========================================
// EASTER EGG: Konami Code for Fun Stats
// ========================================

let konamiCode = [];
const konamiSequence = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];

document.addEventListener('keydown', (e) => {
    konamiCode.push(e.key);
    konamiCode = konamiCode.slice(-10);

    if (konamiCode.join(',') === konamiSequence.join(',')) {
        showEasterEgg();
    }
});

function showEasterEgg() {
    const stats = `
🎉 SECRET STATS UNLOCKED! 🎉

📊 Your Journey Stats:
- Scenes viewed: ${viewedScenes.size}/5
- Scroll depth: ${Math.round((window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100)}%
- Time on page: ${Math.round(performance.now() / 1000)}s

💡 Fun Facts:
- Babies learn ~1 word per 2 waking hours (18-24m)
- By age 2, vocabulary ranges from 50-300+ words
- Every responsive interaction builds neural pathways!

Thanks for being curious about early childhood development! 🌱
    `;

    alert(stats);
}

// ========================================
// INITIALIZATION COMPLETE
// ========================================

console.log('👩‍🍼 Dialogue Journey initialized!');
console.log('Scroll to experience the mother-baby communication evolution');
console.log('💡 Tip: Click on age markers in the timeline to jump to scenes');
