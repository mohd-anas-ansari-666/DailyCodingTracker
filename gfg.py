import requests
from bs4 import BeautifulSoup

def get_gfg_solved(username):
    url = f"https://auth.geeksforgeeks.org/user/{username}/practice/"
    try:
        r = requests.get(url, timeout=10)  # 10-second timeout
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"⚠️ Could not fetch GFG stats: {e}")
        return 0  # return 0 if failed

    soup = BeautifulSoup(r.text, "lxml")
    solved_tag = soup.find("span", {"class": "score_card_value"})
    if solved_tag:
        return int(solved_tag.text.strip())
    return 0
