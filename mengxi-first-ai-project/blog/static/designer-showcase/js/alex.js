document.addEventListener('DOMContentLoaded', () => {
    const grid = document.querySelector('.structure-grid');
    const cards = document.querySelectorAll('.card');
    const toggleBtn = document.getElementById('toggle-soft');
    let isSoftMode = false;

    // 1. Perspective Grid Movement
    document.addEventListener('mousemove', (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 20;

        if (grid) {
            grid.style.transform = `perspective(1000px) rotateX(${20 + y}deg) rotateY(${x}deg) translateY(-200px)`;
        }
    });

    // 2. Scroll Reveal Observer
    const observerOptions = {
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);

    const reveals = document.querySelectorAll('.reveal');
    reveals.forEach(el => observer.observe(el));

    // 3. Soft Mode Toggle
    toggleBtn.addEventListener('click', () => {
        isSoftMode = !isSoftMode;

        if (isSoftMode) {
            document.body.style.backgroundColor = '#1a0d1a'; // Deep purple/wine
            document.querySelectorAll('.card').forEach(card => {
                card.style.borderRadius = '50px 10px 50px 10px';
                card.style.borderStyle = 'dashed';
                card.style.borderColor = '#9d4edd';
            });
            grid.style.opacity = '0.05';
            toggleBtn.textContent = 'RESTORE_STRUCTURE';
            toggleBtn.style.borderColor = '#9d4edd';
            toggleBtn.style.color = '#9d4edd';
        } else {
            document.body.style.backgroundColor = '';
            document.querySelectorAll('.card').forEach(card => {
                const originalType = card.getAttribute('data-type');
                if (originalType === 'hard') {
                    card.style.borderRadius = '0';
                    card.style.borderStyle = 'solid';
                    card.style.borderColor = '';
                } else {
                    card.style.borderRadius = '40px 10px 40px 5px';
                    card.style.borderStyle = 'dashed';
                    card.style.borderColor = '';
                }
            });
            grid.style.opacity = '';
            toggleBtn.textContent = 'ENABLE_SOFT_MODE';
            toggleBtn.style.borderColor = '';
            toggleBtn.style.color = '';
        }
    });

    // 4. Parallax effect for cards
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        cards.forEach((card, index) => {
            const speed = (index % 3 + 1) * 0.05;
            card.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });
});
