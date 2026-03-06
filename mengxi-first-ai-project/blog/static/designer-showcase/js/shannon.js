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

    // Binary BG Simulator
    const binaryBgs = document.querySelectorAll('.binary-bg');
    binaryBgs.forEach(bg => {
        let binaryStr = '';
        for (let i = 0; i < 500; i++) {
            binaryStr += Math.random() > 0.5 ? '1 ' : '0 ';
        }
        bg.innerText = binaryStr;

        // Randomly flip bits
        setInterval(() => {
            let current = bg.innerText.split(' ');
            let idx = Math.floor(Math.random() * current.length);
            if (current[idx] === '1') current[idx] = '0';
            else if (current[idx] === '0') current[idx] = '1';
            bg.innerText = current.join(' ');
        }, 300);
    });

    console.log('[INFORMATION_THEORY] Claude Shannon archive initialized.');
});
