/* Obsidian Callout & Math Auto-Render */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Process Obsidian Callouts
    // Obsidian format in HTML usually starts with [!TYPE] in a blockquote
    const blockquotes = document.querySelectorAll('.article-content blockquote');

    blockquotes.forEach(bq => {
        const firstLine = bq.querySelector('p');
        if (!firstLine) return;

        const match = firstLine.innerHTML.match(/^\[!(\w+)\](.*)/);
        if (match) {
            const type = match[1].toLowerCase();
            const titleText = match[2].trim() || type;

            bq.classList.add('callout');
            bq.setAttribute('data-type', type);

            // Reconstruct inner content
            const titleEl = document.createElement('div');
            titleEl.className = 'callout-title';

            const iconMap = {
                note: '📝',
                info: 'ℹ️',
                todo: '✅',
                tip: '💡',
                success: '✔️',
                warning: '⚠️',
                danger: '🔥',
                bug: '🐛',
                example: '📋',
                quote: '💬'
            };

            titleEl.innerHTML = `<span>${iconMap[type] || '📝'}</span> <span>${titleText}</span>`;

            // Remove the [!TYPE] line from first paragraph
            firstLine.innerHTML = firstLine.innerHTML.replace(/^\[!\w+\](.*)/, '').trim();
            if (firstLine.innerHTML === '') firstLine.remove();

            bq.prepend(titleEl);
        }
    });

    // 2. Wrap Wikilinks [[Link]] or [[Link|Alias]]
    // This is a safety measure if they weren't converted during sync
    const content = document.querySelector('.article-content');
    if (content) {
        content.innerHTML = content.innerHTML.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (match, target, alias) => {
            const label = alias || target;
            // Convert 'My Page' to 'my-page' for URL
            const url = '/posts/' + target.toLowerCase().trim().replace(/\s+/g, '-');
            return `<a href="${url}" class="wikilink">${label}</a>`;
        });
    }

    // 3. View Transitions API Support (if browser supports it)
    if (document.startViewTransition) {
        window.addEventListener('popstate', () => {
            document.startViewTransition(() => {
                // The actually logic for SPA navigation would go here, 
                // but for multi-page we just leverage browser default or simple fades.
            });
        });
    }
});
