document.addEventListener('DOMContentLoaded', () => {

    // Custom Cursor Logic: Attention vs Awareness
    const orb = document.getElementById('attention-orb');
    const field = document.getElementById('awareness-field');

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let orbX = mouseX;
    let orbY = mouseY;

    document.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;

        // Awareness field follows immediately (Awareness is the background)
        field.style.left = `${mouseX}px`;
        field.style.top = `${mouseY}px`;
    });

    function animateCursor() {
        // Attention orb has momentum (Attention is often "sticky" or lagging)
        let dx = mouseX - orbX;
        let dy = mouseY - orbY;

        orbX += dx * 0.15;
        orbY += dy * 0.15;

        orb.style.left = `${orbX}px`;
        orb.style.top = `${orbY}px`;
        orb.style.transform = `translate(-50%, -50%) scale(${1 + Math.abs(dx + dy) * 0.01})`;

        requestAnimationFrame(animateCursor);
    }
    animateCursor();

    // Intersection Observer for Reveal
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -100px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // Experience Gap Interaction: Click to "Yield"
    const yieldSign = document.querySelector('.yield-visual');
    if (yieldSign) {
        yieldSign.addEventListener('click', () => {
            const colors = ['#ffcc00', '#5f7a61', '#7d5fff', '#1c1c1c'];
            const currentColor = yieldSign.style.backgroundColor;
            let nextColor = colors[Math.floor(Math.random() * colors.length)];
            while (nextColor === currentColor) {
                nextColor = colors[Math.floor(Math.random() * colors.length)];
            }
            yieldSign.style.backgroundColor = nextColor;

            // Randomly tilt
            const tilt = (Math.random() - 0.5) * 20;
            yieldSign.style.transform = `rotate(${tilt}deg)`;
        });
    }

    // Magic Reverse: Hover effect for step 2
    const magicStep = document.querySelector('.wf-step.magic');
    if (magicStep) {
        magicStep.addEventListener('mouseenter', () => {
            document.body.style.backgroundColor = '#fdfbff';
            orb.style.background = 'var(--accent-magic)';
            orb.style.transform = 'translate(-50%, -50%) scale(2)';
        });
        magicStep.addEventListener('mouseleave', () => {
            document.body.style.backgroundColor = 'var(--bg-paper)';
            orb.style.background = 'var(--accent-gold)';
            orb.style.transform = 'translate(-50%, -50%) scale(1)';
        });
    }

    console.log('💆 Jordan Moore Profile: Stay present.');
});
