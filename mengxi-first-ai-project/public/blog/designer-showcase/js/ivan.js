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

    // Color Block Visualization Logic
    const vizContainer = document.getElementById('color-block-demo');
    if (vizContainer) {
        const data = [
            { height: 80, opacity: 0.9, color: 'var(--accent-red)' },
            { height: 40, opacity: 0.4, color: 'var(--accent-blue)' },
            { height: 120, opacity: 0.7, color: 'var(--accent-yellow)' },
            { height: 60, opacity: 0.3, color: 'var(--accent-green)' },
            { height: 180, opacity: 0.8, color: 'var(--accent-red)' },
            { height: 90, opacity: 0.5, color: 'var(--accent-blue)' },
            { height: 70, opacity: 0.6, color: 'var(--accent-yellow)' },
            { height: 150, opacity: 0.9, color: 'var(--accent-green)' }
        ];

        data.forEach((item, index) => {
            const block = document.createElement('div');
            block.className = 'viz-block';
            block.style.height = '0px';
            block.style.width = '100%';
            block.style.backgroundColor = item.color;
            block.style.opacity = item.opacity;
            block.style.transition = `height 1s cubic-bezier(0.16, 1, 0.3, 1) ${index * 0.1}s`;

            // Interaction: Show precise value on hover
            block.title = `Query Intensity: ${item.height}%`;

            vizContainer.appendChild(block);

            // Trigger animation after a short delay
            setTimeout(() => {
                block.style.height = `${item.height}px`;
            }, 100);
        });
    }

    // Interactive LEGO Stack at the bottom
    const legoStack = document.getElementById('interactive-lego');
    if (legoStack) {
        const colors = ['red', 'blue', 'yellow', 'green'];
        let count = 0;

        const addBrick = () => {
            if (count > 10) return;
            const brick = document.createElement('div');
            brick.className = `lego-brick ${colors[Math.floor(Math.random() * colors.length)]}`;
            brick.style.width = '60px';
            brick.style.height = '25px';
            brick.style.margin = '2px auto';
            brick.style.cursor = 'pointer';
            brick.style.opacity = '0';
            brick.style.transform = 'translateY(20px)';
            brick.style.transition = 'all 0.4s';

            legoStack.prepend(brick);

            setTimeout(() => {
                brick.style.opacity = '1';
                brick.style.transform = 'translateY(0)';
            }, 10);

            count++;
        };

        // Add initial bricks
        for (let i = 0; i < 4; i++) setTimeout(addBrick, i * 200);

        // Click to add more (Compose your own tower)
        legoStack.addEventListener('click', addBrick);
    }

    // Parallax logic for subtle grid movement
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const grid = document.querySelector('.viewport-grid');
        if (grid) {
            grid.style.transform = `translateY(${scrolled * 0.1}px)`;
        }
    });

    console.log('🧱 Ivan Zhao Profile Initialized: Building Blocks...');
});
