// main.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('页面已加载');
    
    // 主题切换功能
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        const body = document.body;
        const icon = themeToggle.querySelector('i');
        
        themeToggle.addEventListener('click', function() {
            if (body.classList.contains('dark')) {
                body.classList.remove('dark');
                body.classList.add('light');
                if (icon) {
                    icon.classList.remove('fa-sun');
                    icon.classList.add('fa-moon');
                }
            } else {
                body.classList.remove('light');
                body.classList.add('dark');
                if (icon) {
                    icon.classList.remove('fa-moon');
                    icon.classList.add('fa-sun');
                }
            }
        });
    }
    
    // 平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            }
        });
    });
});
