        (function () {
            const theme = localStorage.getItem('tg-theme') || 'dark';
            document.documentElement.dataset.theme = theme;
        })();
        function toggleTheme() {
            const currentTheme = document.documentElement.dataset.theme;
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.dataset.theme = newTheme;
            localStorage.setItem('tg-theme', newTheme);
            updateThemeIcon(newTheme);
        }

        function updateThemeIcon(theme) {
            const icon = document.getElementById('theme-icon');
            if (icon) {
                icon.style.opacity = '0';
                icon.style.transform = 'scale(0.5) rotate(-90deg)';
                setTimeout(() => {
                    icon.innerText = theme === 'dark' ? '🌙' : '☀️';
                    icon.style.opacity = '1';
                    icon.style.transform = 'scale(1) rotate(0deg)';
                }, 150);
            }
        }

        updateThemeIcon(document.documentElement.dataset.theme);

        function updateClock() {
            const now = new Date();
            const timeStr = now.getHours().toString().padStart(2, '0') + ':' +
                now.getMinutes().toString().padStart(2, '0') + ':' +
                now.getSeconds().toString().padStart(2, '0');
            const timeEl = document.getElementById('current-time');
            if (timeEl) timeEl.innerText = timeStr;
        }
        setInterval(updateClock, 1000);
        updateClock();

        // Smooth Scroll & Link Active State
        document.querySelectorAll('.tg-nav-link').forEach(link => {
            link.addEventListener('click', function (e) {
                const href = this.getAttribute('href');
                if (href.startsWith('#')) {
                    const target = document.querySelector(href);
                    if (target) {
                        e.preventDefault();
                        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                        document.querySelectorAll('.tg-nav-link').forEach(l => l.classList.remove('active'));
                        this.classList.add('active');
                    }
                }
            });
        });

        window.addEventListener('scroll', () => {
            const sections = document.querySelectorAll('.tg-section');
            const navLinks = document.querySelectorAll('.tg-nav-link');
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                if (window.pageYOffset >= sectionTop - 200) {
                    current = section.getAttribute('id');
                }
            });
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (current && link.getAttribute('href').includes(current)) {
                    link.classList.add('active');
                }
            });
        });

        // Scroll Reveal Logic
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    // Stagger effect
                    setTimeout(() => {
                        entry.target.classList.add('is-visible');
                    }, index * 50);
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        // Auto-add .tg-fade-in to cards if not present
        document.querySelectorAll('.tg-card, .tg-blog-card, .hal-card').forEach(el => {
            if (!el.classList.contains('tg-fade-in')) {
                el.classList.add('tg-fade-in');
            }
        });

        document.querySelectorAll('.tg-fade-in').forEach(el => {
            revealObserver.observe(el);
        });

        // Poche-style Filtering Logic
        document.querySelectorAll('.hal-filter-btn').forEach(button => {
            button.addEventListener('click', () => {
                const filter = button.getAttribute('data-filter');

                // Active state for button
                document.querySelectorAll('.hal-filter-btn').forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');

                // Filter items
                document.querySelectorAll('.hal-card').forEach(card => {
                    if (filter === 'all' || card.getAttribute('data-category') === filter) {
                        card.classList.remove('hidden');
                    } else {
                        card.classList.add('hidden');
                    }
                });
            });
        });

        // Poche-style Playful Entry Logic (Automated & Fixed Execution)
        function initPocheGate() {
            const gate = document.getElementById('poche-gate');
            if (!gate) return;
            const gateTitle = document.querySelector('.gate-title');

            // Text scramble effect for title
            const originalText = gateTitle.innerText;
            const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
            let interval = null;

            function scrambleText() {
                let iteration = 0;
                clearInterval(interval);
                interval = setInterval(() => {
                    gateTitle.innerText = originalText
                        .split("")
                        .map((letter, index) => {
                            if (index < iteration) return originalText[index];
                            return letters[Math.floor(Math.random() * letters.length)];
                        })
                        .join("");
                    if (iteration >= originalText.length) clearInterval(interval);
                    iteration += 1 / 3;
                }, 40);
            }

            // Check if user has already entered this session to avoid annoyance
            if (!sessionStorage.getItem('hasEnteredGarden')) {
                // Prevent scrolling while gate is active
                document.body.style.overflow = 'hidden';
                window.scrollTo(0, 0);

                // Trigger scramble
                setTimeout(scrambleText, 300);

                // Auto dismiss after 2.5s
                setTimeout(() => {
                    gate.classList.add('entered');
                    document.body.style.overflow = ''; // Restore scrolling
                    sessionStorage.setItem('hasEnteredGarden', 'true');
                    // Trigger entry animations on main content
                    document.body.classList.add('garden-entered');
                }, 2200);
            } else {
                // Instantly hide gate
                gate.style.display = 'none';
                document.body.style.overflow = '';
                document.body.classList.add('garden-entered');
            }
        }

        // Run the gate logic
        initPocheGate();
