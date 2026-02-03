/**
 * INTELLIGENT CODE & TERMINAL ENHANCER
 * - Adds Mac-style Copy buttons
 * - Detects language from Hugo classes and injects expansion logic
 */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Target all Hugo syntax highlight wrappers
    // Hugo 0.60+ with lineNos=true outputs a table inside .highlight div
    // We want to attach buttons to the .highlight wrapper
    const highlights = document.querySelectorAll('.highlight');

    highlights.forEach((wrapper) => {
        // --- A. Identify Language ---
        // Hugo adds class "language-python" OR "highlight language-python" depending on config
        // We grep the class list for "language-*"
        let lang = "";
        wrapper.classList.forEach(cls => {
            if (cls.startsWith('language-')) {
                lang = cls.replace('language-', '');
            }
        });

        // Sometimes the class is on the <code> or inner <div> if not using tables
        // If wrapper didn't have it, try deeper
        if (!lang) {
            const codeBlock = wrapper.querySelector('code');
            if (codeBlock) {
                codeBlock.classList.forEach(cls => {
                    if (cls.startsWith('language-')) {
                        lang = cls.replace('language-', '');
                    }
                });
            }
        }

        // Set Attribute for CSS to display
        if (lang) {
            wrapper.setAttribute('data-lang', lang);
        } else {
            wrapper.setAttribute('data-lang', 'CODE');
        }


        // --- B. Add Copy Button ---
        const button = document.createElement('button');
        button.className = 'copy-code-btn';
        button.innerText = 'Copy';
        button.style.top = '5px'; // Align with header

        button.addEventListener('click', () => {
            // Find the actual text. If using line numbers, it's in the second td .lntd
            // If not, it's in <pre><code>
            let codeText = "";

            // Try logic for table-based line numbers first
            const codeTd = wrapper.querySelector('.lntd:last-child pre, .lntd:last-child code');

            if (codeTd) {
                codeText = codeTd.innerText;
            } else {
                // Fallback for standard blocks
                codeText = wrapper.querySelector('code') ? wrapper.querySelector('code').innerText : wrapper.innerText;
            }

            navigator.clipboard.writeText(codeText).then(() => {
                button.innerText = 'Copied!';
                setTimeout(() => button.innerText = 'Copy', 2000);
            }).catch(err => {
                console.error('Copy failed', err);
                button.innerText = 'Error';
            });
        });

        wrapper.appendChild(button);

        // --- C. Expand/Collapse Logic for Massive Blocks ---
        // If height > 500px, collapse it
        if (wrapper.offsetHeight > 500) {
            wrapper.style.maxHeight = '500px';
            wrapper.style.overflowY = 'hidden'; // Hide vertical overflow

            const expandBtn = document.createElement('button');
            expandBtn.innerText = 'Show More 🔽';
            expandBtn.style.cssText = `
                position: absolute;
                bottom: 0px;
                left: 0;
                width: 100%;
                padding: 10px;
                background: linear-gradient(transparent, #282c34 80%);
                border: none;
                color: white;
                cursor: pointer;
                font-family: var(--font-body);
                font-weight: bold;
                z-index: 100;
            `;

            expandBtn.onclick = () => {
                wrapper.style.maxHeight = 'none';
                wrapper.style.overflowY = 'visible';
                expandBtn.remove();
            };

            wrapper.appendChild(expandBtn);
        }
    });
});
