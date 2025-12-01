from datetime import date
from leetcode import get_leetcode_difficulty_stats
from gfg import get_gfg_solved
from db import init_db, save_run, get_previous_run
import json, requests

config = json.load(open("config.json"))
LC_USER = config["leetcode_username"]
GFG_USER = config["gfg_username"]
BOT_TOKEN = config["telegram_bot_token"]
CHAT_ID = config["telegram_chat_id"]

def send_telegram(msg):
    if BOT_TOKEN and CHAT_ID:
        requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            params={"chat_id": CHAT_ID, "text": msg},
        )

def run():
    # Fetch stats
    lc_stats = get_leetcode_difficulty_stats(LC_USER)
    easy, medium, hard = lc_stats["Easy"], lc_stats["Medium"], lc_stats["Hard"]
    lc_total = easy + medium + hard

    gfg_total = get_gfg_solved(GFG_USER)
    # gfg_total = 0  # skip GFG to avoid timeout
    today_total = lc_total + gfg_total

    # Save this run
    save_run(easy, medium, hard, gfg_total)

    # Get previous run to calculate daily solved
    prev = get_previous_run()
    if prev:
        _, pe, pm, ph, pg = prev
        prev_total = pe + pm + ph + pg
    else:
        prev_total = today_total

    daily_solved = today_total - prev_total

    message = (
        f"📊 Daily Coding Report ({date.today().isoformat()})\n"
        f"LeetCode:\n"
        f"  Easy: {easy}\n"
        f"  Medium: {medium}\n"
        f"  Hard: {hard}\n"
        f"  Total: {lc_total}\n"
        f"\nGFG: {gfg_total}\n"
        f"\n🔥 Problems solved since last run: {daily_solved}"
    )

    print(message)
    send_telegram(message)

if __name__ == "__main__":
    init_db()
    run()
