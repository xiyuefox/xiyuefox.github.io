// ========================================
// BABY TIME TRAVEL - PUDDING-STYLE INTERACTIONS
// Scroll-driven dialogue between pregnant mom and future baby
// ========================================

// Character data for detail panel
const characterData = {
    mom: {
        name: 'Lily Chen',
        time: 'October 2024',
        status: '6 months pregnant',
        age: '32 years old',
        occupation: 'Graphic Designer',
        location: 'San Francisco, CA',
        feelings: 'Excited, nervous, googling everything',
        favoriteActivity: 'Talking to the bump, eating ice cream',
        worries: 'Will I be a good mom? Why is pregnancy so weird?',
        hopes: 'That my baby will be healthy and happy',
        funFact: 'Has read 47 pregnancy books and still feels unprepared'
    },
    baby: {
        name: 'Emma Chen',
        time: 'October 2025',
        status: '1 year old',
        age: '12 months',
        favoriteWord: 'Mama (and also "NO")',
        favoriteFood: 'Whatever Mom is eating, but smashed',
        skills: 'Walking (wobbling), talking (babbling), causing chaos',
        sleep: '...let\'s not talk about sleep',
        personality: 'Curious, giggly, surprisingly opinionated',
        funFact: 'Has already mastered puppy-dog eyes to get what she wants'
    }
};

// ========================================
// SCROLL TRACKING & SCENE ACTIVATION
// ========================================

let currentScene = -1;

function initializeScrollTracking() {
    const sections = document.querySelectorAll('.dialogue-section');
    const timeline = document.getElementById('timeline');
    const timelineMarkers = timeline.querySelectorAll('.timeline-marker');
    const avatarMom = document.getElementById('avatarMom');
    const avatarBaby = document.getElementById('avatarBaby');

    // IntersectionObserver for dialogue bubbles
    const observerOptions = {
        threshold: 0.5,
        rootMargin: '0px 0px -200px 0px'
    };

    const dialogueObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Fade in the dialogue bubble
                entry.target.querySelector('.dialogue-bubble').classList.add('visible');

                // Update current scene
                const sceneIndex = parseInt(entry.target.getAttribute('data-scene'));
                if (sceneIndex !== currentScene) {
                    currentScene = sceneIndex;
                    updateTimeline(sceneIndex);

                    // Update avatar highlighting
                    const speaker = entry.target.getAttribute('data-speaker');
                    updateSpeaker(speaker);
                }
            }
        });
    }, observerOptions);

    // Observe all dialogue sections
    sections.forEach(section => {
        dialogueObserver.observe(section);
    });

    // Timeline marker click events
    timelineMarkers.forEach((marker, index) => {
        marker.addEventListener('click', () => {
            // Find corresponding section (accounting for paired sections)
            const targetSection = Array.from(sections).find(section => {
                const sceneIndex = parseInt(section.getAttribute('data-scene'));
                return sceneIndex === index || sceneIndex === index + 1;
            });

            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'center'
                });
            }
        });
    });
}

function updateTimeline(sceneIndex) {
    const timelineMarkers = document.querySelectorAll('.timeline-marker');
    timelineMarkers.forEach((marker, index) => {
        if (index === sceneIndex || index === Math.floor(sceneIndex / 2)) {
            marker.classList.add('active');
        } else {
            marker.classList.remove('active');
        }
    });
}

function updateSpeaker(speaker) {
    const avatarMom = document.getElementById('avatarMom');
    const avatarBaby = document.getElementById('avatarBaby');

    if (speaker === 'mom') {
        avatarMom.classList.add('speaking');
        avatarBaby.classList.remove('speaking');
    } else if (speaker === 'baby') {
        avatarBaby.classList.add('speaking');
        avatarMom.classList.remove('speaking');
    }
}

// ========================================
// AVATAR CLICK - DETAIL PANEL
// ========================================

