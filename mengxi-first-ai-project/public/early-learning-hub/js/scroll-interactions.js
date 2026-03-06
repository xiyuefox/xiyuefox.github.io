// ========================================
// SCROLL-TRIGGERED INTERACTIONS
// Pudding-inspired scrollytelling and interactive elements
// ========================================

// Principle detail data
const principleData = {
    genetics: {
        icon: '🧬',
        title: '50% + 50%',
        subtitle: 'Nature and Nurture',
        description: 'Genetics determine about 50% of a child\'s potential, while environment shapes the other 50%. This means you have enormous influence!',
        sections: [
            {
                title: '💡 What This Means',
                items: [
                    'Your child\'s potential is not fixed at birth',
                    'Quality interactions create new neural pathways',
                    'Every conversation literally shapes their brain',
                    'Early experiences have compounding effects'
                ]
            },
            {
                title: '🎯 Action Steps',
                items: [
                    'Create a language-rich environment',
                    'Respond to your baby\'s coos and babbles',
                    'Read books together daily',
                    'Limit screen time, maximize face time'
                ]
            }
        ],
        stats: {
            number: '700+',
            label: 'New neural connections per second (age 0-3)'
        }
    },
    play: {
        icon: '🎮',
        title: 'Play = Learning',
        subtitle: 'Free Play is Powerful',
        description: 'Research shows free play is more effective than structured learning programs for young children. Play IS the work of childhood.',
        sections: [
            {
                title: '💡 Why Play Matters',
                items: [
                    'Develops executive function (self-control)',
                    'Builds creativity and problem-solving',
                    'Teaches social-emotional skills',
                    'Reduces stress and builds resilience'
                ]
            },
            {
                title: '🎯 Types of Play',
                items: [
                    'Pretend play: boosts abstract thinking',
                    'Physical play: develops motor skills',
                    'Object play: enhances spatial reasoning',
                    'Social play: teaches cooperation'
                ]
            }
        ],
        stats: {
            number: '2-3x',
            label: 'Better self-control from play vs. structured learning'
        }
    },
    emotion: {
        icon: '❤️',
        title: 'Emotion First',
        subtitle: 'Connect Before You Correct',
        description: 'When children are upset, their prefrontal cortex goes "offline." You must help them regulate emotions before teaching can happen.',
        sections: [
            {
                title: '💡 Brain Science',
                items: [
                    'Stress hormones block learning',
                    'Emotional safety enables exploration',
                    'Secure attachment predicts academic success',
                    'Co-regulation teaches self-regulation'
                ]
            },
            {
                title: '🎯 How to Connect',
                items: [
                    'Name their feelings: "You\'re frustrated"',
                    'Get down to their eye level',
                    'Use calm, warm tone of voice',
                    'Teach after calm is restored'
                ]
            }
        ],
        stats: {
            number: '10x',
            label: 'More effective to teach after emotional connection'
        }
    },
    interaction: {
        icon: '👀',
        title: 'Interaction',
        subtitle: 'Face Time Beats Screen Time',
        description: 'Language learning requires live, interactive communication. No screen-based program can replicate the benefits of face-to-face interaction.',
        sections: [
            {
                title: '💡 Research Findings',
                items: [
                    'Babies learn ZERO words from TV (under 2)',
                    'Each hour of TV = 1,000 fewer words learned',
                    'Each hour with people = 1,000 more words',
                    'Quality of interaction matters more than quantity'
                ]
            },
            {
                title: '🎯 Maximize Interaction',
                items: [
                    'Narrate your activities together',
                    'Follow your child\'s interests',
                    'Use "serve and return" conversations',
                    'Respond to their attempts to communicate'
                ]
            }
        ],
        stats: {
            number: '30M',
            label: 'Word gap by age 3 (high vs. low interaction)'
        }
    }
};

