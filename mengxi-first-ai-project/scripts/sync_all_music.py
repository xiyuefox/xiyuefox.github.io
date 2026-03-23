import os
import glob
import subprocess
import json

SOURCE_PATH = "/Users/hulimofaqiu/Music/网易云音乐"
TARGET_DIR = "/Users/hulimofaqiu/mengxi-first-ai-project/images/music"
DATA_DIR = "/Users/hulimofaqiu/mengxi-first-ai-project/data"

os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

def main():
    print("🎵 开启自动化网易云音乐库同步引擎...")
    if not os.path.exists(SOURCE_PATH):
        print(f"❌ 找不到网易云 music 路径: {SOURCE_PATH}")
        return

    all_files = glob.glob(os.path.join(SOURCE_PATH, "*.*"))
    playlist = []

    for fpath in all_files:
        filename = os.path.basename(fpath)
        title_tag = filename.replace(".ncm", "").replace(".mp3", "")
        
        if filename.endswith(".ncm"):
            # 使用 ncmdump 解密到 images/music/
            try:
                subprocess.run(["ncmdump", fpath, "-o", TARGET_DIR], check=True)
                mp3_name = filename.replace(".ncm", ".mp3")
                playlist.append({"title": title_tag, "src": "/images/music/" + mp3_name})
            except Exception as e:
                print(f"⚠️ 解密失败 {filename}: {e}")
        elif filename.endswith(".mp3"):
            # 复制到 images/music/
            try:
                subprocess.run(["cp", fpath, os.path.join(TARGET_DIR, filename)], check=True)
                playlist.append({"title": title_tag, "src": "/images/music/" + filename})
            except Exception as e:
                print(f"⚠️ 拷贝失败 {filename}: {e}")

    # 排序自定义规则
    def get_sort_weight(item):
        title = item["title"].lower()
        # 1. Le chant de la mer 在首位
        if "le chant de la mer" in title and "nolwenn" in title:
            return 0
        # 2. Nolwenn的其余歌曲靠前
        elif "nolwenn" in title:
            return 1
        # 3. 程璧的歌曲在最后面 (数字越大约靠后)
        elif "程璧" in item["title"]:
            return 4
        # 4. 古琴放在程璧之前
        elif "古琴" in item["title"]:
            return 3
        # 5. 其他所有的夹在中间
        else:
            return 2

    playlist.sort(key=get_sort_weight)

    # 写入 JSON
    json_path = os.path.join(DATA_DIR, "playlist.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(playlist, f, ensure_ascii=False, indent=2)

    print(f"✅ 同步完成！共 {len(playlist)} 首歌已备妥至 images/music/")
    print(f"✅ 数据保存在: {json_path}")

if __name__ == "__main__":
    main()
