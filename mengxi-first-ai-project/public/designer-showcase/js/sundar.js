document.addEventListener('DOMContentLoaded', () => {
    // Custom Cursor
    const cursor = document.getElementById('cursor');
    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
    });

    // Reveal on scroll
    const reveals = document.querySelectorAll('.reveal');
    const options = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, options);

    reveals.forEach(reveal => {
        observer.observe(reveal);
    });

    // Token Counter Animation
    const tokenStats = document.querySelector('.t-stats');
    if (tokenStats) {
        let count = 0;
        const target = 480000000000000;
        const duration = 2000;
        const increment = target / (duration / 16);

        function updateTokens() {
            count += increment;
            if (count < target) {
                tokenStats.textContent = Math.floor(count).toLocaleString();
                requestAnimationFrame(updateTokens);
            } else {
                tokenStats.textContent = target.toLocaleString();
            }
        }

        // Start counter when visible
        const observerToken = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) updateTokens();
        });
        observerToken.observe(tokenStats);
    }

    // Scuba Parallax Effect
    const scubaBox = document.querySelector('.scuba-box');
    if (scubaBox) {
        document.addEventListener('mousemove', (e) => {
            const x = (window.innerWidth / 2 - e.clientX) / 50;
            const y = (window.innerHeight / 2 - e.clientY) / 50;
            const deepCalm = scubaBox.querySelector('.deep-calm');
            deepCalm.style.transform = `translate(${x}px, ${y}px)`;
        });
    }

    // Subtle background animation
    let gridOffset = 0;
    function animateGrid() {
        gridOffset += 0.5; // High velocity
        document.body.style.backgroundPosition = `${gridOffset}px ${gridOffset}px`;
        requestAnimationFrame(animateGrid);
    }
    animateGrid();

    // Log boot sequence
    console.log("%c SUNDAR_OS_BOOTING... ", "background: #4285f4; color: white; padding: 5px;");
    console.log("%c [STATUS: INFRASTRUCTURE_READY] ", "color: #34a853;");
});
