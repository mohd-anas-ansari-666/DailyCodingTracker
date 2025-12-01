import json
from leetcode import get_leetcode_stats
from gfg import get_gfg_stats
from db import init_db, save_daily
import requests

# Load config
config = json.load(open("config.json"))

LC_USER = config["leetcode_username"]
GFG_USER = config["gfg_username"]
BOT_TOKEN = config["telegram_bot_token"]
CHAT_ID = config["telegram_chat_id"]

def send_telegram(msg):
    if BOT_TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.get(url, params={"chat_id": CHAT_ID, "text": msg})

def run():
    print("Fetching LeetCode stats...")
    lc_count = get_leetcode_stats(LC_USER)

    print("Fetching GFG stats...")
    gfg_count = get_gfg_stats(GFG_USER)

    print("Saving to DB...")
    save_daily(lc_count, gfg_count)

    message = f"Daily Coding Stats:\nLeetCode: {lc_count}\nGFG: {gfg_count}"
    print(message)
    send_telegram(message)

if __name__ == "__main__":
    init_db()
    run()
