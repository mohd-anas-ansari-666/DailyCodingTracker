import sqlite3
from datetime import date

DB_NAME = "stats.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS daily_stats (
            day TEXT PRIMARY KEY,
            lc_count INTEGER,
            gfg_count INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_daily(lc, gfg):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    today = date.today().isoformat()
    c.execute("REPLACE INTO daily_stats VALUES (?, ?, ?)", (today, lc, gfg))
    conn.commit()
    conn.close()

def get_all():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    rows = c.execute("SELECT * FROM daily_stats ORDER BY day").fetchall()
    conn.close()
    return rows
