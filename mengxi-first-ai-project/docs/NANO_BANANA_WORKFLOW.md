# 🍌 Nano Banana Pro: Visual Intelligence Workflow
**Version**: 1.0.0
**Status**: Production Ready
**Philosophy**: "Make it look hand-drawn, make it feel premium."

## 1. Overview
The Nano Banana Pro Workflow is a hybrid visual processing system designed to transform technical diagrams into engaging, human-centric visual notes. It solves the "Boring Diagram Problem" by applying a consistent hand-drawn aesthetic across the entire blog without manual overhead.

## 2. The Hybrid Architecture
We use a **Two-Tier Strategy** to balance quality and scalability.

### Tier A: Hero Visuals (The "Wow" Factor)
*   **Target**: The top 3-5 most complex or critical concepts in an article (Mindmaps, timelines).
*   **Method**: Generative AI (DALL-E 3 / Imagen 3).
*   **Style**: "Nano Banana Sketch Note" – High fidelity, colored markers, paper texture, rich illustrations.
*   **Storage**: Static PNGs in `blog/static/images/`.
*   **Integration**: Standard Markdown Image Links `![[image.png]]`.

### Tier B: Dynamic Batching ( The "Scale" Factor)
*   **Target**: The remaining 100+ diagrams (Flowcharts, simple graphs, sequence diagrams).
*   **Method**: Client-side Rendering (Mermaid.js).
*   **Style**: "Nano Banana Dynamic" – CSS-injected `Patrick Hand` font, custom stroke colors, hand-drawn node shapes.
*   **Storage**: Code-only (`mermaid` blocks in Markdown).
*   **Integration**: Automatic JS injection via `baseof.html`.

## 3. Implementation Details

### 3.1. Dynamic Rendering Engine (Tier B)
**File**: `themes/starter-theme/layouts/_default/baseof.html`

We inject a custom initialization script that:
1.  Intercepts all `pre code.language-mermaid` blocks.
2.  Converts them to `div.mermaid`.
3.  Initializes Mermaid with:
    *   `fontFamily`: "Patrick Hand" (Google Font).
    *   `theme`: "base".
    *   `themeVariables`: 
        *   Primary Color: `#fffef0` (Cream Paper).
        *   Line Color: `#2c3e50` (Ink Blue).
        *   Secondary Color: `#f1c40f` (Highlighter Yellow).

**Usage**: No action needed. Just write standard mermaid code.

### 3.2. Hero Image Pipeline (Tier A)
**Files**: `scripts/obsidian_to_hugo.py`, `scripts/upload_helper.py`

1.  **Generate**: Use AI prompt "Hand-drawn sketch note style..."
2.  **Save**: Place image in Obsidian Vault.
3.  **Link**: Use `![[image.png]]`.
4.  **Sync**: The `obsidian_to_hugo` script automatically:
    *   Detects the wikilink.
    *   Copies the image to `static/images/`.
    *   Converts link to relative path `/images/image.png`.
    *   (Optional) Uploads to R2 if enabled.

## 4. Disaster Recovery & Resilience
*   **Local Fallback**: If Cloudflare R2 is unreachable, the system automatically builds using local assets (`/images/`).
*   **Link Reversion**: `scripts/revert_image_urls.py` can convert broken absolute URLs back to resilient Wikilinks.

## 5. Style Guide
*   **Fonts**: *Patrick Hand* for text, *Nunito* for UI.
*   **Colors**: 
    *   Background: `#fffef0`
    *   Ink: `#2c3e50`
    *   Accent: `#e74c3c` (Corrections), `#2ecc71` (Solutions).

---
*Maintained by Antigravity Agent*

## 6. Gap Analysis: Nano Banana Pro vs. Standard Image Skills

We analyzed our workflow against the industry-standard `gemini-image-skill` pattern.

| Component | 🔴 Reference (Standard Skill) | 🟢 Banana Pro (Our System) | 🚀 Implications |
| :--- | :--- | :--- | :--- |
| **Auth** | **Requires API Key** (User pays/manages). | **Zero-Config** (Uses Agent's internal tools). | **Advantage**: Free, boundless usage. No key management hell. |
| **Control** | **Prompt-Based** ("Draw a cat"). | **Workflow-Based** (Mermaid -> Sketch). | **Advantage**: We transform *structured data* (diagrams), not just loose text. |
| **Style** | **Variable** (Dependent on prompt). | **Enforced** (Code-injected Font/Colors). | **Advantage**: Brand consistency across 100+ diagrams. |
| **Persistence** | **Ephemeral** (Returns temporary URL). | **Permanent** (Saves to Repo/R2). | **Advantage**: You own your assets. Zero broken links. |

### 🔍 Missing Feature: Image-to-Image (Img2Img)
The reference skill supports `Image + Prompt` generation (e.g., "Make this photo look like a sketch").
*   **Gap**: Currently, we generate Hero images from scratch (Text-to-Image).
*   **Fix**: We can upgrade our workflow to accept a "Style Reference" image (e.g., a master sketch) to ensure every new Hero image perfectly matches the previous one's stroke width and color palette.

## 7. Improvement Recommendations

### Recommendation A: The "Prompt Wrapper" Script
Instead of writing long prompts manually, we should create a tiny script that wraps your intent in the "Banana Style":
*   **Input**: "A brain"
*   **Auto-Prompt**: "Hand-drawn sketch note style illustration of **A brain**, using thick 2px ink lines, #f1c40f highlights, on textured paper background."

### Recommendation B: Local Style Reference
Since you don't have an external API key, we will leverage the Agent's `generate_image` ability to read local files.
*   **Action**: Save one "Perfect" diagram as `reference-style.png`.
*   **Usage**: When asking the Agent for a new image, tell it: *"Use reference-style.png as the style guide."*

### Recommendation C: Vector Output
Mermaid is SVG (Scalable). Our AI images are PNG (Pixels).
*   **Goal**: Move towards SVG generation for Hero images too, allowing you to edit the text inside the diagram after generation.
