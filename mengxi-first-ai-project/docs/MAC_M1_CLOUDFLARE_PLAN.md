
# 🍏 The M1 Mac "Cloud Garden" Plan
**For:** Liberal Arts Students on M1 Macs | **Platform:** Cloudflare Pages (No-Git) | **Time:** 4-6 Hours/Week

Welcome! You have a massive advantage: **You already own the land (your Cloudflare domain)**. This plan is designed to be the *shortest path* between your writing and that domain, skipping the confusing "Git/GitHub" detour entirely.

**Core Philosophy:**
1.  **Direct Flight:** We upload files straight from your Mac to Cloudflare.
2.  **Writing Sanctuary:** Obsidian is where you live. Technology stays in the basement.
3.  **The "Teleporter":** We will upgrade from "Manual Upload" to "One-Click Deploy" gradually.

---

## 🌱 Phase 1: The Potting Shed (Weeks 1-4)
**Goal:** A working blog on your M1 Mac. Safe, private, offline.

### Week 1: The Magic Wand (Homebrew)
*   **Concept:** The "App Store" for experts, but we strictly follow the recipe.
*   **M1 Mac Step:**
    1.  Open **Terminal** (Command + Space, type "Terminal").
    2.  Copy-paste the Homebrew install command (from `brew.sh`).
    3.  *Important:* Read the "Next Steps" output! You might need to add it to your "Path". If confused, ask an AI: "How to add Homebrew to Path on M1 Mac".
    4.  Run `brew install hugo`.
    5.  **Celebration:** Type `hugo version`. Seeing numbers means you won!

### Week 2: The Structure (Hugo)
*   **Concept:** Building the bookshelf.
*   **Tasks:**
    1.  Open Terminal. Type `cd Desktop`.
    2.  Type `hugo new site my-blog`.
    3.  Go to your Desktop. See the folder `my-blog`? **That is your website.**
    4.  Download the **PaperMod** theme zip file. Unzip it into `my-blog/themes/PaperMod`.
    5.  **Milestone:** You have a website folder you can touch and see.

### Week 3: The Writer's Room (Obsidian)
*   **Concept:** Moving in your furniture.
*   **Tasks:**
    1.  Open **Obsidian**.
    2.  "Open folder as Vault" -> Select `Desktop/my-blog/content/posts`.
    3.  Write your first note: "Hello World.md".
    4.  **Vital Step:** Add the "Frontmatter" (The library card) at the top:
        ```yaml
        ---
        title: "Hello World"
        date: 2024-01-01
        draft: false
        ---
        ```
    5.  Write your heart out.

### Week 4: The Mirror (Local Preview)
*   **Concept:** Looking in the mirror before going out.
*   **Tasks:**
    1.  Open Terminal.
    2.  Type `cd Desktop/my-blog`.
    3.  Type `hugo server`.
    4.  Open Safari and go to `http://localhost:1313`.
    5.  **Magic:** Edit your Obsidian note. Save. Look at Safari. *It changed instantly.*

---

## ☁️ Phase 2: The Cloud Greenhouse (Weeks 5-8)
**Goal:** Your first live website. Direct upload.

### Week 5: The Build (Making the Book)
*   **Concept:** Printing the pages.
*   **Tasks:**
    1.  In Terminal (`my-blog` folder), type `hugo`. (No "server", just "hugo").
    2.  Look in your folder. A new folder called `public` appeared.
    3.  This `public` folder contains your *entire* website ready for the world.

### Week 6: The Launch (Cloudflare Direct)
*   **Concept:** Putting the book on the shelf.
*   **Tasks:**
    1.  Log in to **Cloudflare Dashboard**.
    2.  Go to **Workers & Pages** -> **Create Application** -> **Pages** -> **Upload Assets**.
    3.  Name it `my-blog`.
    4.  **Drag and drop** your `public` folder into the browser window.
    5.  Click "Deploy Site".
    6.  **Celebration:** Cloudflare gives you a link (e.g., `my-blog.pages.dev`). Click it. YOU ARE LIVE!

