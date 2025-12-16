
import sys
import json
import urllib.request
import subprocess
import os
import mimetypes

API_URL = "https://xixi-image-bed.jinxiyue07.workers.dev/upload"

def copy_to_clipboard(text):
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(text.encode('utf-8'))

def upload_image(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return

    print(f"📤 Uploading {os.path.basename(file_path)}...")
    
    # Simple multipart upload using urllib is verbose, but we can do a minimal version or use requests if available.
    # To keep it robust without knowing if 'requests' is installed, we'll try to use curl via subprocess.
    # It's cleaner on Mac than writing correct multipart/form-data logic in vanilla python.
    
    try:
        # curl -X POST -F "file=@path" URL
        result = subprocess.run(
            ["curl", "-s", "-X", "POST", "-F", f"file=@{file_path}", API_URL],
            capture_output=True,
            text=True
        )
        
        response = json.loads(result.stdout)
        
        if response.get('success'):
            url = response['url']
            filename = os.path.basename(file_path)
            # Create Markdown Link
            md_link = f"![{filename}]({url})"
            
            # Copy to clipboard
            copy_to_clipboard(md_link)
            
            print(f"✅ Success!")
            print(f"🔗 URL: {url}")
            print(f"📋 Copied to clipboard: {md_link}")
            return md_link
        else:
            print(f"❌ Upload Failed: {response.get('error', 'Unknown error')}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 upload_helper.py <path_to_image>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    upload_image(file_path)
