import requests
from bs4 import BeautifulSoup

def get_gfg_solved(username):
    url = f"https://auth.geeksforgeeks.org/user/{username}/practice/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    solved_tag = soup.find("span", {"class": "score_card_value"})
    if solved_tag:
        return int(solved_tag.text.strip())
    return 0