// Age detail data
const ageData = {
    '0-1': {
        icon: '👶',
        title: '0-1 Years',
        subtitle: 'Foundation Building',
        description: 'The first year is all about sensory exploration and attachment. Your responsive care literally shapes brain architecture.',
        sections: [
            {
                title: '⭐ Key Milestones',
                items: [
                    'Social smile by 2 months',
                    'Reaches for objects by 4 months',
                    'Sits without support by 6 months',
                    'First words by 12 months'
                ]
            },
            {
                title: '🎯 Focus Areas',
                items: [
                    'Secure attachment through responsiveness',
                    'Tummy time for motor development',
                    'Face-to-face interaction for language',
                    'Safe exploration of textures and sounds'
                ]
            },
            {
                title: '📚 Recommended Activities',
                items: [
                    'Peek-a-boo games',
                    'High-contrast books',
                    'Singing and talking',
                    'Gentle physical play'
                ]
            }
        ],
        stats: {
            number: '8,000',
            label: 'Neural connections per second'
        }
    },
    '1-2': {
        icon: '🚼',
        title: '1-2 Years',
        subtitle: 'Language Explosion',
        description: 'Toddlers learn a new word approximately every 2 hours they\'re awake. This is the golden age for language development.',
        sections: [
            {
                title: '⭐ Key Milestones',
                items: [
                    'Walks independently',
                    'Says 10-20 words by 18 months',
                    'Points to objects when named',
                    'Follows simple instructions'
                ]
            },
            {
                title: '🎯 Focus Areas',
                items: [
                    'Rich language input (talk constantly!)',
                    'Reading picture books together',
                    'Encouraging safe exploration',
                    'Setting consistent routines'
                ]
            },
            {
                title: '⚠️ Common Concerns',
                items: [
                    'Tantrums are normal (emotional regulation developing)',
                    'Not sharing is developmental (building self-concept)',
                    'Picky eating is common (offer variety, no pressure)'
                ]
            }
        ],
        stats: {
            number: '1 word/2hrs',
            label: 'Rate of vocabulary growth'
        }
    },
    '2-3': {
        icon: '🧒',
        title: '2-3 Years',
        subtitle: 'The "Terrible Twos"',
        description: 'This phase isn\'t about being difficult—it\'s about developing autonomy and self-awareness. The "No!" phase is healthy.',
        sections: [
            {
                title: '⭐ Key Milestones',
                items: [
                    'Uses 2-3 word sentences',
                    'Runs and jumps confidently',
                    'Plays alongside other children',
                    'Begins toilet training readiness'
                ]
            },
            {
                title: '🎯 Focus Areas',
                items: [
                    'Provide choices (within limits)',
                    'Support autonomy: "You do it!"',
                    'Emotion coaching during meltdowns',
                    'Pretend play and creativity'
                ]
            },
            {
                title: '💪 Building Skills',
                items: [
                    'Self-help skills (dressing, feeding)',
                    'Emotional vocabulary',
                    'Turn-taking in games',
                    'Following 2-step directions'
                ]
            }
        ],
        stats: {
            number: '200-300',
            label: 'Words in vocabulary by age 2'
        }
    },
    '3-5': {
        icon: '👧',
        title: '3-5 Years',
        subtitle: 'Executive Function Development',
        description: 'Self-control develops rapidly in these years and predicts success better than IQ. Focus on executive function skills.',
        sections: [
            {
                title: '⭐ Key Milestones',
                items: [
                    'Speaks in complete sentences',
                    'Draws recognizable shapes',
                    'Plays cooperatively with peers',
                    'Shows creativity and imagination'
                ]
            },
            {
                title: '🎯 Executive Function Skills',
                items: [
                    'Working memory: "Simon Says" games',
                    'Cognitive flexibility: "Opposite game"',
                    'Inhibitory control: "Red light, green light"',
                    'Planning: simple cooking or building projects'
                ]
            },
            {
                title: '🎓 Pre-Academic Skills',
                items: [
                    'Letter and number recognition (if interested)',
                    'Storytelling and comprehension',
                    'Pattern recognition',
                    'Social problem-solving'
                ]
            }
        ],
        stats: {
            number: '2x',
            label: 'Self-control predicts success better than IQ'
        }
    }
};

// ========================================
// SCROLL OBSERVER FOR FADE-IN ANIMATIONS
// ========================================

const observerOptions = {
    threshold: 0.15,
    rootMargin: '0px 0px -100px 0px'
};

const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

