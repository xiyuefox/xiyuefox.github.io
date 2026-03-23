import os
import random
import requests
import re
from datetime import datetime

# 🌟 经典治愈系绘本金句库
QUOTE_POOL = [
    {
        "book": "男孩、鼹鼠、狐狸和马",
        "book_en": "The Boy, the Mole, the Fox and the Horse",
        "en": "“What is the bravest thing you've ever said?” asked the boy. “Help,” said the horse.",
        "zh": "“你说的最勇敢的话是什么？”男孩问。“帮帮我。”马儿说。"
    },
    {
        "book": "男孩、鼹鼠、狐狸和马",
        "book_en": "The Boy, the Mole, the Fox and the Horse",
        "en": "“Asking for help isn't giving up,” said the horse. “It's refusing to give up.”",
        "zh": "“求救不是放弃，”马儿说。“它是拒绝放弃。”"
    },
    {
        "book": "猜猜我有多爱你",
        "book_en": "Guess How Much I Love You",
        "en": "“I love you right up to the moon—and back.”",
        "zh": "“我爱你一直到月亮那里，再从月亮上回到这里。”"
    },
    {
        "book": "猜猜我有多爱你",
        "book_en": "Guess How Much I Love You",
        "en": "“I love you as high as I can hop.”",
        "zh": "“我跳得有多高，就有多爱你。”"
    },
    {
        "book": "猜猜我有多爱你",
        "book_en": "Guess How Much I Love You",
        "en": "“I love you all the way down the lane as far as the river.”",
        "zh": "“我爱你，从这条小路一直到那边的河心。”"
    },
    {
        "book": "小王子",
        "book_en": "The Little Prince",
        "en": "“It is only with the heart that one can see rightly; what is essential is invisible to the eye.”",
        "zh": "“只有用心才能看得清。实质性的东西，用眼睛是看不见的。”"
    },
    {
        "book": "小王子",
        "book_en": "The Little Prince",
        "en": "“You become responsible, forever, for what you have tamed.”",
        "zh": "“你对你所驯养的一切，负有永远的责任。”"
    },
    {
        "book": "逃家小兔",
        "book_en": "The Runaway Bunny",
        "en": "“If you run away,” said his mother, “I will run after you. For you are my little bunny.”",
        "zh": "“如果你跑走了，”妈妈说，“我就跑去追你，因为你是我的小宝贝。”"
    },
    {
        "book": "我永远爱你",
        "book_en": "Love You Forever",
        "en": "“I’ll love you forever, I’ll like you for always, As long as I’m living, my baby you’ll be.”",
        "zh": "“我会永远爱你，我会永远疼你，只要我活着，你就是我的乖宝贝。”"
    },
    {
        "book": "爱心树",
        "book_en": "The Giving Tree",
        "en": "“Once there was a tree... and she loved a little boy.”",
        "zh": "“从前有一棵树……她非常爱一个小男孩。”"
    }
]

import json

# 缓存文件路径
CACHE_FILE = "/Users/hulimofaqiu/mengxi-first-ai-project/data/healing_quotes_cache.json"

def generate_healing_insight(quote):
    # 尝试读取缓存
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            cache = json.load(f)
            if quote['en'] in cache:
                return cache[quote['en']]
    else:
        cache = {}

    print(f"🔮 正在由 Gemini 生成对《{quote['book']}》的治愈解读...")
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "💡 温暖就在身边，静候宝宝的降临。"

    prompt = f"""
请扮演一位极其温柔、治愈的伴侣或心理抚慰师。
针对以下来自绘本《{quote['book']}》的经典语录，写一小段【针对孕晚期/待产妈妈】的治愈系解读与鼓励话语。
文字要求：
1. 极度温暖、治愈、轻缓，抚平焦虑。
2. 50-80字以内，读起来像热茶或拥抱。
3. 结尾加一句对妈妈和宝宝的祝福。

语录：
{quote['en']}
{quote['zh']}
"""
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        res = requests.post(url, json=payload, timeout=10)
        if res.status_code == 200:
            insight = res.json()['candidates'][0]['content']['parts'][0]['text'].strip()
            # 写入缓存
            if not os.path.exists(os.path.dirname(CACHE_FILE)):
                os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                current_cache = json.load(f) if os.path.exists(CACHE_FILE) else {}
            current_cache[quote['en']] = insight
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(current_cache, f, ensure_ascii=False, indent=4)
            return insight
    except Exception as e:
        print(f"⚠️ Gemini 治愈解读调用失败: {e}")
    return "💡 育儿路上，我们携手同行。愿你和宝宝平安喜乐。"

