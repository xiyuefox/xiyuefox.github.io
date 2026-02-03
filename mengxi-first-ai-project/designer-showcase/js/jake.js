document.addEventListener('DOMContentLoaded', () => {
    const stage = document.body;
    const scrubber = document.querySelector('.timeline-scrubber');
    const handle = document.querySelector('.scrubber-handle');
    const scrollContainer = document.querySelector('.dual-axis-container');

    // 1. Dual-Axis Scrubber Logic
    let isDraggingScrubber = false;

    scrubber.addEventListener('mousedown', (e) => {
        isDraggingScrubber = true;
        updateScrubber(e);
    });

    window.addEventListener('mousemove', (e) => {
        if (!isDraggingScrubber) return;
        updateScrubber(e);
    });

    window.addEventListener('mouseup', () => {
        isDraggingScrubber = false;
    });

    function updateScrubber(e) {
        const rect = scrubber.getBoundingClientRect();
        let x = e.clientX - rect.left;
        x = Math.max(0, Math.min(x, rect.width));

        const percentage = x / rect.width;
        handle.style.left = `${percentage * 100}%`;

        // Sync with horizontal scroll
        const scrollWidth = scrollContainer.scrollWidth - window.innerWidth;
        scrollContainer.scrollLeft = percentage * scrollWidth;

        // Update handle text (pseudo 'time' or 'coordinate')
        const coord = Math.round(percentage * 1000);
        handle.innerText = `${coord}`;
    }

    // 2. Draggable Panels Logic (Apossible style)
    const panels = document.querySelectorAll('.draggable-panel');
    let zIndex = 10;

    // Load saved positions
    const savedPositions = JSON.parse(localStorage.getItem('jds_panel_positions') || '{}');

    panels.forEach((panel, index) => {
        const panelId = panel.dataset.id || `panel-${index}`;
        panel.dataset.id = panelId; // Ensure every panel has an ID

        if (savedPositions[panelId]) {
            panel.style.left = savedPositions[panelId].left;
            panel.style.top = savedPositions[panelId].top;
        }

        let isDraggingPanel = false;
        let startX, startY, initialX, initialY;

        panel.addEventListener('mousedown', (e) => {
            isDraggingPanel = true;
            panel.style.zIndex = ++zIndex;
            startX = e.clientX;
            startY = e.clientY;
            initialX = panel.offsetLeft;
            initialY = panel.offsetTop;
            panel.style.cursor = 'grabbing';
        });

        window.addEventListener('mousemove', (e) => {
            if (!isDraggingPanel) return;
            const dx = e.clientX - startX;
            const dy = e.clientY - startY;
            const finalX = `${initialX + dx}px`;
            const finalY = `${initialY + dy}px`;
            panel.style.left = finalX;
            panel.style.top = finalY;

            // Update connections while dragging
            drawConnections();
        });

        window.addEventListener('mouseup', () => {
            if (!isDraggingPanel) return;
            isDraggingPanel = false;
            panel.style.cursor = 'grab';

            // Save positions on mouse up
            const currentPos = JSON.parse(localStorage.getItem('jds_panel_positions') || '{}');
            currentPos[panelId] = {
                left: panel.style.left,
                top: panel.style.top
            };
            localStorage.setItem('jds_panel_positions', JSON.stringify(currentPos));
        });
    });

    // 3. Reveal Text Logic (Slow down)
    const observerOptions = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal-text').forEach(el => observer.observe(el));

    // 4. Parallax Particles (Choreographer of space-time)
    const starfield = document.querySelector('.starfield');
    if (starfield) {
        for (let i = 0; i < 50; i++) {
            const star = document.createElement('div');
            star.style.position = 'absolute';
            star.style.width = '2px';
            star.style.height = '2px';
            star.style.background = 'white';
            star.style.left = `${Math.random() * 100}%`;
            star.style.top = `${Math.random() * 100}%`;
            star.style.opacity = Math.random();
            starfield.appendChild(star);
        }
    }

    // 5. b-gen-22 Mock Generator Logic
    const briefs = [
        "Design a website that only functions during a full moon.",
        "Create an interface for a time-traveler's lost luggage.",
        "A weather app for a planet where it only rains secrets.",
        "A social network for trees to communicate through root systems.",
        "A navigation system for a library with no physical walls.",
        "A clock that measures emotional depth instead of seconds.",
        "A camera app that only captures what the photographer is thinking.",
        "A portfolio for a designer who doesn't believe in the internet.",
        "An operating system for a playful machine with a soul.",
        "A typography system based on the movement of migrating birds."
    ];

    let attempts = parseInt(localStorage.getItem('bgen22_attempts') || '30');
    const briefDisplay = document.getElementById('brief-display');
    const genBtn = document.getElementById('gen-btn');
    const attemptsDisplay = document.getElementById('attempts-count');

    function updateGeneratorUI() {
        if (!attemptsDisplay || !genBtn) return;
        attemptsDisplay.innerText = attempts;
        if (attempts <= 0) {
            genBtn.disabled = true;
            genBtn.innerText = "ATTEMPTS_EXHAUSTED";
            briefDisplay.innerText = "You have reached the limit of your creative exploration. Slow down.";
        }
    }

    if (genBtn) {
        genBtn.addEventListener('click', () => {
            if (attempts > 0) {
                attempts--;
                localStorage.setItem('bgen22_attempts', attempts.toString());

                briefDisplay.style.opacity = '0';

                setTimeout(() => {
                    const randomBrief = briefs[Math.floor(Math.random() * briefs.length)];
                    briefDisplay.innerText = randomBrief;
                    briefDisplay.style.opacity = '1';
                    updateGeneratorUI();
                }, 300);
            }
        });

        updateGeneratorUI();

        // 6. Voyager Drifting Logic
        const voyager = document.getElementById('voyager-probe');
        let voyagerX = -100;

        if (voyager) {
            function driftVoyager() {
                voyagerX += 0.2; // Slow drift
                if (voyagerX > window.innerWidth + 100) {
                    voyagerX = -100;
                }
                voyager.style.left = `${voyagerX}px`;

                // Randomly update coordinate text
                if (Math.random() > 0.98) {
                    const dist = (14 + Math.random()).toFixed(4);
                    voyager.querySelector('.voyager-label').innerText = `VOYAGER_1_DIST: ${dist} AU`;
                }

                requestAnimationFrame(driftVoyager);
            }
            driftVoyager();
        }
    }

    // 7. Constellation Connections logic
    const svg = document.getElementById('constellation');
    const panelList = Array.from(document.querySelectorAll('.draggable-panel'));

    // 8. Reset Engine Logic
    const resetBtn = document.getElementById('reset-engine');
    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            localStorage.removeItem('jds_panel_positions');
            location.reload();
        });
    }

    // 9. FrontPage 2000 Retro Mode Logic
    const retroToggle = document.getElementById('retro-toggle');
    const isRetro = localStorage.getItem('jds_retro_mode') === 'true';
    if (isRetro) document.body.classList.add('retro-mode');

    if (retroToggle) {
        retroToggle.addEventListener('click', () => {
            const active = document.body.classList.toggle('retro-mode');
            localStorage.setItem('jds_retro_mode', active);
        });
    }

    function drawConnections() {
        if (!svg) return;
        svg.innerHTML = '';

        // Connect each panel to the next one in the list
        for (let i = 0; i < panelList.length; i++) {
            for (let j = i + 1; j < i + 2 && j < panelList.length; j++) {
                const p1 = panelList[i];
                const p2 = panelList[j];

                const r1 = p1.getBoundingClientRect();
                const r2 = p2.getBoundingClientRect();

                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', r1.left + r1.width / 2);
                line.setAttribute('y1', r1.top + r1.height / 2);
                line.setAttribute('x2', r2.left + r2.width / 2);
                line.setAttribute('y2', r2.top + r2.height / 2);

                svg.appendChild(line);
            }
        }
    }

    // 10. Easter Egg: Luddite Manifesto
    const voyagerSignal = document.querySelector('.voyager-signal');
    const modal = document.getElementById('luddite-modal');
    const closeBtn = document.getElementById('luddite-close');

    if (voyagerSignal && modal) {
        voyagerSignal.addEventListener('click', (e) => {
            e.stopPropagation();
            modal.style.display = 'flex';
        });
        closeBtn.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }

    // 11. Time Sync Easter Egg
    function checkTimeSync() {
        const now = new Date();
        const hours = now.getHours();
        const statusText = document.querySelector('.scroll-status');

        if (hours >= 0 && hours <= 4) {
            if (statusText) statusText.innerText = "SYSTEM: TRUE_CREATORS_WORK_IN_THE_DEAD_OF_NIGHT";
        } else if (hours >= 5 && hours <= 7) {
            if (statusText) statusText.innerText = "SYSTEM: DAWN_BREAKER_MODE_ACTIVE";
        }
    }
    checkTimeSync();

    // 12. 30-Click Philosophical Limit
    let globalClicks = parseInt(localStorage.getItem('jds_global_clicks') || '0');
    const HUD = document.querySelector('.ui-header');

    function updateClickHUD() {
        const clickDisplay = document.getElementById('click-counter-hud') || document.createElement('div');
        clickDisplay.id = 'click-counter-hud';
        clickDisplay.style.cssText = `margin-left: 2rem; color: ${globalClicks >= 30 ? 'var(--accent)' : 'var(--text-secondary)'}; font-family: var(--font-mono); font-size: 0.7rem;`;
        clickDisplay.innerText = `[ CLICKS: ${globalClicks}/30 ]`;
        if (!document.getElementById('click-counter-hud')) HUD.appendChild(clickDisplay);

        if (globalClicks >= 30) {
            triggerLimitMessage();
        }
    }

    function triggerLimitMessage() {
        const msg = document.createElement('div');
        msg.id = 'limit-overlay';
        msg.style.cssText = `position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: var(--accent); color: white; z-index: 300; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 2rem;`;
        msg.innerHTML = `
            <h1 style="font-family: var(--font-mono); font-size: 1.5rem; margin-bottom: 2rem;">CRITICAL_EXHAUSTION</h1>
            <p style="font-size: 1.2rem; max-width: 500px; font-style: italic;">"You have exhausted your 30 expenditures of attention. Now, slow down. Experience the silence between actions."</p>
            <button onclick="localStorage.setItem('jds_global_clicks', '0'); location.reload();" style="margin-top: 2rem; background: white; color: var(--accent); border: none; padding: 1rem 2rem; font-family: var(--font-mono); cursor: pointer;">RESTART_COSMIC_FLOW</button>
        `;
        if (!document.getElementById('limit-overlay')) document.body.appendChild(msg);
    }

    document.addEventListener('mousedown', () => {
        if (globalClicks < 30) {
            globalClicks++;
            localStorage.setItem('jds_global_clicks', globalClicks.toString());
            updateClickHUD();
        }
    });
    updateClickHUD();

    // 13. Slow Scroll Detector
    let lastScrollPos = 0;
    let lastScrollTime = Date.now();
    const slowScrollMsg = document.createElement('div');
    slowScrollMsg.id = 'slow-scroll-indicator';
    slowScrollMsg.style.cssText = `position: fixed; bottom: 8rem; left: 50%; transform: translateX(-50%); color: var(--accent); font-family: var(--font-mono); font-size: 0.7rem; opacity: 0; transition: opacity 0.5s; pointer-events: none; z-index: 99;`;
    slowScrollMsg.innerText = "PATH_OF_SLOWNESS_DETECTED: YOU ARE PRACTICING JAKE'S PHILOSOPHY";
    document.body.appendChild(slowScrollMsg);

    scrollContainer.addEventListener('scroll', () => {
        const currentPos = scrollContainer.scrollLeft;
        const currentTime = Date.now();
        const distance = Math.abs(currentPos - lastScrollPos);
        const timeDiff = currentTime - lastScrollTime;

        if (timeDiff > 0) {
            const velocity = distance / timeDiff; // pixels per ms
            if (velocity > 0 && velocity < 0.3) {
                slowScrollMsg.style.opacity = '1';
                document.body.style.boxShadow = "inset 0 0 50px rgba(255, 62, 62, 0.1)";
            } else {
                slowScrollMsg.style.opacity = '0';
                document.body.style.boxShadow = "none";
            }
        }

        lastScrollPos = currentPos;
        lastScrollTime = currentTime;

        // Hide message after stop
        clearTimeout(window.scrollStopTimeout);
        window.scrollStopTimeout = setTimeout(() => {
            slowScrollMsg.style.opacity = '0';
            document.body.style.boxShadow = "none";
        }, 1500);
    });

    // Update lines every frame for smooth dragging follow
    function animateLines() {
        drawConnections();
        requestAnimationFrame(animateLines);
    }
    animateLines();

    // Re-trigger reveal text logic on scroll
    scrollContainer.addEventListener('scroll', () => {
        document.querySelectorAll('.reveal-text').forEach(el => observer.observe(el));
    });
});