function initializeAvatarClicks() {
    const avatarMom = document.getElementById('avatarMom');
    const avatarBaby = document.getElementById('avatarBaby');
    const detailPanel = document.getElementById('detailPanel');
    const closePanel = document.getElementById('closePanel');
    const detailContent = document.getElementById('detailContent');

    // Mom avatar click
    avatarMom.addEventListener('click', () => {
        showDetailPanel('mom');
    });

    // Baby avatar click
    avatarBaby.addEventListener('click', () => {
        showDetailPanel('baby');
    });

    // Close button
    closePanel.addEventListener('click', () => {
        detailPanel.classList.remove('open');
    });

    // Close on background click
    detailPanel.addEventListener('click', (e) => {
        if (e.target === detailPanel) {
            detailPanel.classList.remove('open');
        }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && detailPanel.classList.contains('open')) {
            detailPanel.classList.remove('open');
        }
    });
}

function showDetailPanel(character) {
    const detailPanel = document.getElementById('detailPanel');
    const detailContent = document.getElementById('detailContent');
    const data = characterData[character];

    if (character === 'mom') {
        detailContent.innerHTML = `
            <h2>👩 ${data.name}</h2>
            <div class="detail-item">
                <div class="detail-label">Time</div>
                <div class="detail-value">${data.time}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Status</div>
                <div class="detail-value">${data.status}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Age</div>
                <div class="detail-value">${data.age}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Occupation</div>
                <div class="detail-value">${data.occupation}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Location</div>
                <div class="detail-value">${data.location}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Current Feelings</div>
                <div class="detail-value">${data.feelings}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Favorite Activity</div>
                <div class="detail-value">${data.favoriteActivity}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Biggest Worries</div>
                <div class="detail-value">${data.worries}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Hopes for Baby</div>
                <div class="detail-value">${data.hopes}</div>
            </div>
            <div class="detail-item" style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1);">
                <div class="detail-label">Fun Fact</div>
                <div class="detail-value">${data.funFact}</div>
            </div>
        `;
    } else {
        detailContent.innerHTML = `
            <h2>👶 ${data.name}</h2>
            <div class="detail-item">
                <div class="detail-label">Time</div>
                <div class="detail-value">${data.time}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Status</div>
                <div class="detail-value">${data.status}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Age</div>
                <div class="detail-value">${data.age}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Favorite Word</div>
                <div class="detail-value">${data.favoriteWord}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Favorite Food</div>
                <div class="detail-value">${data.favoriteFood}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Skills</div>
                <div class="detail-value">${data.skills}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Sleep Schedule</div>
                <div class="detail-value">${data.sleep}</div>
            </div>
            <div class="detail-item">
                <div class="detail-label">Personality</div>
                <div class="detail-value">${data.personality}</div>
            </div>
            <div class="detail-item" style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1);">
                <div class="detail-label">Fun Fact</div>
                <div class="detail-value">${data.funFact}</div>
            </div>
        `;
    }

    detailPanel.classList.add('open');
}

// ========================================
// SMOOTH SCROLL PROGRESS
// ========================================

function initializeSmoothScrollEffects() {
    let ticking = false;

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                updateScrollEffects();
                ticking = false;
            });
            ticking = true;
        }
    });
}

function updateScrollEffects() {
    // Could add parallax or other scroll effects here
    // For now, keeping it simple like Pudding
}

// ========================================
// KEYBOARD SHORTCUTS
// ========================================

function initializeKeyboardShortcuts() {
    document.addEventListener('keydown', (e) => {
        // Arrow down: scroll to next section
        if (e.key === 'ArrowDown' && !e.shiftKey && !e.ctrlKey && !e.metaKey) {
            e.preventDefault();
            scrollToNextSection();
        }

        // Arrow up: scroll to previous section
        if (e.key === 'ArrowUp' && !e.shiftKey && !e.ctrlKey && !e.metaKey) {
            e.preventDefault();
            scrollToPreviousSection();
        }
    });
}

