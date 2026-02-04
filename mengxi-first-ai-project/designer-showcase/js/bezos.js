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

    // Regret Minimization Model Slider
    const ageSlider = document.getElementById('ageSlider');
    const regretMsg = document.getElementById('regretMsg');

    const messages = {
        30: "正在西雅图的车库里构建未来的基础设施...",
        40: "如果我不尝试，80 岁的我会不会为此自责？",
        50: "我们通过‘反向推导’看到了客户的需求。",
        60: "哪怕失败，我也不会因为‘没有尝试’而遗憾。",
        70: "通往太空的道路正在被铺平。",
        80: "这一生，我最大限度地减少了所有的后悔。"
    };

    ageSlider.addEventListener('input', (e) => {
        const val = e.target.value;
        const key = Math.floor(val / 10) * 10;
        regretMsg.textContent = messages[key] || messages[80];
        regretMsg.style.transform = `translateX(${(val - 30) * 2}px)`;
    });

    // Flywheel Interactivity
    const flywheel = document.getElementById('flywheel');
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const rotateSpeed = 60 - (scrolled / 100);
        const speed = Math.max(10, rotateSpeed);
        flywheel.style.animationDuration = `${speed}s`;
    });

    // Subtle Parallax for stars
    window.addEventListener('mousemove', (e) => {
        const stars = document.querySelector('.stars-overlay');
        const x = (e.clientX - window.innerWidth / 2) * 0.02;
        const y = (e.clientY - window.innerHeight / 2) * 0.02;
        stars.style.transform = `translate(${x}px, ${y}px)`;
    });

    // Hover effect for Taste items
    document.querySelectorAll('.t-item').forEach(item => {
        item.addEventListener('mouseenter', () => {
            if (item.classList.contains('cool')) {
                item.style.color = 'var(--text-white)';
                item.style.backgroundColor = 'var(--accent-orange)';
                item.style.paddingLeft = '10px';
            }
        });
        item.addEventListener('mouseleave', () => {
            if (item.classList.contains('cool')) {
                item.style.color = 'var(--accent-orange)';
                item.style.backgroundColor = 'transparent';
                item.style.paddingLeft = '0';
            }
        });
    });

    console.log('📦 Jeff Bezos System | Always Day 1 | Growth Flywheel Active');
});
