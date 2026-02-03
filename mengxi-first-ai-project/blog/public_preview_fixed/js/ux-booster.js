
// UX Booster Pack Scripts
document.addEventListener('DOMContentLoaded', () => {

    // 1. Reading Progress Bar
    const progressBar = document.createElement('div');
    progressBar.id = 'progress-bar';
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', () => {
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (scrollTop / scrollHeight) * 100;
        progressBar.style.width = scrolled + '%';

        // 2. Back To Top Visibility
        const backToTopBtn = document.getElementById('back-to-top');
        if (backToTopBtn) {
            if (scrollTop > 300) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        }
    });

    // 2. Back To Top Button Injection
    const backBtn = document.createElement('button');
    backBtn.id = 'back-to-top';
    backBtn.innerHTML = '↑';
    backBtn.ariaLabel = "Back to Top";
    backBtn.onclick = () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };
    document.body.appendChild(backBtn);

});
