# Early Learning Hub - Deployment Guide

## Recommended: Cloudflare Pages (simpler for static websites)

### 1. Install Wrangler CLI (v2+)
```bash
npm install -g wrangler
```

### 2. Login to Cloudflare
```bash
wrangler login
```
This will open a browser window to authenticate with your Cloudflare account.

### 3. Initialize Cloudflare Pages project
Navigate to your project folder and run:
```bash
cd /Users/hulimofaqiu/mengxi-first-ai-project/early-learning-hub
wrangler pages init
```
- When prompted, enter a project name (e.g., "early-learning-hub")
- Select "Static HTML" as the framework
- Set build command to `false` (we don't need to build anything)
- Set dist directory to `.` (current directory)
- Select your Cloudflare account

### 4. Deploy the website
```bash
wrangler pages deploy .
```

### 5. Access your website
After successful deployment, Cloudflare will provide you with a URL like:
```
https://early-learning-hub.pages.dev
```

---

## Cloudflare Workers (alternative for dynamic functionality)

If you plan to add dynamic features later, you can use Cloudflare Workers:

### 1. Initialize Workers project
```bash
wrangler init early-learning-hub-worker
cd early-learning-hub-worker
```

### 2. Replace worker.js with your code
Edit `src/worker.js` to serve static files or add API endpoints.

### 3. Deploy Workers
```bash
wrangler deploy
```

---

## Next steps for AI tutor functionality:

To add the AI tutor chat feature, you'll need to:
1. Obtain a Claude API key from https://console.anthropic.com/
2. Modify `tutor.html` to include a secure way to handle API requests
3. Update the chat JavaScript to communicate with the Claude API

For security reasons, **never expose your API key directly in client-side JavaScript**.
Consider using a Cloudflare Worker as a proxy to handle API requests.

Let me know if you need assistance with any of these steps!
