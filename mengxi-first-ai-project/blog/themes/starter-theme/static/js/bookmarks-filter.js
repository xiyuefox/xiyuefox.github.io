/* Bookmarks Filtering Logic */
document.addEventListener('DOMContentLoaded', () => {
    const pills = document.querySelectorAll('.filter-pill');
    const cards = document.querySelectorAll('.bookmark-card');

    pills.forEach(pill => {
        pill.addEventListener('click', () => {
            const filter = pill.getAttribute('data-filter');

            // Update Active State
            pills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');

            // Filter Cards
            cards.forEach(card => {
                const category = card.getAttribute('data-category').toLowerCase();

                if (filter === 'all' || category === filter.toLowerCase()) {
                    card.style.display = 'flex';
                    // Trigger fade in
                    card.classList.add('reveal-item', 'active');
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});
