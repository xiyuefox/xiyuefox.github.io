import os
import requests
import re
import json

# 📅 孕晚期 35周+ 科学作息时间线原胚
BASE_SCHEDULE = [
    {
        "time": "08:00 - 09:00",
        "title": "☀️ 晨间唤醒 & 开启元气",
        "action": "测量胎动、体重、心率。温水洗漱后享用高蛋白早餐（全麦、鸡蛋、牛奶）。",
        "suggested": "08:00 起床唤醒 | 08:10 享用早餐",
        "dxy_tip": "起卧时动作要缓慢，防水肿带来的腿脚麻木；左侧卧起坐最安全。",
        "xhs_tip": "早餐前喝一杯温水，对孕晚期的肠道蠕动非常友好，顺便记录 Obsidian 晨间日志。"
    },
    {
        "time": "09:00 - 11:30",
        "title": "⏳ 黄金专注期（大段时间）",
        "action": "轻度居家办公/学习、阅读 Obsidian 育儿笔记，整理新生儿房间布置或大件清单。",
        "suggested": "09:15 专注工作/学习 | 10:30 起身拉伸",
        "dxy_tip": "每坐 40 分钟必须起身活动 5 分钟，散步或做简单的拉伸，缓解下肢水肿。",
        "hn_tip": "这时候思路最清晰，适合看看 Hacker News 极客自动化极速情报，或者做极客 DIY 极客方案。"
    },
    {
        "time": "12:00 - 14:00",
        "title": "🍲 营养午餐 & 充电小憩",
        "action": "补充绿叶菜、红肉（补铁）。饭后 30 分钟不宜坐靠，慢走后进行 30~60 分钟左侧卧午休。",
        "suggested": "12:00 营养午餐 | 13:00 慢步消食 & 午休",
        "dxy_tip": "午休时腿下可以垫一个软枕头，比心脏略高，能极大程度消退下蹲水肿。",
        "xhs_tip": "午睡前可以刷一会儿小红书待产包，但不要超过 15 分钟防止大脑过度兴奋。"
    },
    {
        "time": "14:30 - 17:30",
        "title": "⏳ 柔和舒缓期（大段时间）",
        "action": "孕妇瑜伽、盆底肌锻炼（凯格尔运动）、待产包避坑清点。听听古典音乐进行胎教。",
        "suggested": "15:00 瑜伽/凯格尔 | 16:00 音频胎教",
        "dxy_tip": "凯格尔运动可以锻炼产道肌肉，为顺产蓄力；如果有宫缩感，立刻停止休息。",
        "xhs_tip": "孕晚期容易饿，下午可以加餐坚果、低糖水果（如奇异果、圣女果）。"
    },
    {
        "time": "18:00 - 20:30",
        "title": "🌆 晚间温馨 & 户外散步",
        "action": "清淡晚餐。饭后由伴侣陪同，在公园或安全路段慢步 30~45 分钟。",
        "suggested": "18:00 清淡晚餐 | 19:30 伴侣慢步散步",
        "dxy_tip": "散步是最好的助产运动，穿软底防滑鞋，有规律的胎动往往在此时出现。",
        "hn_tip": "在散步时可以跟伴侣聊聊树莓派智能看护 DIY 的实现，家庭极客时光段。"
    },
    {
        "time": "21:00 - 22:30",
        "title": "🌌 夜间沉淀 & 舒眠准备",
        "action": "温水泡脚缓解水肿，远离蓝光屏幕。听听治愈一言，回顾一天的美好，22:30 准时就寝。",
        "suggested": "21:30 温水泡脚 | 22:15 离线日记 | 22:30 就寝",
        "dxy_tip": "睡前少喝水，左侧卧睡眠为主。可以用专门的孕妇枕支撑腹部 and 腿部。",
        "xhs_tip": "在 Obsidian 离线写下给宝宝的 Time Travel 悄悄话，带着爱意入睡。"
    }
]

