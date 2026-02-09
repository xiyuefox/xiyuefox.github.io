#!/bin/bash

# Configuration
PROJECT_DIR="$HOME/mengxi-first-ai-project"
SCRIPT_PATH="$PROJECT_DIR/scripts/obsidian_to_hugo.py"
BLOG_DIR="$PROJECT_DIR/blog"
PROJECT_NAME="mengxi-blog"

echo "🚀 Starting Automated Publishing Workflow..."

# 1. Run Python Sync Script (Content)
echo "📦 Syncing Obsidian Content..."
python3 "$SCRIPT_PATH"

# 1b. Run Timeline Sync Script (Data)
echo "⏳ Syncing Timeline Data..."
python3 "$PROJECT_DIR/obsidian-sync.py"

# 1c. Sync Designer Showcase (Themes & Pages)
echo "🎨 Syncing Designer Showcase..."
cp -r "$PROJECT_DIR/designer-showcase/" "$BLOG_DIR/static/designer-showcase/"

# 2. Build Hugo Site
echo "🔨 Building Hugo site..."
cd "$BLOG_DIR" || exit
hugo --minify

# 3. Deploy to Cloudflare
echo "☁️ Deploying to Cloudflare..."
npx wrangler pages deploy public --project-name "$PROJECT_NAME"

# 4. Notification
echo "✅ Done!"
osascript -e 'display notification "Blog Synced & Published!" with title "Mengxi Blog"'
