#!/bin/bash

# Step 1: Download the repository zip file
echo "📥 Downloading repository..."
curl -LO https://github.com/xpzouying/xiaohongshu-mcp/archive/main.zip || { echo "❌ Download failed. Please download manually from: https://github.com/xpzouying/xiaohongshu-mcp/archive/main.zip"; exit 1; }

# Step 2: Extract the zip file
echo "📦 Extracting repository..."
unzip main.zip || { echo "❌ Extraction failed. Please extract manually."; exit 1; }

# Step 3: Navigate to the extracted directory
echo "📂 Entering repository directory..."
cd xiaohongshu-mcp-main || { echo "❌ Directory not found."; exit 1; }

# Step 4: Install dependencies
echo "🔧 Installing dependencies..."
go mod download || { echo "❌ Dependency installation failed."; exit 1; }
go mod tidy || { echo "❌ Dependency tidying failed."; exit 1; }

# Step 5: Start the server
echo "🚀 Starting server..."
go run . -headless=false

