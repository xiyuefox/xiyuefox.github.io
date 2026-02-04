document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('sketch-canvas');
    const ctx = canvas.getContext('2d');
    const toggleBtn = document.getElementById('toggle-mode');
    let isDarkMode = false;
    let sketches = [];

    // Setup canvas
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        generateSketches();
    }

    // Generate random sketch-like marks
    function generateSketches() {
        sketches = [];
        const numSketches = Math.floor((canvas.width * canvas.height) / 30000);

        for (let i = 0; i < numSketches; i++) {
            sketches.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                type: Math.floor(Math.random() * 4), // 0: circle, 1: line, 2: scribble, 3: cross
                size: 10 + Math.random() * 30,
                rotation: Math.random() * Math.PI * 2,
                opacity: 0.1 + Math.random() * 0.3
            });
        }
        drawSketches();
    }

    function drawSketches() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const color = isDarkMode ? '255, 255, 255' : '0, 0, 0';

        sketches.forEach(sketch => {
            ctx.save();
            ctx.translate(sketch.x, sketch.y);
            ctx.rotate(sketch.rotation);
            ctx.strokeStyle = `rgba(${color}, ${sketch.opacity})`;
            ctx.lineWidth = 1;
            ctx.lineCap = 'round';

            switch (sketch.type) {
                case 0: // Circle
                    ctx.beginPath();
                    ctx.arc(0, 0, sketch.size / 2, 0, Math.PI * 2);
                    ctx.stroke();
                    break;

                case 1: // Line
                    ctx.beginPath();
                    ctx.moveTo(-sketch.size / 2, 0);
                    ctx.lineTo(sketch.size / 2, 0);
                    ctx.stroke();
                    break;

                case 2: // Scribble
                    ctx.beginPath();
                    ctx.moveTo(-sketch.size / 2, -sketch.size / 4);
                    for (let i = 0; i < 5; i++) {
                        const x = -sketch.size / 2 + (sketch.size / 4) * i;
                        const y = (i % 2 === 0 ? -1 : 1) * sketch.size / 4;
                        ctx.lineTo(x, y);
                    }
                    ctx.stroke();
                    break;

                case 3: // Cross
                    ctx.beginPath();
                    ctx.moveTo(-sketch.size / 4, -sketch.size / 4);
                    ctx.lineTo(sketch.size / 4, sketch.size / 4);
                    ctx.moveTo(sketch.size / 4, -sketch.size / 4);
                    ctx.lineTo(-sketch.size / 4, sketch.size / 4);
                    ctx.stroke();
                    break;
            }
            ctx.restore();
        });
    }

    // Scroll Reveal Observer
    const observerOptions = { threshold: 0.15 };
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // Dark Mode Toggle
    toggleBtn.addEventListener('click', () => {
        isDarkMode = !isDarkMode;
        document.body.classList.toggle('dark-mode');
        toggleBtn.textContent = isDarkMode ? '切换_日间模式' : '切换_手艺模式';
        drawSketches();
    });

    // Mouse interaction - add sketches on movement
    let lastMouseTime = 0;
    document.addEventListener('mousemove', (e) => {
        const now = Date.now();
        if (now - lastMouseTime < 100) return;
        lastMouseTime = now;

        // Add subtle sketch mark near cursor
        if (Math.random() > 0.7) {
            const color = isDarkMode ? '255, 255, 255' : '0, 0, 0';
            ctx.save();
            ctx.strokeStyle = `rgba(${color}, 0.1)`;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.arc(e.clientX, e.clientY, 5 + Math.random() * 10, 0, Math.PI * 2);
            ctx.stroke();
            ctx.restore();
        }
    });

    // Parallax effect for cards
    const cards = document.querySelectorAll('.card');
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        cards.forEach((card, index) => {
            const speed = (index % 4 + 1) * 0.02;
            card.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });

    // Initialize
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Lesson card hover animation
    document.querySelectorAll('.lesson-card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            const visual = card.querySelector('.lesson-visual');
            if (visual) {
                visual.style.transform = 'scale(1.1)';
            }
        });
        card.addEventListener('mouseleave', () => {
            const visual = card.querySelector('.lesson-visual');
            if (visual) {
                visual.style.transform = 'scale(1)';
            }
        });
    });

    // Philosopher card click to expand info
    document.querySelectorAll('.philosopher-card').forEach(card => {
        card.style.cursor = 'pointer';
        card.addEventListener('click', () => {
            const topic = card.querySelector('.phil-topic');
            if (topic) {
                topic.style.transition = 'all 0.3s';
                if (topic.style.fontSize === '1rem') {
                    topic.style.fontSize = '';
                    topic.style.fontWeight = '';
                } else {
                    topic.style.fontSize = '1rem';
                    topic.style.fontWeight = 'bold';
                }
            }
        });
    });

    // Yijing Coin Flip Interaction
    const coins = document.querySelectorAll('.coin');
    const yinYangSymbols = ['☯', '⚊', '⚋'];

    coins.forEach(coin => {
        coin.addEventListener('click', () => {
            coin.classList.add('flipping');

            // Randomize result after animation
            setTimeout(() => {
                coin.classList.remove('flipping');
                const randomSymbol = yinYangSymbols[Math.floor(Math.random() * yinYangSymbols.length)];
                coin.textContent = randomSymbol;

                // Add glow effect based on result
                if (randomSymbol === '⚊') {
                    coin.style.boxShadow = '0 0 20px rgba(255, 215, 0, 0.8)';
                } else if (randomSymbol === '⚋') {
                    coin.style.boxShadow = '0 0 20px rgba(128, 90, 213, 0.8)';
                } else {
                    coin.style.boxShadow = '';
                }
            }, 600);
        });
    });

    // Trigram hover sound effect (visual feedback)
    const trigrams = document.querySelectorAll('.trigram');
    trigrams.forEach(trigram => {
        trigram.addEventListener('click', () => {
            // Visual pulse effect
            trigram.style.animation = 'none';
            trigram.offsetHeight; // Trigger reflow
            trigram.style.animation = 'trigramPulse 0.5s ease-out';

            // Show trigram name tooltip
            const name = trigram.getAttribute('data-name');
            const tooltip = document.createElement('div');
            tooltip.className = 'trigram-tooltip';
            tooltip.textContent = name;
            tooltip.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: linear-gradient(135deg, #e85d04, #805ad5);
                color: white;
                padding: 1rem 2rem;
                border-radius: 8px;
                font-size: 1.5rem;
                font-family: var(--font-serif);
                z-index: 1000;
                animation: tooltipFade 1.5s ease-out forwards;
            `;
            document.body.appendChild(tooltip);

            setTimeout(() => {
                tooltip.remove();
            }, 1500);
        });
    });

    // Add CSS animation for trigram and tooltip
    const styleSheet = document.createElement('style');
    styleSheet.textContent = `
        @keyframes trigramPulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); background: rgba(232, 93, 4, 0.5); }
            100% { transform: scale(1); }
        }
        @keyframes tooltipFade {
            0% { opacity: 0; transform: translate(-50%, -50%) scale(0.5); }
            20% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
            80% { opacity: 1; }
            100% { opacity: 0; transform: translate(-50%, -50%) scale(0.8); }
        }
    `;
    document.head.appendChild(styleSheet);

    // Draw Mode Toggle
    const drawBtn = document.getElementById('btn-draw-now');
    let isDrawMode = false;
    let isPainting = false;

    drawBtn.addEventListener('click', () => {
        isDrawMode = !isDrawMode;
        document.body.classList.toggle('draw-mode');

        if (isDrawMode) {
            drawBtn.textContent = '退出绘图 EXIT_DRAW';
            canvas.classList.add('active-paint');

            // Add hint if not exists
            if (!document.querySelector('.draw-hint')) {
                const hint = document.createElement('div');
                hint.className = 'draw-hint';
                hint.textContent = '鼠标左键绘图，右键清空 | ESC 退出';
                document.body.appendChild(hint);
            }
        } else {
            drawBtn.textContent = '立即动笔 DRAW_NOW';
            canvas.classList.remove('active-paint');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            generateSketches(); // Restore background sketches
        }
    });

    // Painting Logic
    canvas.addEventListener('mousedown', (e) => {
        if (!isDrawMode) return;
        if (e.button === 2) { // Right click to clear
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            return;
        }
        isPainting = true;
        ctx.beginPath();
        ctx.moveTo(e.clientX, e.clientY);
        ctx.strokeStyle = '#2a2a2a';
        ctx.lineWidth = 2;
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
    });

    canvas.addEventListener('mousemove', (e) => {
        if (!isDrawMode || !isPainting) return;
        ctx.lineTo(e.clientX, e.clientY);
        ctx.stroke();
    });

    canvas.addEventListener('mouseup', () => {
        isPainting = false;
    });

    canvas.addEventListener('contextmenu', (e) => {
        if (isDrawMode) e.preventDefault();
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && isDrawMode) {
            drawBtn.click();
        }
    });

    console.log('🎨 Ralph Ammer Profile Loaded | draw > art | 易经 Yijing');
});