function scrollToNextSection() {
    const sections = Array.from(document.querySelectorAll('.dialogue-section'));
    const viewportCenter = window.innerHeight / 2;

    for (let section of sections) {
        const rect = section.getBoundingClientRect();
        if (rect.top > viewportCenter) {
            section.scrollIntoView({ behavior: 'smooth', block: 'center' });
            break;
        }
    }
}

function scrollToPreviousSection() {
    const sections = Array.from(document.querySelectorAll('.dialogue-section')).reverse();
    const viewportCenter = window.innerHeight / 2;

    for (let section of sections) {
        const rect = section.getBoundingClientRect();
        if (rect.bottom < viewportCenter) {
            section.scrollIntoView({ behavior: 'smooth', block: 'center' });
            break;
        }
    }
}

// ========================================
// EAGER LOADING OF NEXT DIALOGUE
// ========================================

function initializeEagerLoading() {
    const sections = document.querySelectorAll('.dialogue-section');

    const loadObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Pre-load animations for next section
                const nextSection = entry.target.nextElementSibling;
                if (nextSection && nextSection.classList.contains('dialogue-section')) {
                    nextSection.querySelector('.dialogue-bubble')?.classList.add('preload');
                }
            }
        });
    }, {
        rootMargin: '500px'
    });

    sections.forEach(section => loadObserver.observe(section));
}

// ========================================
// PUDDING-INSPIRED ENHANCEMENTS
// ========================================

function initializeEnhancementAnimations() {
    // Observe data callouts
    const dataCallouts = document.querySelectorAll('.data-callout');
    const reflectivePrompts = document.querySelectorAll('.reflective-prompt');
    const sceneDividers = document.querySelectorAll('.scene-divider');
    const developmentCharts = document.querySelectorAll('.development-chart');
    const shareSections = document.querySelectorAll('.share-section');

    const enhancementObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.3,
        rootMargin: '0px 0px -100px 0px'
    });

    // Observe all enhancement elements
    dataCallouts.forEach(el => enhancementObserver.observe(el));
    reflectivePrompts.forEach(el => enhancementObserver.observe(el));
    sceneDividers.forEach(el => enhancementObserver.observe(el));
    developmentCharts.forEach(el => enhancementObserver.observe(el));
    shareSections.forEach(el => enhancementObserver.observe(el));

    console.log(`📊 Enhanced with ${dataCallouts.length} data callouts, ${reflectivePrompts.length} reflective prompts, ${developmentCharts.length} charts`);
}

// ========================================
// INTERACTIVE MILESTONE CARDS
// ========================================

const milestoneDetails = {
    '0': {
        title: 'Birth: Voice Recognition',
        detail: 'Newborns can recognize their mother\'s voice within hours of birth. They prefer her voice over any other!'
    },
    '3': {
        title: '3 Months: Social Smiles',
        detail: 'At 3 months, babies start smiling in response to social interaction, not just reflexively.'
    },
    '6': {
        title: '6 Months: Solid Foods',
        detail: 'Around 6 months, babies develop the motor skills and digestive capacity for solid foods!'
    },
    '9': {
        title: '9 Months: First Words',
        detail: 'Most babies say their first recognizable word between 9-14 months. "Mama" and "Dada" are most common!'
    },
    '12': {
        title: '12 Months: First Steps',
        detail: 'By their first birthday, many babies take their first independent steps. Walking marks huge brain development!'
    }
};

function initializeMilestoneCards() {
    const milestoneCards = document.querySelectorAll('.milestone-card');

    milestoneCards.forEach(card => {
        card.addEventListener('click', () => {
            const month = card.getAttribute('data-month');
            const details = milestoneDetails[month];

            if (details) {
                alert(`🎉 ${details.title}\n\n${details.detail}`);
            }
        });
    });

    console.log(`🎯 ${milestoneCards.length} milestone cards initialized`);
}

// ========================================
// SOCIAL SHARING FUNCTIONALITY
// ========================================