### Week 7: The Nameplate (Domain Binding)
*   **Concept:** Hanging your shingle.
*   **Advantage:** Since your domain is *already* in Cloudflare, this is instant.
*   **Tasks:**
    1.  In your Cloudflare Pages project (`my-blog`), click **Custom Domains**.
    2.  Click **Set up a custom domain**.
    3.  Type your domain (e.g., `alex-writes.com`).
    4.  Cloudflare will say "I manage this DNS! easy peasy."
    5.  Click **Activate**.
    6.  **Milestone:** Visit your real .com domain. Cry tears of joy.

### Week 8: The Rhythm (Manual Cycle)
*   **Concept:** Weekly watering.
*   **Tasks:**
    1.  Write in Obsidian all week.
    2.  Friday Ritual:
        - Run `hugo` command.
        - Drag `public` folder to Cloudflare Dashboard.
    3.  It takes 2 minutes. It is simple. It works.

---

## ⚡ Phase 3: The Teleporter (Weeks 9-12)
**Goal:** Stop dragging folders. Let the Mac do it.

### Week 9: The Engine (Node.js)
*   **Concept:** Installing the teleporter battery.
*   **Tasks:**
    1.  Terminal: `brew install node`.
    2.  Terminal: `npm install -g wrangler`. (Wrangler is the Cloudflare courier).
    3.  Type `npx wrangler login`. It will open Safari. Click "Allow".
    4.  Now your Mac is authorized to talk to Cloudflare.

### Week 10: The First Beam (CLI Deploy)
*   **Concept:** Sending the package through the tube.
*   **Tasks:**
    1.  Terminal: `hugo` (Build the site).
    2.  Terminal: `npx wrangler pages deploy public --project-name my-blog`.
    3.  Watch the text fly by. "Upload complete".
    4.  Check your site. It updated! No dragging required.

### Week 11: The "One-Click" Button (Automator)
*   **Concept:** Hiring a butler.
*   **Tasks:**
    1.  Open the Mac app **Shortcuts** or **Automator**.
    2.  Create a "Run Shell Script".
    3.  Paste your commands:
        ```bash
        cd ~/Desktop/my-blog
        /opt/homebrew/bin/hugo
        /opt/homebrew/bin/npx wrangler pages deploy public --project-name my-blog
        ```
    4.  Save it as an App called "Publish Blog".
    5.  Put it on your Dock.

### Week 12: Speed & CDN
*   **Concept:** Global distribution.
*   **Tasks:**
    1.  Enable "Early Hints" in Cloudflare Speed settings.
    2.  Turn on "Rocket Loader".
    3.  Your M1 Mac + Cloudflare combination is now faster than 99% of WordPress sites.

---

## 🚀 Phase 4: Auto-Pilot (Weeks 13-16)
**Goal:** Frictionless creativity.

### Week 13: Image Optimization
*   **Concept:** Compressing the luggage.
*   **Task:** Learn to put images in `static/images`.
*   **Tip:** Use an app like "ImageOptim" (Mac) before putting them in the folder. Keeps your site lightning fast.

### Week 14: Obsidian Polish
*   **Focus:** The Writing Environment.
*   **Task:** Install the "Shell Commands" plugin in Obsidian.
*   **Magic:** Bind your "Publish Blog" script to a button *inside* Obsidian.
*   **Result:** You write. You click one button. The world sees it.

### Week 15: Security & Backups (The "Just in Case")
*   **Concept:** Fire insurance.
*   **Task:** Since we aren't using GitHub, simply copy your `my-blog` folder to Google Drive or iCloud once a month. Or use Time Machine. Keep it simple.

### Week 16: Graduation 🎓
*   **Task:** Write your "Manifesto".
*   **Reflection:** You built a system that relies on YOU, not on a platform algorithm.
*   **Celebration:** Buy yourself a nice coffee. You are a webmaster.

---

## 🧠 "Why is this better for me?"

1.  **No Git/GitHub:** You save about 50 hours of learning curve and stress.
2.  **M1 Speed:** Hugo builds your site in 0.2 seconds on an M1 chip. Instant gratification.
3.  **Cloudflare Power:** You are using enterprise-grade hosting for free.
4.  **Local Control:** If the internet breaks, you still have all your writing on your Mac.

**Troubleshooting Local Command:**
Typing `hugo` works? Great.
If not, try `/opt/homebrew/bin/hugo`. (Homebrew lives there on M1 Macs).
