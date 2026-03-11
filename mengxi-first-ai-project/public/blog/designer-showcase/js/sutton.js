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

    // RL Agent Grid Panel Interaction Simulator
    // Clicking grid panels updates terminal-like feedback in a pseudo "TD Error"
    const panels = document.querySelectorAll('.grid-panel');
    panels.forEach(panel => {
        panel.addEventListener('click', () => {
            const originalColor = panel.style.borderColor;

            // Simulating positive reward (TD Error Spike)
            panel.style.transition = 'all 0.1s ease';
            panel.style.transform = 'scale(0.98)';
            panel.style.borderColor = '#d33c2a'; // Sutton Accent Red

            setTimeout(() => {
                panel.style.transform = 'scale(1)';
                panel.style.borderColor = originalColor;
            }, 150);
        });
    });

    console.log('[AGENT_INITIALIZED] Reward Function Defined. Exploring environment...');
});
