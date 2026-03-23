with open("scripts/fetch_hn_feed.py", "r") as f:
    lines = f.readlines()

with open("scripts/fetch_hn_feed.py", "w") as f:
    f.writelines(lines[:332])
