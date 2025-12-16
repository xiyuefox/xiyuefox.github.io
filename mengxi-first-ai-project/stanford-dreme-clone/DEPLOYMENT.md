# Stanford DREME TE - Deployment Guide

## Cloudflare Pages Deployment

### 1. Install/Update Wrangler CLI (v2+)
```bash
npm install -g wrangler --force
```

### 2. Login to Cloudflare
```bash
wrangler login
```
This will open a browser window to authenticate with your Cloudflare account.

### 3. Initialize Cloudflare Pages project
```bash
cd /Users/hulimofaqiu/mengxi-first-ai-project/stanford-dreme-clone
wrangler pages init
```
- Enter project name: `stanford-dreme-clone`
- Select framework: `Static HTML`
- Build command: `false`
- Dist directory: `.`
- Select your Cloudflare account

### 4. Deploy the website
```bash
wrangler pages deploy .
```

After deployment, you'll get a URL like:
```
https://stanford-dreme-clone.pages.dev
```