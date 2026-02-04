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

    // Energy Flow Animation for Atomic Exchange
    const flows = document.querySelectorAll('.energy-flow');
    flows.forEach(flow => {
        // Continuous pulse or moving particle effect could be added here
        setInterval(() => {
            flow.style.opacity = (Math.random() * 0.5 + 0.5).toString();
        }, 100);
    });

    // Isotope Decay Interaction
    const decayGraph = document.querySelector('.decay-graph');
    if (decayGraph) {
        decayGraph.addEventListener('mousemove', (e) => {
            const rect = decayGraph.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const percentage = (x / rect.width) * 100;

            // Subtle flash effect on peak zone
            if (percentage < 25) {
                decayGraph.style.boxShadow = 'inset 20px 0 20px rgba(0, 255, 255, 0.05)';
            } else {
                decayGraph.style.boxShadow = 'none';
            }
        });
    }

    // Terminal typing effect for footer
    const lines = document.querySelectorAll('.term-line');
    lines.forEach((line, index) => {
        const text = line.textContent;
        line.textContent = '';
        setTimeout(() => {
            let i = 0;
            const timer = setInterval(() => {
                line.textContent += text.charAt(i);
                i++;
                if (i >= text.length) clearInterval(timer);
            }, 30);
        }, index * 1000);
    });

    // Parallax logic for blueprint grid
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const blueprint = document.querySelector('.background-blueprint');
        if (blueprint) {
            blueprint.style.backgroundPositionY = `${scrolled * 0.5}px`;
        }
    });

    console.log('⚛️ Chris Paik System: Physics vs Narrative | Pace Capital');
});
