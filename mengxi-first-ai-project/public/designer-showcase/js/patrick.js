document.addEventListener('DOMContentLoaded', () => {

    // Reveal Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // Staggered Timeline Appearance
    const fossilItems = document.querySelectorAll('.fossil-item');
    fossilItems.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = 'translateX(-20px)';
        item.style.transition = `all 0.6s ease ${index * 0.1 + 0.5}s`;

        // Use a separate observer for better control
        const timeObserver = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                item.style.opacity = '1';
                item.style.transform = 'translateX(0)';
            }
        }, { threshold: 0.5 });
        timeObserver.observe(item);
    });

    // Suble Mouse Parallax for Gradient
    const gradient = document.querySelector('.stripe-gradient');
    document.addEventListener('mousemove', (e) => {
        const moveX = (e.clientX - window.innerWidth / 2) * 0.05;
        const moveY = (e.clientY - window.innerHeight / 2) * 0.05;
        if (gradient) {
            gradient.style.transform = `translate(${moveX}px, ${moveY}px) scale(1.1)`;
        }
    });

    // Question Wall Random Drift
    const questions = document.querySelectorAll('.q-item');
    questions.forEach(q => {
        q.addEventListener('mouseenter', () => {
            q.style.transform = `scale(1.05) translateY(-5px)`;
            q.style.borderColor = 'var(--accent-indigo)';
            q.style.boxShadow = '0 5px 15px rgba(99, 91, 255, 0.1)';
        });
        q.addEventListener('mouseleave', () => {
            q.style.transform = 'scale(1) translateY(0)';
            q.style.boxShadow = 'none';
            if (!q.classList.contains('highlight')) {
                q.style.borderColor = 'var(--border-soft)';
            }
        });
    });

    // Strategy Callout Pulse
    const callout = document.querySelector('.strategy-callout');
    if (callout) {
        setInterval(() => {
            callout.style.borderColor = 'var(--accent-cyan)';
            setTimeout(() => {
                callout.style.borderColor = 'var(--accent-indigo)';
            }, 1000);
        }, 3000);
    }

    console.log('🏛️ Patrick Collison System: Civilization Architecture | Progress考古');
});
