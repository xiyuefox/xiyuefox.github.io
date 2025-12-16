# Blog Website Analysis & Action Plan (mengxi.space)

## 1. Site Analysis (网站分析)

### Current Site Structure
- **Framework**: Hugo (Static Site Generator)
- **Theme**: `starter-theme` (Very basic, likely custom or minimal template)
- **Content**: Sourced from `content/posts`, organized by categories (inbox, sparks, notes, ideas, growth).
- **Frontend**:
  - The live blog (`mengxi.space`) currently uses a standard list layout.
  - **Critical Gap**: You have a rich, interactive "Timeline" design (`obsidian-timeline.html`) and "Knowledge Graph" design (`obsidian-knowledge-system.html`) in your project root, but these **are not integrated** into the actual Hugo blog. They exist only as standalone prototypes.

### Issues Identified
1.  **Layout Disconnect**: The current Hugo theme does not reflect the modern, interactive designs found in your prototypes.
2.  **Missing Features**: The "Timeline" view is static hardcoded HTML in the prototype and doesn't exist in the Hugo theme.
3.  **Search**: Config indicates a `/search` page, but it's likely basic. The prototypes suggest a desire for filtered views (Notes vs Ideas).

## 2. Code Review (代码审查)

### Automation Scripts
1.  **`scripts/obsidian_to_hugo.py`** (The Content Syncer)
    - **Status**: ✅ Functional.
    - **Role**: Syncs Markdown files from your Obsidian Vault to `blog/content`.
    - **Features**: Handles folder-to-category mapping, frontmatter generation, and filename sanitization.
    - **Issue**: R2 Image uploading is currently disabled (`ENABLE_R2_UPLOAD = False`), meaning images might be broken or dependent on local relative paths which don't work well in Hugo if not copied correctly.

2.  **`obsidian-sync.py`** (The Timeline Generator)
    - **Status**: ⚠️ Disconnected.
    - **Role**: Generates `timeline-data.json` from Obsidian files.
    - **Issue**: This JSON file is generated but **never used**. Your `obsidian-timeline.html` prototype uses hardcoded Javascript data, not this JSON file.

3.  **`scripts/sync-and-publish.sh`** (The Orchestrator)
    - **Status**: ✅ Good.
    - **Role**: Automates the pipeline (Sync -> Build -> Deploy).

## 3. Progress Tracking (进度追踪)

- **Last Completed Milestone**: You successfully created the automation to move content from Obsidian to Hugo (`obsidian_to_hugo.py`) and set up the Cloudflare deployment.
- **Current State**: You are in the "Integration" phase. You have the *backend* data (Markdown/JSON) and the *frontend* design (HTML prototypes), but they are not connected.
- **Reference Docs**: Existing plans (`IMPLEMENTATION_ROADMAP.md`) are for "Sheikah Slate", not the blog.

## 4. Next Steps & Action Plan (下一步行动)

### Priority 1: Integrate Timeline View (Critical)
The most high-value task is to replace the generic "Posts" list with your custom Timeline view.

- [ ] **Step 1**: Move `timeline-data.json` to `blog/static/data/timeline.json` (or similar) so the frontend can load it.
- [ ] **Step 2**: Port `obsidian-timeline.html` into a Hugo Layout (e.g., `layouts/section/timeline.html`).
- [ ] **Step 3**: Update the logic in the HTML to fetch data from the JSON file instead of using hardcoded arrays.

### Priority 2: Style & Navigation
- [ ] **Step 1**: Migrate `css/unified-styles.css` into the Hugo theme (`blog/themes/starter-theme/static/css`).
- [ ] **Step 2**: Update the Hugo header to match the `u-nav` design from your prototypes.

### Priority 3: Image Hosting
- [ ] **Step 1**: Enable the R2 upload in `obsidian_to_hugo.py` or implement a local asset copy strategy to ensure images appear on the site.

---
**Recommendation**: I suggest we start by **Integrating the Timeline View**. I can convert your `obsidian-timeline.html` into a proper Hugo layout and connect it to your `timeline-data.json`. Shall we proceed with this?