function initializeSocialSharing() {
    const shareTwitter = document.getElementById('shareTwitter');
    const shareFacebook = document.getElementById('shareFacebook');
    const shareCopy = document.getElementById('shareCopy');

    const pageUrl = encodeURIComponent(window.location.href);
    const pageTitle = encodeURIComponent('A Conversation Across Time - Mom & Baby Interactive Story');
    const pageDescription = encodeURIComponent('Experience a heartwarming dialogue between a pregnant mother and her future baby!');

    // Twitter share
    if (shareTwitter) {
        shareTwitter.href = `https://twitter.com/intent/tweet?text=${pageTitle}&url=${pageUrl}`;
        shareTwitter.target = '_blank';
    }

    // Facebook share
    if (shareFacebook) {
        shareFacebook.href = `https://www.facebook.com/sharer/sharer.php?u=${pageUrl}`;
        shareFacebook.target = '_blank';
    }

    // Copy link
    if (shareCopy) {
        shareCopy.addEventListener('click', async (e) => {
            e.preventDefault();
            try {
                await navigator.clipboard.writeText(window.location.href);
                const originalText = shareCopy.innerHTML;
                shareCopy.innerHTML = '<span>✅</span> Link Copied!';
                shareCopy.style.borderColor = 'rgba(100, 255, 150, 0.8)';

                setTimeout(() => {
                    shareCopy.innerHTML = originalText;
                    shareCopy.style.borderColor = '';
                }, 2000);
            } catch (err) {
                console.error('Failed to copy:', err);
                alert('Link: ' + window.location.href);
            }
        });
    }

    console.log('📤 Social sharing initialized');
}

// ========================================
// EASTER EGG: KONAMI CODE
// ========================================

let konamiSequence = [];
const konamiCode = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];

function initializeKonamiCode() {
    document.addEventListener('keydown', (e) => {
        konamiSequence.push(e.key);
        konamiSequence = konamiSequence.slice(-10);

        if (konamiSequence.join(',') === konamiCode.join(',')) {
            activateEasterEgg();
        }
    });
}

function activateEasterEgg() {
    alert(`🎉 SECRET UNLOCKED!

Fun Facts:
- Babies can hear in the womb starting around week 18
- They can recognize mom's voice at birth
- By 1 year, they understand 50+ words
- They say their first word around 12 months
- A baby's brain triples in size in the first year!

Thanks for scrolling through this time-travel story! 👶✨`);
}

// ========================================
// ANALYTICS TRACKING (READY FOR INTEGRATION)
// ========================================

function trackSceneView(sceneIndex) {
    console.log(`📊 Scene ${sceneIndex} viewed`);
    // Example: gtag('event', 'scene_view', { scene_index: sceneIndex });
}

function trackAvatarClick(character) {
    console.log(`👤 Avatar clicked: ${character}`);
    // Example: gtag('event', 'avatar_click', { character: character });
}

// ========================================
// INITIALIZATION
// ========================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('👶 Baby Time Travel - Initializing...');

    initializeScrollTracking();
    initializeAvatarClicks();
    initializeSmoothScrollEffects();
    initializeKeyboardShortcuts();
    initializeEagerLoading();
    initializeEnhancementAnimations(); // Pudding-inspired enhancements
    initializeMilestoneCards(); // NEW: Interactive milestone chart
    initializeSocialSharing(); // NEW: Social media sharing
    initializeKonamiCode();

    console.log('✨ All systems go! Scroll to begin the journey.');
    console.log('💡 Tip: Click on Lily or Emma to learn more about them!');
    console.log('⌨️  Use Arrow Up/Down to navigate between scenes');
    console.log('🎯 Click milestone cards to see development details!');
});

// ========================================
// PERFORMANCE MONITORING
// ========================================

window.addEventListener('load', () => {
    const loadTime = performance.now();
    console.log(`⚡ Page loaded in ${Math.round(loadTime)}ms`);

    // Track scroll depth
    let maxScroll = 0;
    window.addEventListener('scroll', () => {
        const scrollPercent = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
        if (scrollPercent > maxScroll) {
            maxScroll = scrollPercent;
            if (scrollPercent > 90) {
                console.log('🎉 User reached the end!');
            }
        }
    });
});
