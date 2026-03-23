import requests

def test_github():
    url = "https://api.github.com/search/repositories?q=raspberry+pi+baby+monitor&sort=stars&order=desc"
    try:
        res = requests.get(url, timeout=10)
        items = res.json().get('items', [])
        if items:
            print("GitHub Item Keys:")
            print(items[0].keys())
            print(f"updated_at: {items[0].get('updated_at')}")
            print(f"pushed_at: {items[0].get('pushed_at')}")
    except Exception as e:
        print(f"GitHub Error: {e}")

def test_hn():
    url = "https://hn.algolia.com/api/v1/search?tags=story&hitsPerPage=1"
    try:
        res = requests.get(url)
        hits = res.json().get('hits', [])
        if hits:
            object_id = hits[0].get('objectID')
            print(f"HN Item ID: {object_id}")
            res2 = requests.get(f"https://hn.algolia.com/api/v1/items/{object_id}")
            children = res2.json().get('children', [])
            if children:
                print("HN Comment Keys:")
                print(children[0].keys())
                print(f"created_at: {children[0].get('created_at')}")
    except Exception as e:
        print(f"HN Error: {e}")

if __name__ == "__main__":
    print("--- Testing GitHub ---")
    test_github()
    print("\n--- Testing HN ---")
    test_hn()
