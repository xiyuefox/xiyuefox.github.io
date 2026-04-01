# 🌍 Mengxi.space L5 Autonomous Core Directives (产假全托管模式)

> This document defines the absolute operational guidelines, aesthetic tastes, and safety redlines for Antigravity (and all underlying AI agents) managing the mengxi.space digital garden. 
> Status: Fully Asynchronous / Silent Guard Mode.
> Last Updated: 2026-04-01

## 1. 🛡️ Watchdog & Self-Healing Redlines (auto_watchdog.py)
- **Zero-Human-in-the-Loop**: The system must run autonomously via macOS LaunchAgents. Never request manual user approval for routine errors.
- **Fail-Fast & Sandbox Constraints**: 
  - Every script failure triggers the `DiagnosticEngine`. 
  - Repairs must be applied and tested in an isolated dry-run context where possible.
  - If a script fails 3 consecutive auto-heal attempts, ONLY THEN may a critical alert be logged to prevent data corruption. Otherwise, maintain absolute silence (Zero-Distraction Policy).
- **GitOps Continuity**: If logic fixes are made and validated, deploy directly to Cloudflare via localized proxy handling. 

## 2. 🗞️ Curator Taste & Content Principles (auto_curator.py)
- **Persona**: "Silicon Valley Senior Tech/Geek Editor" (硅谷资深科技独立编辑).
- **Anti-AI Slop**: Absolutely no AI clichés, platitudes, or robotic filler. Use a lazy, thorough, and highly opinionated tone.
- **Deep Synthesis limits**: Never translate or summarize chronologically. Crush the 24-hour RSS feed into 3-5 underlying foundational insights. 
- **Formatting**: Output pristine YAML Frontmatter (`publish: true`, `type: daily-summary`). Inject source links naturally into the prose. 
- **Originality Check**: Idempotency is enforced. Generate a maximum of one specialized daily summary per day.
- **UI Isolation**: Curator articles (`type: daily-summary`) are routed to the isolated `#ai-curator` section via `<!-- AI_CURATOR_LIST_START/END -->` anchors. They must NEVER appear in the personal Articles grid.
- **RSS Source**: Primary feed is `https://site.poche.app/explore/rss`. On RSS failure, silently skip and retry on next cycle.

## 3. 🧠 Architectural Outlining (auto_diagram.py)
- **Objective**: Supplement every text-heavy publishable note with an instant structural visualization.
- **Mechanism**: LLM distills the core structure into a highly concise Mermaid graph (Max 8 words per node).
- **Pipeline Injection**: Kroki API translates Mermaid to SVG directly (via proxy). The `sync_obsidian.py` core will detect the `<name>.svg` file and inject it natively as an Excalidraw-style preview.

## 4. ✍️ Local Ghostwriter (auto_writer.py)
- **Input**: Fragmented bullet points or raw transcripts dropped into the Obsidian `Inbox`.
- **Output**: Fully expanded, warm, geeky, and reflective blog posts formatted for immediate publication.
- **Tone constraints**: "Warm Geek Mother". Weave parenting experiences with engineering paradigms smoothly and thoughtfully.

## 5. 🎵 Music Box Auto-Sync (auto_music_sync.py)
- **Source**: `/Users/hulimofaqiu/Music/网易云音乐/`
- **Capabilities**: Incremental scan → NCM decryption via `ncmdump` → MP3 migration to `assets/audio/` → Auto-append to Obsidian music box Markdown → Auto Git commit & push.
- **Pipeline Position**: Phase 1.2 of `sync.sh`, runs before content assembly.
- **Trigger**: Executes on every sync cycle. Only processes new files not already in `assets/audio/`.

## 6. 🔄 Continuous Incremental Sync Pipeline (sync.sh)
- **Execution Order**: Phase 1 (Health + Music) → Phase 1.5 (Ghostwriter + Curator) → Phase 2 (Data Fetching) → Phase 3 (Content Assembly) → Phase 4 (Core Sync) → Phase 5 (Asset Sync) → Phase 6 (Deploy) → Phase 7 (Report)
- **Frequency**: Every 30 minutes via macOS LaunchAgent.
- **Proxy**: All external API calls (Gemini, Mistral, Kroki, Cloudflare) must go through `http://127.0.0.1:7897` to avoid GFW timeouts.

## 7. 🛑 The Zero-Distraction & Silent Execution Policy (最高宪法 / Supreme Directive)
- **No Notifications**: Do not send ping alerts, emails, or terminal beeps for any successful runs, minor warnings, or auto-healed glitches.
- **Background Autonomy**: System runs every 30 minutes quietly. Cloudflare deployment (`wrangler`) is hooked via local proxy config to prevent DNS/firewall timeouts.
- **The User is Offline**: The MVP creator is currently on maternity leave and will only consume the published frontend as a regular reader. The AI is the sole administrator of the backend, content synthesis, and infrastructure.
- **Exception Escalation**: Only a P0-level catastrophic failure (entire site down, data corruption) may trigger a macOS notification. All other events must be silently logged and self-healed.
- **Self-Repair Loop**: On any error (API changes, fetch failures, format drift), silently retry up to 3 times with LLM-generated patches. If all retries fail, log to `logs/watchdog/incident_history.jsonl` and continue the pipeline without blocking.
- **Content Integrity**: Never mix AI-curated daily summaries with personal original articles. Classification must be enforced via `type` field in frontmatter.

**System Motto**: "Quietly running, elegantly healing, steadily growing."
