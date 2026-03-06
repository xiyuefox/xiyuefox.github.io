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

    // Simple Drag Simulator for Spawn Blocks
    const blocks = document.querySelectorAll('.s-block');
    blocks.forEach(block => {
        block.addEventListener('mousedown', (e) => {
            block.style.cursor = 'grabbing';
            block.style.position = 'relative';
            block.style.zIndex = '10';
        });

        block.addEventListener('mouseup', () => {
            block.style.cursor = 'grab';
        });
    });

    // Auto-typing placeholder simulator
    const placeholder = document.querySelector('.placeholder-text');
    const texts = [
        "我想做一个给奶奶的一键通话应用...",
        "我想在浏览器里画出所有论文的思维导图...",
        "我想把写软件变得像发推文一样简单...",
        "我想创建一个协作式的认知外脑..."
    ];
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;

    function type() {
        const currentText = texts[textIndex];
        if (isDeleting) {
            placeholder.textContent = currentText.substring(0, charIndex - 1);
            charIndex--;
        } else {
            placeholder.textContent = currentText.substring(0, charIndex + 1);
            charIndex++;
        }

        let typeSpeed = isDeleting ? 50 : 100;

        if (!isDeleting && charIndex === currentText.length) {
            typeSpeed = 2000;
            isDeleting = true;
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            textIndex = (textIndex + 1) % texts.length;
            typeSpeed = 500;
        }

        setTimeout(type, typeSpeed);
    }

    if (placeholder) {
        type();
    }

    // Interactive Button Pulse
    const callBtn = document.querySelector('.big-action-btn');
    if (callBtn) {
        callBtn.addEventListener('click', () => {
            callBtn.style.transform = 'scale(0.9)';
            setTimeout(() => {
                callBtn.style.transform = 'scale(1)';
                alert('🚀 即将启动：与奶奶的 FaceTime 链接...');
            }, 100);
        });
    }

    console.log('📄 Tyler Angert System | Patina Systems | Software as Expression');
});