// Observe all fade-in elements and setup timeline after DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    // Fade-in animations
    const fadeElements = document.querySelectorAll('.fade-in-scroll');
    fadeElements.forEach(el => fadeObserver.observe(el));

    // ========================================
    // PROGRESS TIMELINE TRACKING
    // ========================================

    const sections = document.querySelectorAll('.scroll-section');
    const timelineMarkers = document.querySelectorAll('.timeline-marker');

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const sectionId = entry.target.getAttribute('data-section');

                // Update active marker
                timelineMarkers.forEach(marker => {
                    if (marker.getAttribute('data-section') === sectionId) {
                        marker.classList.add('active');
                    } else {
                        marker.classList.remove('active');
                    }
                });
            }
        });
    }, {
        threshold: 0.5
    });

    sections.forEach(section => sectionObserver.observe(section));

    // Click timeline markers to scroll to sections
    timelineMarkers.forEach(marker => {
        marker.addEventListener('click', () => {
            const sectionId = marker.getAttribute('data-section');
            const section = document.querySelector(`[data-section="${sectionId}"]`);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    });
});

// ========================================
// DETAIL PANEL FUNCTIONS
// ========================================

function openDetailPanel() {
    const panel = document.getElementById('detailPanel');
    panel.classList.add('open');
    document.body.style.overflow = 'hidden'; // Prevent background scroll
}

function closeDetailPanel() {
    const panel = document.getElementById('detailPanel');
    panel.classList.remove('open');
    document.body.style.overflow = ''; // Restore scroll
}

function showPrincipleDetail(principleId) {
    const data = principleData[principleId];
    if (!data) return;

    const content = `
        <div class="panel-header">
            <div class="panel-icon">${data.icon}</div>
            <h2 class="panel-title">${data.title}</h2>
            <p class="panel-subtitle">${data.subtitle}</p>
        </div>
        
        <p style="color: var(--text-primary); line-height: 1.7; margin-bottom: 1.5rem;">
            ${data.description}
        </p>
        
        ${data.sections.map(section => `
            <div class="panel-section">
                <h4>${section.title}</h4>
                <ul>
                    ${section.items.map(item => `<li>${item}</li>`).join('')}
                </ul>
            </div>
        `).join('')}
        
        <div class="stat-highlight">
            <div class="stat-number">${data.stats.number}</div>
            <div class="stat-label">${data.stats.label}</div>
        </div>
        
        <div style="margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid #E9ECEF;">
            <p style="font-size: 0.9rem; color: var(--text-secondary);">
                💡 Want to dive deeper? Explore our <a href="books.html" style="color: var(--primary); text-decoration: underline;">recommended books</a> 
                or ask our <a href="tutor.html" style="color: var(--primary); text-decoration: underline;">AI tutor</a>.
            </p>
        </div>
    `;

    document.getElementById('panelContent').innerHTML = content;
    openDetailPanel();
}

function showAgeDetail(ageId) {
    const data = ageData[ageId];
    if (!data) return;

    const content = `
        <div class="panel-header">
            <div class="panel-icon">${data.icon}</div>
            <h2 class="panel-title">${data.title}</h2>
            <p class="panel-subtitle">${data.subtitle}</p>
        </div>
        
        <p style="color: var(--text-primary); line-height: 1.7; margin-bottom: 1.5rem;">
            ${data.description}
        </p>
        
        ${data.sections.map(section => `
            <div class="panel-section">
                <h4>${section.title}</h4>
                <ul>
                    ${section.items.map(item => `<li>${item}</li>`).join('')}
                </ul>
            </div>
        `).join('')}
        
        <div class="stat-highlight">
            <div class="stat-number">${data.stats.number}</div>
            <div class="stat-label">${data.stats.label}</div>
        </div>
        
        <div style="margin-top: 2rem; text-align: center;">
            <a href="ages/${ageId}.html" style="display: inline-block; background: var(--primary); color: white; padding: 0.75rem 2rem; border-radius: 25px; text-decoration: none; font-weight: 600; transition: all 0.3s ease;">
                Explore Age ${ageId} Activities →
            </a>
        </div>
    `;

    document.getElementById('panelContent').innerHTML = content;
    openDetailPanel();
}

// Close panel with Escape key
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeDetailPanel();
    }
});

// Close panel when clicking outside
document.getElementById('detailPanel')?.addEventListener('click', (e) => {
    if (e.target.id === 'detailPanel') {
        closeDetailPanel();
    }
});

// ========================================
// SMOOTH SCROLL FOR RESOURCE CARDS
// ========================================

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

// ========================================
// PERFORMANCE: Reduce animations on low-end devices
// ========================================

if (navigator.hardwareConcurrency && navigator.hardwareConcurrency <= 2) {
    document.body.classList.add('reduced-motion');
}

console.log('🌱 Early Learning Hub - Optimized interactions loaded!');
