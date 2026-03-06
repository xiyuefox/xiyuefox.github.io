/**
 * Duan Yongping Page JavaScript
 * Benfen philosophy animations and interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    // ============================================
    // Scroll Reveal Observer
    // ============================================
    const reveals = document.querySelectorAll('.reveal');

    if (reveals.length) {
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
    // Benfen Visual Interaction
    // ============================================
    const benfenCircles = document.querySelectorAll('.benfen-circle');

    benfenCircles.forEach((circle, index) => {
        circle.addEventListener('mouseenter', () => {
            // Highlight corresponding explanation
            const explanations = document.querySelectorAll('.benfen-item');
            if (explanations[index]) {
                explanations[index].style.background = 'rgba(46, 139, 87, 0.1)';
            }
        });

        circle.addEventListener('mouseleave', () => {
            const explanations = document.querySelectorAll('.benfen-item');
            if (explanations[index]) {
                explanations[index].style.background = 'rgba(255, 255, 255, 0.02)';
            }
        });
    });

    // ============================================
    // Layer Item Interaction
    // ============================================
    const layerItems = document.querySelectorAll('.layer-item');

    layerItems.forEach((item, index) => {
        item.addEventListener('click', () => {
            // Toggle active state
            item.classList.toggle('layer-active');

            // Show insight based on layer
            const layerInsights = [
                "商业模式是基础。没有好模式，其他都是空谈。",
                "企业文化决定企业能走多远。没有诚信，不可持续。",
                "价格是入场券。好公司也要有好价格。"
            ];

            if (item.classList.contains('layer-active')) {
                const insight = document.createElement('div');
                insight.className = 'layer-insight';
                insight.textContent = layerInsights[index];
                item.appendChild(insight);
            } else {
                const existingInsight = item.querySelector('.layer-insight');
                if (existingInsight) {
                    existingInsight.remove();
                }
            }
        });
    });

    // ============================================
    // Stop Doing List Toggle
    // ============================================
    const stopItems = document.querySelectorAll('.stop-items li');

    stopItems.forEach(item => {
        item.style.cursor = 'pointer';
        item.addEventListener('click', () => {
            item.style.textDecoration = item.style.textDecoration === 'line-through' ? 'none' : 'line-through';
            item.style.opacity = item.style.textDecoration === 'line-through' ? '0.4' : '1';
        });
    });

    // ============================================
    // Case Cards Parallax on Scroll
    // ============================================
    const caseCards = document.querySelectorAll('.case-card');

    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;

        caseCards.forEach((card, index) => {
            const speed = 0.02 + (index * 0.01);
            card.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });

    // ============================================
    // Timeline Intersection Highlight
    // ============================================
    const timelineEvents = document.querySelectorAll('.t-event');

    const timelineObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
            }
        });
    }, {
        threshold: 0.3,
        rootMargin: '-100px 0px -50% 0px'
    });

    timelineEvents.forEach(event => {
        event.style.transition = 'opacity 0.5s ease';
        event.style.opacity = '0.4';
        timelineObserver.observe(event);
    });

    // ============================================
    // Quote Cards Random Fade
    // ============================================
    const quoteItems = document.querySelectorAll('.quote-item');

    quoteItems.forEach(quote => {
        // Random initial delay
        quote.style.animationDelay = `${Math.random() * 2}s`;

        quote.addEventListener('mouseenter', () => {
            quote.style.transform = 'scale(1.02)';
            quote.style.boxShadow = '0 10px 30px rgba(212, 160, 23, 0.2)';
        });

        quote.addEventListener('mouseleave', () => {
            quote.style.transform = 'scale(1)';
            quote.style.boxShadow = 'none';
        });
    });

    // ============================================
    // Person Cards Hover Effect
    // ============================================
    const personCards = document.querySelectorAll('.person-card');

    personCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.borderColor = 'var(--accent-green)';
            card.style.background = 'rgba(46, 139, 87, 0.05)';
        });

        card.addEventListener('mouseleave', () => {
            card.style.borderColor = 'var(--border-dim)';
            card.style.background = 'rgba(255, 255, 255, 0.02)';
        });
    });

    // ============================================
    // Keyboard Shortcuts
    // ============================================
    document.addEventListener('keydown', (e) => {
        // Skip if in input field
        if (['input', 'textarea'].includes(document.activeElement.tagName.toLowerCase())) {
            return;
        }

        // B to toggle all stop items
        if (e.key.toLowerCase() === 'b') {
            stopItems.forEach(item => {
                const isStruck = item.style.textDecoration === 'line-through';
                item.style.textDecoration = isStruck ? 'none' : 'line-through';
                item.style.opacity = isStruck ? '1' : '0.4';
            });
        }
    });

    // ============================================
    // Add layer insight styles dynamically
    // ============================================
    const styleSheet = document.createElement('style');
    styleSheet.textContent = `
        .layer-item {
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .layer-item.layer-active {
            background: rgba(46, 139, 87, 0.1) !important;
            border-left-color: var(--accent-green) !important;
        }

        .layer-insight {
            margin-top: 12px;
            padding: 8px 12px;
            background: rgba(46, 139, 87, 0.15);
            border-radius: 4px;
            font-size: 0.85rem;
            color: var(--accent-green);
            font-family: var(--font-mono);
            animation: fadeInUp 0.3s ease;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    `;
    document.head.appendChild(styleSheet);

    // ============================================
    // Smooth scroll for anchor links
    // ============================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
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
});
