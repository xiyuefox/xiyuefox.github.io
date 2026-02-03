document.addEventListener('DOMContentLoaded', () => {
    // create overlay
    const overlay = document.createElement('div');
    overlay.className = 'lightbox-overlay';
    document.body.appendChild(overlay);

    // image element in overlay
    const overlayImg = document.createElement('img');
    overlay.appendChild(overlayImg);

    // close on click
    overlay.addEventListener('click', () => {
        overlay.classList.remove('active');
    });

    // attach click listeners to all article images
    const images = document.querySelectorAll('.post-content img');
    images.forEach(img => {
        img.addEventListener('click', function (e) {
            e.stopPropagation(); // prevent bubbling
            overlayImg.src = this.src;
            overlayImg.alt = this.alt;
            overlay.classList.add('active');
        });
    });
});
