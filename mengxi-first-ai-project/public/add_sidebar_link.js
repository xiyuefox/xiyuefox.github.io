const fs = require('fs');
const path = require('path');

const filesToEdit = [
    path.join(__dirname, '../index.html'),
    path.join(__dirname, '../public/index.html')
];

// Regex matching the link optionally containing anything inside the tag.
const targetPattern = /<a href="post\.html\?post=dxy-mom-feed" class="tg-nav-link">[\s\S]*?<\/a>/g;

const newItem = `<a href="post.html?post=dxy-mom-feed" class="tg-nav-link">
                                <span class="tg-nav-icon">🍼</span> ./maternity_feed
                            </a>
                            <a href="post.html?post=hn-topics-feed" class="tg-nav-link">
                                <span class="tg-nav-icon">🤖</span> ./geek_mom
                            </a>`;

for (const filePath of filesToEdit) {
    if (!fs.existsSync(filePath)) {
        console.log(`File ${filePath} doesn't exist, skipping`);
        continue;
    }
    let content = fs.readFileSync(filePath, 'utf8');
    const hasMatch = targetPattern.test(content);
    if (!hasMatch) {
        console.log(`Target not found in ${filePath}`);
        continue;
    }
    // reset index
    targetPattern.lastIndex = 0;
    content = content.replace(targetPattern, (match) => {
        // preserve spacing before the node if possible
        const spaces = match.match(/^\s*/)[0];
        return match + '\n' + spaces + `<a href="post.html?post=hn-topics-feed" class="tg-nav-link">\n` +
               spaces + `    <span class="tg-nav-icon">🤖</span> ./geek_mom\n` +
               spaces + `</a>`;
    });
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Updated ${filePath}`);
}
