document.addEventListener('DOMContentLoaded', () => {

    // Reveal Observer
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // Trust Battery Logic
    let currentBattery = 50;
    const batteryLevel = document.getElementById('batteryLevel');
    const batteryStatus = document.getElementById('batteryStatus');

    window.changeBattery = (amount) => {
        currentBattery = Math.min(100, Math.max(0, currentBattery + amount));
        batteryLevel.style.width = currentBattery + '%';

        if (currentBattery >= 80) {
            batteryStatus.textContent = `${currentBattery}% (FULL_AUTONOMY_GRANTED)`;
            batteryLevel.style.backgroundColor = '#00ff41';
            batteryLevel.style.boxShadow = '0 0 30px #00ff41';
        } else if (currentBattery <= 20) {
            batteryStatus.textContent = `${currentBattery}% (CRITICAL_REBUILD_NEEDED)`;
            batteryLevel.style.backgroundColor = '#ff3131';
            batteryLevel.style.boxShadow = '0 0 30px #ff3131';
        } else {
            batteryStatus.textContent = `${currentBattery}% (IN_PROGRESS_50_START)`;
            batteryLevel.style.backgroundColor = '#00ff41';
            batteryLevel.style.boxShadow = '0 0 20px #00ff41';
        }
    };

    // Glitch title effect randomization
    const title = document.querySelector('.glitch-title');
    if (title) {
        setInterval(() => {
            title.style.textShadow = Math.random() > 0.9 ?
                '2px 0 #ff3131, -2px 0 #00ff41' : 'none';
        }, 100);
    }

    // Terminal typing simulator
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
        }, index * 400);
    });

    console.log('🕹️ Tobi OS Loaded: Anti-fragile Mode Activated. GLHF.');
});
