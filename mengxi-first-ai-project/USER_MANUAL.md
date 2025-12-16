# 📖 My Obsidian Blog User Manual

## 🌟 How to Write & Publish

### 1. Write in Obsidian ✍️
- Open your **Obsidian** app.
- Write a new article or edit an existing one in the `content/posts` folder.
- **Example Frontmatter** (Put this at the top of every article):
  ```yaml
  ---
  title: "My Amazing Post"
  date: 2025-12-14
  draft: false
  ---
  ```
- *Tip: Set `draft: false` when you are ready to publish!*

### 2. Preview (Optional) 👁️
- Open Terminal and run: `hugo server -D` in the `blog` folder.
- Go to `http://localhost:1313` to see your changes in real-time.

### 3. One-Click Publish 🚀
- Double-click the **"Publish Blog"** app we created in your project folder.
- Wait for the "Blog Deployed Successfully!" notification.
- Done! Your changes are live on your domain.

---

## 🛠️ Troubleshooting

- **Images not showing?** Make sure you put them in `blog/static/images` or use standard Markdown image links.
- **Changes not appearing?** Check if `draft: true` is still set in your article's frontmatter.
- **Deployment Failed?** Open Terminal and type `npx wrangler login` again to refresh your connection.

---
*Happy Blogging!*
