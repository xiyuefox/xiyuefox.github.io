
# 🚀 Automated Blog System Setup Guide

This guide helps you set up a fully automated blog where you write in Obsidian, push to GitHub, and Cloudflare Pages automatically builds your site using Hugo.

## 📋 Prerequisites
1.  **GitHub Account**
2.  **Cloudflare Account**
3.  **Hugo Installed Locally** (for testing)

## 🛠️ Step 1: Initialize the Project Locally (If not done)
You need to install the PaperMod theme. Run this in your project root:
```bash
git submodule add https://github.com/adityatelange/hugo-PaperMod blog/themes/PaperMod
git submodule update --init --recursive
```

## ☁️ Step 2: Configure Cloudflare Pages
1.  Log in to the **Cloudflare Dashboard**.
2.  Go to **Pages > Create a project > Connect to Git**.
3.  Select your GitHub repository (`mengxi-first-ai-project`).
4.  **Build Settings**:
    *   **Framework preset**: Hugo
    *   **Build command**: `hugo --minify`
    *   **Build output directory**: `blog/public` (Important! Since our hugo site is in a subfolder)
    *   **Root directory**: `blog` (Set this in the advanced settings if available, or rely on the workflow)
5.  **Environment Variables** (Optional):
    *   `HUGO_VERSION`: `0.120.0` (or latest)

## 🔑 Step 3: Configure Deployment Secrets (For GitHub Actions)
If you prefer using the provided GitHub Action (`.github/workflows/deploy.yml`) instead of Cloudflare's automatic git integration:
1.  Go to GitHub Repo **Settings > Secrets and variables > Actions**.
2.  Add:
    *   `CLOUDFLARE_ACCOUNT_ID`
    *   `CLOUDFLARE_API_TOKEN`

## 💎 Step 4: Obsidian Automation
1.  Open `scripts/obsidian_to_hugo.py`.
2.  Edit `OBSIDIAN_VAULT_PATH` to point to your local vault.
3.  Run the script whenever you want to publish:
    ```bash
    python3 scripts/obsidian_to_hugo.py
    ```
4.  Git commit and push the changes:
    ```bash
    git add .
    git commit -m "New blog post"
    git push origin main
    ```

## 🌍 Step 5: Custom Domain (Cloudflare)
1.  In Cloudflare Pages project, go to **Custom domains**.
2.  Click **Set up a custom domain**.
3.  Enter `your-blog.com` and follow the DNS verification steps.