def generate_interactive_card():
    import datetime

    # 🎯 设定锚点日期
    TARGET_DATE = datetime.date(2026, 4, 15)
    # 获取脚本运行时的系统当前日期
    CURRENT_DATE = datetime.date.today()

    # 计算分支 A（未到破壳日）或 B 分支（已到/超过破壳日）
    if CURRENT_DATE < TARGET_DATE:
        remaining_days = (TARGET_DATE - CURRENT_DATE).days
        # 推算精准孕周 (以 280 天为总孕期)
        days_pregnant = 280 - remaining_days
        current_week = days_pregnant // 7
        
        timeline_header = f"""
  <p style="margin: 0; line-height: 1.8;">T-MINUS · <span style="color: #000; font-weight: 500;">{remaining_days} DAYS</span></p>
  <p style="margin: 0; line-height: 1.8; font-size: 11px; text-transform: uppercase;">EXPECTING YU JI · WEEK {current_week}</p>
"""
    else:
        days_born = (CURRENT_DATE - TARGET_DATE).days
        timeline_header = f"""
  <p style="margin: 0; line-height: 1.8;">YU JI · <span style="color: #000; font-weight: 500;">DAY {days_born + 1}</span></p>
  <p style="margin: 0; line-height: 1.8; font-size: 11px; text-transform: uppercase;">HELLO WORLD</p>
"""

    # Poche 风格级极简日常事项清单
    schedule_html = ""
    for s in BASE_SCHEDULE:
        tips = []
        if 'dxy_tip' in s: tips.append(f'<span style="color: #888;">🛡️ 丁香妈妈: {s["dxy_tip"]}</span>')
        if 'hn_tip' in s: tips.append(f'<span style="color: #888;">💡 极客参考: {s["hn_tip"]}</span>')
        if 'xhs_tip' in s: tips.append(f'<span style="color: #888;">💖 小红书: {s["xhs_tip"]}</span>')
        
        tips_html = "<br> ".join(tips)
        if tips_html:
            tips_html = f'<div style="margin-top: 0.25rem; font-size: 11px; line-height: 1.6;">{tips_html}</div>'

        suggested_html = ""
        if 'suggested' in s:
            suggested_html = f'<p style="margin: 0.2rem 0; font-size: 11px; color: #444; font-family: ui-monospace, monospace; border-bottom: 1px dotted #fafafa; padding-bottom: 2px;">⏰ 建议 · {s["suggested"]}</p>'

        schedule_html += f"""
    <div style="margin-top: 1rem;">
      <p style="margin: 0; line-height: 1.6; color: #000; font-weight: 500;">[{s['time']}] · {s['title']}</p>
      {suggested_html}
      <p style="margin: 0.2rem 0 0.5rem 0; line-height: 1.6; color: #555; font-size: 12px;">{s['action']}</p>
      {tips_html}
    </div>
"""

    full_html = f"""
<div class="poche-timeline" style="margin: 2rem 0; font-family: ui-monospace, monospace; font-size: 13px; color: #666; letter-spacing: 0.05em; border-left: 1px solid #eaeaea; padding-left: 1rem;">
  {timeline_header}
  
  <p style="margin: 1.5rem 0 0.5rem 0; font-weight: 600; color: #000; font-size: 11px; text-transform: uppercase; border-bottom: 1px dotted #eaeaea; padding-bottom: 0.25rem; display: inline-block;">DAILY SCHEDULE</p>
  {schedule_html}
</div>
"""
    return full_html
    return full_html

def main():
    print("📅 正在生成孕晚期 35周+ 科学作息时间卡片...")
    card_html = generate_interactive_card()

    index_path = "/Users/hulimofaqiu/mengxi-first-ai-project/index.html"
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()

        welcome_text_pattern = r'(<div class="tg-welcome-text">[\s\S]*?</div>)'
        matches = re.findall(welcome_text_pattern, content)

        if matches:
            matched_div = matches[0]
            # 🎯 如果已经存在 daily-schedule-card，则先替换掉旧的
            if "<!-- SCHEDULE_START -->" in content:
                print("♻️ 发现已有日课表锚点，正在更新...")
                replace_pattern = r'<!-- SCHEDULE_START -->[\s\S]*?<!-- SCHEDULE_END -->'
                content = re.sub(replace_pattern, "<!-- SCHEDULE_START -->\n" + card_html + "\n<!-- SCHEDULE_END -->", content)
            elif "daily-schedule-card" in content:
                print("♻️ 发现已有旧版日课表，正在更新...")
                replace_pattern = r'(<div class="daily-schedule-card"[\s\S]*?</div>\s*</div>)'
                content = re.sub(replace_pattern, card_html + "</div>", content)
            else:
                print("🆕 注入全新作息时间看板...")
                new_matched_div = matched_div[:-6] + card_html + "</div>"
                content = content.replace(matched_div, new_matched_div)

            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("✅ 孕晚期作息卡片已打入主页 top header ！！！")
        else:
            print("⚠️ 未能在 index.html 匹配到 <div class='tg-welcome-text'>")

if __name__ == "__main__":
    main()