def main():
    print("💖 正在生成全量绘本治愈一言交互看板...")
    
    # 1. 补全所有 Insight（带缓存）
    final_data = []
    for item in QUOTE_POOL:
        item['insight'] = generate_healing_insight(item)
        final_data.append(item)

    # 2. 提取所有书本，去重
    books = list(dict.fromkeys([i['book'] for i in QUOTE_POOL]))
    select_html = '<label style="font-size: 0.82rem; color: var(--tg-text-light);">📚 切换绘本：</label><select id="healing-book-select" style="background: rgba(0,0,0,0.5); color: #fff; border: 1px solid rgba(255,255,255,0.2); border-radius: 4px; font-size: 0.82rem; padding: 2px 4px; cursor:pointer;">'
    select_html += '<option value="all">🎲 随机随机</option>'
    for b in books:
        select_html += f'<option value="{b}">{b}</option>'
    select_html += '</select>'

    # 2b. 提取背景音乐列表
    music_playlist_html = '<select id="ambient-music-playlist" style="font-size: 0.8rem; background: rgba(0,0,0,0.4); color: #FFD700; border: 1px solid rgba(255,215,0,0.2); border-radius: 4px; padding: 2px 4px; cursor: pointer; max-width: 140px; outline:none; text-overflow: ellipsis; white-space: nowrap; overflow: hidden;"><option value="">📻 随机播放治愈音声...</option>'
    playlist_path = "/Users/hulimofaqiu/mengxi-first-ai-project/data/playlist.json"
    music_list_json = "[]"
    if os.path.exists(playlist_path):
        try:
            with open(playlist_path, 'r', encoding='utf-8') as f:
                songs = json.load(f)
                music_list_json = json.dumps(songs, ensure_ascii=False)
                for s in songs:
                    title = s['title']
                    music_playlist_html += f'<option value="{s["src"]}">{title}</option>'
        except: pass
    music_playlist_html += '</select>'

    # 3. 拼装卡片 HTML 和前端 Script
    card_html = f"""
                    <div class="daily-healing-card" style="margin-top: 1.5rem; padding: 1.25rem; border: 1px solid rgba(255, 215, 0, 0.3); border-radius: 8px; background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(4px); box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                        <div style="font-family: var(--tg-font-sans); color: #FFD700; font-weight: 600; font-size: 0.9rem; margin-bottom: 0.75rem; display: flex; align-items: center; justify-content: space-between;">
                            <span>💖 每日一言 | 治愈系书摘内参</span>
                            <div>{select_html}</div>
                        </div>
                        <p id="healing-en" style="font-style: italic; font-size: 0.95rem; color: var(--tg-text-light); margin-bottom: 0.5rem; line-height: 1.5; font-family: Cambria, Georgia, serif;"></p>
                        <p id="healing-zh" style="font-size: 0.95rem; color: var(--tg-text-main); font-weight: 500; margin-bottom: 1rem;"></p>
                        <hr style="border: 0; border-top: 1px dashed rgba(255, 255, 255, 0.1); margin: 0.75rem 0;">
                        <p style="font-size: 0.88rem; color: var(--tg-text-light); line-height: 1.6; background: rgba(255,255,255,0.02); padding: 0.5rem 0.75rem; border-radius: 6px; border-left: 3px solid #FFD700;">
                            ✨ <strong>AI 温暖解读</strong>：<span id="healing-insight"></span>
                        </p>
                        <div style="text-align: right; color: var(--tg-text-muted); font-size: 0.8rem; font-style: italic; margin-top: 0.5rem;">
                            —— 📖 <span id="healing-source"></span>
                        </div>
                        
                        <!-- 🎵 治愈音声板块 -->
                        <div class="music-ambient-player" style="margin-top: 1.25rem; padding-top: 0.85rem; border-top: 1px solid rgba(255, 255, 255, 0.05); display: flex; flex-direction: column; gap: 8px;">
                            <div style="display: flex; align-items: center; justify-content: space-between; gap: 10px; flex-wrap: wrap;">
                                <div style="display: flex; flex-direction: column; gap: 3px; flex: 1; min-width: 160px;">
                                    <div style="font-size: 0.85rem; color: #f0f0f0; display: flex; align-items: center; gap: 6px;">
                                        🎵 <strong>治愈音声</strong> {music_playlist_html}
                                    </div>
                                    <div id="ambient-current-track" style="font-size: 0.72rem; color: var(--tg-text-light); opacity: 0.7; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; max-width: 220px;">
                                        🎬 治愈系列 · 自动加载网易云
                                    </div>
                                </div>
                                <div style="display: flex; align-items: center; gap: 8px;">
                                    <button id="custom-play-btn" style="background: rgba(255, 215, 0, 0.15); color: #FFD700; border: 1px solid rgba(255, 215, 0, 0.4); border-radius: 50%; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; cursor: pointer; font-size: 0.75rem; outline: none; transition: all 0.2s;" title="播放/暂停">▶</button>
                                    <audio id="ambient-audio" src="" preload="none" style="display: none;"></audio>
                                </div>
                            </div>
                        </div>
                    </div>

                    <script>
                        const healingQuotes = {json.dumps(final_data, ensure_ascii=False)};
                        const musicList = {music_list_json};

                        function updateHealingCard(bookFilter) {{
                            let pool = healingQuotes;
                            if (bookFilter !== 'all') {{
                                pool = healingQuotes.filter(q => q.book === bookFilter);
                            }}
                            const picked = pool[Math.floor(Math.random() * pool.length)];
                            document.getElementById('healing-en').innerText = picked.en;
                            document.getElementById('healing-zh').innerText = picked.zh;
                            document.getElementById('healing-insight').innerText = picked.insight;
                            document.getElementById('healing-source').innerText = `《${{picked.book}}》 (${{picked.book_en}})`;
                        }}

                        function setupAmbientAudio() {{
                            const selectNode = document.getElementById('ambient-music-playlist');
                            const audioNode = document.getElementById('ambient-audio');
                            const trackNode = document.getElementById('ambient-current-track');
                            const playBtn = document.getElementById('custom-play-btn');
                            if (!selectNode || !audioNode || !playBtn || !trackNode) return;

                            function togglePlay() {{
                                if (audioNode.paused) {{
                                    audioNode.play().catch(e => console.log('Auto-play prevented:', e));
                                }} else {{
                                    audioNode.pause();
                                }}
                            }}

                            playBtn.addEventListener('click', togglePlay);

                            // 绑定基础状态监听，确保按钮响应绝对正确
                            audioNode.addEventListener('playing', function() {{
                                playBtn.innerText = '⏸';
                            }});
                            
                            audioNode.addEventListener('pause', function() {{
                                playBtn.innerText = '▶';
                            }});

                            audioNode.addEventListener('ended', function() {{
                                playBtn.innerText = '▶';
                            }});

                            selectNode.addEventListener('change', function() {{
                                if (this.value) {{
                                    audioNode.src = this.value;
                                    audioNode.load();
                                    audioNode.play().catch(e => console.log('Auto-play prevented:', e));
                                    trackNode.innerText = `🎶 正在播放：` + selectNode.options[selectNode.selectedIndex].text;
                                }}
                            }});

                            if (musicList.length > 0) {{
                                const randomSong = musicList[Math.floor(Math.random() * musicList.length)];
                                for(let i=0; i<selectNode.options.length; i++) {{
                                    if (selectNode.options[i].value === randomSong.src) {{
                                        selectNode.selectedIndex = i;
                                        break;
                                    }}
                                }}
                                audioNode.src = randomSong.src;
                                audioNode.load();
                                trackNode.innerText = `🎲 随机：` + randomSong.title;
                            }}
                        }}

                        updateHealingCard('all');
                        setupAmbientAudio();

                        document.getElementById('healing-book-select').addEventListener('change', function() {{
                            updateHealingCard(this.value);
                        }});
                    </script>
"""

    index_path = "/Users/hulimofaqiu/mengxi-first-ai-project/index.html"
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()

        welcome_text_pattern = r'(<div class="tg-welcome-text">[\s\S]*?</div>)'
        matches = re.findall(welcome_text_pattern, content)

        if matches:
            matched_div = matches[0]
            if "<!-- HEALING_QUOTE_START -->" in content:
                print("♻️ 发现已有治愈一言锚点，正在更新交互面板...")
                replace_pattern = r'<!-- HEALING_QUOTE_START -->[\s\S]*?<!-- HEALING_QUOTE_END -->'
                content = re.sub(replace_pattern, "<!-- HEALING_QUOTE_START -->\n" + card_html + "\n<!-- HEALING_QUOTE_END -->", content)
            elif "daily-healing-card" in content:
                print("♻️ 发现已有旧版治愈一言，正在更新交互面板...")
                replace_pattern = r'(<div class="daily-healing-card"[\s\S]*?</script>\s*</div>)'
                content = re.sub(replace_pattern, card_html + "</div>", content)
            else:
                print("🆕 注入全量治愈一言交互看板...")
                new_matched_div = matched_div[:-6] + card_html + "</div>"
                content = content.replace(matched_div, new_matched_div)

            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("✅ 治愈一言交互面板已静态打入主页 ！！！")
        else:
            print("⚠️ 未能在 index.html 匹配到 <div class='tg-welcome-text'>")

if __name__ == "__main__":
    main()
