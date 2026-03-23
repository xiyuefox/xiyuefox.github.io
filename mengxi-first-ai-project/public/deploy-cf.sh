#!/bin/bash

# Configuration
PROJECT_NAME="mengxi-space"
BLOG_DIR="$HOME/mengxi-first-ai-project/blog"
PUBLIC_DIR="$BLOG_DIR/public"

# Check Wrangler
# We use npx so global install check might be skipped if we just rely on npx, 
# but let's check if npx works or if wrangler is in path. 
# The user instruction was "Install Wrangler... (npm global or brew)".
# But the script uses `npx wrangler`, which usually requires `npm install` locally or downloads on fly.
# Let's just check if `npm` or `npx` is available at least.

if ! command -v npx &> /dev/null; then
    echo "❌ npx not found. Please install Node.js."
    exit 1
fi

# Build
echo "🔨 Building Hugo site..."
if [ -d "$BLOG_DIR" ]; then
    cd "$BLOG_DIR" || exit
else
    echo "❌ Blog directory not found: $BLOG_DIR"
    exit 1
fi

if hugo --minify; then
    echo "✅ Hugo build successful."
else
    echo "❌ Hugo build failed."
    exit 1
fi

# Verify Output
if [ ! -f "public/index.html" ]; then
    echo "❌ Missing index.html in public directory."
    exit 1
fi

# Deploy
echo "☁️ Deploying to Cloudflare Pages..."
# Using npx to ensure we use a valid wrangler instance.
# --project-name matches what we want in CF.
if npx wrangler pages deploy public --project-name="$PROJECT_NAME"; then
    echo ""
    echo "✅ Deployed to https://$PROJECT_NAME.pages.dev"
    echo "   (Custom domain 'mengxi.space' may take a moment to propagate if configured)"
else
    echo ""
    echo "❌ Deployment failed. Check Wrangler output above."
    # If project doesn't exist, npx wrangler pages deploy usually asks to create it interactively.
    # In a script, this might hang or fail if not authenticated.
    exit 1
fi
