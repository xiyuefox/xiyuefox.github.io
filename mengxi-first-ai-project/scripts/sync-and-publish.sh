#!/bin/bash

# Configuration
PROJECT_DIR="$HOME/mengxi-first-ai-project"
SCRIPT_PATH="$PROJECT_DIR/scripts/obsidian_to_hugo.py"
BLOG_DIR="$PROJECT_DIR/blog"
PROJECT_NAME="mengxi-blog"

# Load environment variables (such as GEMINI_API_KEY) from .env if it exists
if [ -f "$PROJECT_DIR/.env" ]; then
    echo "🔑 Loading environment variables from .env"
    export $(cat "$PROJECT_DIR/.env" | grep -v '^#' | xargs)
fi

echo "🚀 Starting Automated Publishing Workflow..."

# 0a. Sync Ambient Music Playlist from local folder
echo "🎵 Syncing NetEase Music Ambient Tracks..."
ncmdump -d "$HOME/Music/网易云音乐" -o "$PROJECT_DIR/images/music" 2>/dev/null || true
python3 "$PROJECT_DIR/scripts/sync_all_music.py"

# 0b. Re-generate Daily Quote & Sound Dashboard on index.html
python3 "$PROJECT_DIR/scripts/generate_daily_quote.py"

# 0c. Fetch External Montessori & Smart Feeds
echo "🥑 Fetching Montessori Content..."
python3 "$PROJECT_DIR/scripts/fetch_montessori.py"

echo "🍼 Fetching Newborn Care Content..."
python3 "$PROJECT_DIR/scripts/fetch_newborn_care.py"

echo "🥣 Fetching Dingxiang Mama Content..."
python3 "$PROJECT_DIR/scripts/fetch_dxy_mom.py"

echo "🧩 Fetching Math Puzzles Content..."
python3 "$PROJECT_DIR/scripts/fetch_math_puzzles.py"

echo "🔄 正在解析数学逻辑与 Smart Games 矩阵..."
python3 "$PROJECT_DIR/scripts/fetch_logic_puzzles.py"

python3 "$PROJECT_DIR/scripts/fetch_hn_feed.py"

echo "🔄 正在同步 poche.app 精神母舰看板..."
python3 "$PROJECT_DIR/scripts/fetch_poche_feed.py"

echo "🏥 正在拉取红房子就医直通车数据..."
python3 "$PROJECT_DIR/scripts/fetch_redhouse_nav.py"


# 1. Run Python Sync Script (Content)
echo "📦 Syncing Obsidian Content..."
python3 "$SCRIPT_PATH"

# 1b. Run Timeline Sync Script (Data)
echo "⏳ Syncing Timeline Data..."
python3 "$PROJECT_DIR/obsidian-sync.py"

# 1c. Sync Designer Showcase (Themes & Pages)
echo "🎨 Syncing Designer Showcase..."
cp -r "$PROJECT_DIR/designer-showcase/" "$BLOG_DIR/static/designer-showcase/"

# 1d. Sync Root App Content (SPA & Tools)
echo "🛠️ Syncing Root App Content..."
cp "$PROJECT_DIR/index.html" "$BLOG_DIR/static/index.html"
cp "$PROJECT_DIR/post.html" "$BLOG_DIR/static/post.html"
mkdir -p "$BLOG_DIR/static/apps"
cp -r "$PROJECT_DIR/apps/" "$BLOG_DIR/static/apps/"
mkdir -p "$BLOG_DIR/static/posts/md"
cp -r "$PROJECT_DIR/posts/md/" "$BLOG_DIR/static/posts/md/"
cp -r "$PROJECT_DIR/css/" "$BLOG_DIR/static/css/"
cp -r "$PROJECT_DIR/images/" "$BLOG_DIR/static/images/"

# 2. Build Hugo Site
echo "🔨 Building Hugo site..."
cd "$BLOG_DIR" || exit
hugo --minify

# 2b. Overwrite with Static Root Pages (Fix Hugo Override Bug)
echo "📄 Overwriting index.html & post.html for homepage dashboard..."
cp "$PROJECT_DIR/index.html" "$BLOG_DIR/public/index.html"
cp "$PROJECT_DIR/post.html" "$BLOG_DIR/public/post.html"

# 3. Deploy to Cloudflare
echo "☁️ Deploying to Cloudflare..."
npx wrangler pages deploy public --project-name "$PROJECT_NAME"

# 4. Notification
echo "✅ Done!"
osascript -e 'display notification "Blog Synced & Published!" with title "Mengxi Blog"'
