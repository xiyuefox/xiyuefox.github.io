#!/usr/bin/env python3
import os
import shutil
import subprocess

SOURCE_DIR = "/Users/hulimofaqiu/Music/网易云音乐"
PROJECT_DIR = "/Users/hulimofaqiu/mengxi-first-ai-project"
TARGET_DIR = os.path.join(PROJECT_DIR, "assets", "audio")
MD_FILE = "/Users/hulimofaqiu/Documents/obisidian笔记文件/articles/2026-04-01-宝宝的数字音乐盒.md"

def main():
    print("🎵 开始增量同步宝宝数字音乐盒资产...")
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    if not os.path.exists(SOURCE_DIR):
        print(f"⚠️ 源目录不存在: {SOURCE_DIR}")
        return

    new_songs = []
    
    # 获取目标目录中已存在的文件（用于比对）
    existing_files = set(os.listdir(TARGET_DIR))

    for filename in os.listdir(SOURCE_DIR):
        filepath = os.path.join(SOURCE_DIR, filename)
        if not os.path.isfile(filepath):
            continue
            
        basename, ext = os.path.splitext(filename)
        ext = ext.lower()
        
        target_mp3 = f"{basename}.mp3"
        
        if ext == '.ncm':
            # 如果对应的 mp3 还不目标目录里，说明是新增的 ncm
            if target_mp3 not in existing_files:
                print(f"🔓 发现新增加密文件，正在解密: {filename}")
                try:
                    subprocess.run(["ncmdump", filepath], check=True, capture_output=True)
                    # ncmdump 默认会在同目录生成同名的 .mp3
                    source_mp3 = os.path.join(SOURCE_DIR, target_mp3)
                    if os.path.exists(source_mp3):
                        shutil.copy2(source_mp3, os.path.join(TARGET_DIR, target_mp3))
                        new_songs.append(target_mp3)
                        existing_files.add(target_mp3)
                        print(f"✅ 解密并迁移成功: {target_mp3}")
                    else:
                        print(f"❌ 解密失败或找不到生成的mp3: {filepath}")
                except Exception as e:
                    print(f"❌ ncmdump 执行失败: {e}")
                    
        elif ext == '.mp3':
            # 如果是原生的 mp3
            if filename not in existing_files:
                print(f"📦 发现新增普通音频，正在迁移: {filename}")
                shutil.copy2(filepath, os.path.join(TARGET_DIR, filename))
                new_songs.append(filename)
                existing_files.add(filename)
                print(f"✅ 迁移成功: {filename}")

    if new_songs:
        print(f"📝 发现 {len(new_songs)} 首新歌，正在写入数字花园...")
        if os.path.exists(MD_FILE):
            with open(MD_FILE, 'r', encoding='utf-8') as f:
                content = f.read()
                
            append_text = ""
            for song in new_songs:
                md_link = f"![[{song}]]"
                if md_link not in content:
                    append_text += f"\n{md_link}"
                    
            if append_text:
                with open(MD_FILE, 'a', encoding='utf-8') as f:
                    f.write(append_text)
                print("✅ Markdown 更新成功。")
        else:
            print(f"⚠️ 找不到 Markdown 文件: {MD_FILE}，跳过写入。")

        print("🚀 触发静默发布 (Git Commit & Push)...")
        try:
            # Add changes
            subprocess.run(["git", "add", "assets/audio/"], cwd=PROJECT_DIR, check=True)
            # If the Obsidian vault is in the same repo, this adds the md file. If not, it just tracks assets.
            # In mengxi.space context, we might also want to commit all just in case.
            subprocess.run(["git", "add", "."], cwd=PROJECT_DIR, check=True)
            subprocess.run(["git", "commit", "-m", "auto-update: added new baby songs"], cwd=PROJECT_DIR, check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=PROJECT_DIR, check=True)
            print("✅ Git 提交流水线完成！")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ Git 提交或推送失败: {e}")
            
    else:
        print("💡 没有发现新的音乐文件，跳过更新。")

if __name__ == "__main__":
    main()
