#!/bin/bash

# Baby Time Travel to mengxi.space Deployment Script
# This script builds Hugo and deploys to Cloudflare Pages

echo "🚀 Baby Time Travel → mengxi.space Deployment"
echo "=============================================="
echo ""

# Navigate to Hugo blog directory
cd /Users/hulimofaqiu/mengxi-first-ai-project/blog

echo "📦 Building Hugo site..."
hugo

if [ $? -eq 0 ]; then
    echo "✅ Hugo build successful!"
    echo ""
    echo "📂 Baby Time Travel files located at:"
    echo "   public/baby-time-travel/index.html"
    echo "   public/baby-time-travel/script.js"
    echo ""
    
    # Check if sync script exists
    if [ -f "/Users/hulimofaqiu/mengxi-first-ai-project/scripts/sync-and-publish.sh" ]; then
        echo "🔄 Running sync-and-publish script..."
        bash /Users/hulimofaqiu/mengxi-first-ai-project/scripts/sync-and-publish.sh
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "🎉 DEPLOYMENT COMPLETE!"
            echo ""
            echo "🌐 Your site will be live at:"
            echo "   https://mengxi.space/baby-time-travel/"
            echo ""
            echo "⏱️  Cloudflare Pages usually takes 1-2 minutes to deploy."
            echo "💡 Refresh your browser after a minute to see the changes."
        else
            echo "❌ Sync script failed. Please check the output above."
        fi
    else
        echo "⚠️  Sync script not found at: scripts/sync-and-publish.sh"
        echo ""
        echo "📋 Manual deployment steps:"
        echo "   1. The Hugo build is complete (public/ directory updated)"
        echo "   2. If you use Git, run:"
        echo "      cd blog"
        echo "      git add public/baby-time-travel"
        echo "      git commit -m 'Add Baby Time Travel'"
        echo "      git push"
        echo "   3. Or manually upload public/ to Cloudflare Pages"
    fi
else
    echo "❌ Hugo build failed. Please check for errors above."
    exit 1
fi

echo ""
echo "=============================================="
echo "✅ Script complete!"
