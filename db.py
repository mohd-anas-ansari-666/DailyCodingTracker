import sqlite3
from datetime import date

DB_NAME = "stats.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS daily_stats (
            day TEXT PRIMARY KEY,
            lc_easy INTEGER,
            lc_medium INTEGER,
            lc_hard INTEGER,
            gfg_total INTEGER
        )
    """)

    conn.commit()
    conn.close()

def save_daily(day, easy, medium, hard, gfg):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        REPLACE INTO daily_stats VALUES (?, ?, ?, ?, ?)
    """, (day, easy, medium, hard, gfg))
    conn.commit()
    conn.close()

def get_previous_day(current_day):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    row = c.execute("""
        SELECT * FROM daily_stats
        WHERE day < ?
        ORDER BY day DESC LIMIT 1
    """, (current_day,)).fetchone()
    conn.close()
    return row

def get_all():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    rows = c.execute("SELECT * FROM daily_stats ORDER BY day").fetchall()
    conn.close()
    return rows
