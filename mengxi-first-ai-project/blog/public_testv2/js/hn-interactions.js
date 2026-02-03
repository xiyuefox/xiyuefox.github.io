// Hacker News Interactions
// Handles 'hide', 'vote', and other HN-style interactions

document.addEventListener('DOMContentLoaded', () => {
    // Restore hidden state
    const hiddenPosts = JSON.parse(localStorage.getItem('hn_hidden_posts') || '[]');
    hiddenPosts.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.style.display = 'none';
        // Also hide the next sibling if it's metadata (not applicable in current DOM structure, but good safety)
    });
});

function hidePost(element, postId) {
    // 1. Find the container
    // Structure: .hn-meta [a] -> .hn-item-container
    const container = element.closest('.hn-item-container');
    if (container) {
        // 2. Hide visual
        container.style.display = 'none';

        // 3. Persist
        // Ensure container has ID or use specific identifier
        // We use RelPermalink as ID usually, passing it in
        if (postId) {
            let hidden = JSON.parse(localStorage.getItem('hn_hidden_posts') || '[]');
            if (!hidden.includes(postId)) {
                hidden.push(postId);
                localStorage.setItem('hn_hidden_posts', JSON.stringify(hidden));
            }
        }
    }
    return false; // Prevent navigation
}

function unhideAll() {
    localStorage.removeItem('hn_hidden_posts');
    window.location.reload();
}
