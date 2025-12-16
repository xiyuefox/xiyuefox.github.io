# Implementation Plan: Integrate Timeline View

## Goal
Integrate the interactive "Timeline" design (`obsidian-timeline.html`) into the Hugo blog (`mengxi.space`), replacing or augmenting the static post list.

## User Review Required
> [!IMPORTANT]
> This change introduces **Alpine.js** (via CDN) and **custom CSS** to the blog. These are necessary for the interactive timeline.

## Proposed Changes

### 1. Asset Migration
- **[NEW]** `blog/static/css/unified-styles.css`
  - Copy content from `css/unified-styles.css`.
- **[NEW]** `blog/static/timeline-data.json`
  - This will be the source of truth for the timeline data.
  - We will update `obsidian-sync.py` to output to this location (or copy it).

### 2. Layout Implementation
- **[NEW]** `blog/layouts/page/timeline.html` (or `themes/starter-theme/layouts/page/timeline.html`)
  - converting `obsidian-timeline.html` into a Hugo template.
  - It will fetch `/timeline-data.json` using Alpine.js.

### 3. Content Creation
- **[NEW]** `blog/content/timeline.md`
  - Frontmatter: `layout: "timeline"`, `title: "Timeline"`.

## Verification Plan
1.  **Run Sync**: Execute `python3 obsidian-sync.py` and verify `blog/static/timeline-data.json` is created/updated.
2.  **Build Site**: Run `hugo server` and check `http://localhost:1313/timeline`.
3.  **Visual Check**: Verify the timeline looks like the prototype and loads data.
