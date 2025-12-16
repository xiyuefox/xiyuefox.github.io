
import re
import os
import urllib.request
import ssl

target_file = "/Users/hulimofaqiu/Documents/obisidian笔记文件/math magic.md"

def diagnose_images(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all images
        urls = re.findall(r'!\[.*?\]\((https?://[^)]+)\)', content)
        
        print(f"🔍 Found {len(urls)} images.")
        
        if not urls:
            print("No images found to diagnose.")
            return

        # Check first 3
        for i, url in enumerate(urls[:3]):
            print(f"\nChecking Image {i+1}: {url}")
            try:
                # Create a request
                req = urllib.request.Request(url, method='HEAD')
                # Ignore SSL for diagnosis if needed, but python usually fine
                context = ssl.create_default_context()
                context.check_hostname = False
                context.verify_mode = ssl.CERT_NONE
                
                with urllib.request.urlopen(req, context=context, timeout=5) as response:
                    print(f"   ✅ Status: {response.status}")
                    print(f"   ✅ Content-Type: {response.headers.get('Content-Type')}")
            except urllib.error.HTTPError as e:
                print(f"   ❌ HTTP Error: {e.code} - {e.reason}")
            except Exception as e:
                print(f"   ❌ Network Error: {e}")

    except Exception as e:
        print(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    diagnose_images(target_file)
