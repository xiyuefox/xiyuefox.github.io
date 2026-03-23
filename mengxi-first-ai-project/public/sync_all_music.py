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

    # 写入 JSON
    json_path = os.path.join(DATA_DIR, "playlist.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(playlist, f, ensure_ascii=False, indent=2)

    print(f"✅ 同步完成！共 {len(playlist)} 首歌已备妥至 images/music/")
    print(f"✅ 数据保存在: {json_path}")

if __name__ == "__main__":
    main()
