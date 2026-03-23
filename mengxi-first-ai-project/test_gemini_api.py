import os
import requests

# Load env variables from .env
env_path = ".env"
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                try:
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value.replace('"', '').replace("'", "")
                except ValueError:
                    pass

api_key = os.environ.get("GEMINI_API_KEY")
print(f"API Key: {api_key[:5]}...")

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
try:
    res = requests.get(url, timeout=12)
    print(f"Status Code: {res.status_code}")
    if res.status_code == 200:
        data = res.json()
        for m in data.get('models', []):
            print(f"- {m['name']}")
    else:
         print(f"Response: {res.text}")
except Exception as e:
    print(f"Exception: {e}")
