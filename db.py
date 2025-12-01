import sqlite3
from datetime import datetime, date

DB_NAME = "stats.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            run_time TEXT PRIMARY KEY,
            lc_easy INTEGER,
            lc_medium INTEGER,
            lc_hard INTEGER,
            gfg_total INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_run(lc_easy, lc_medium, lc_hard, gfg_total):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    now = datetime.now().isoformat(timespec='seconds')
    c.execute("""
        INSERT OR REPLACE INTO runs VALUES (?, ?, ?, ?, ?)
    """, (now, lc_easy, lc_medium, lc_hard, gfg_total))
    conn.commit()
    conn.close()

def get_previous_run():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    row = c.execute("""
        SELECT * FROM runs
        ORDER BY run_time DESC
        LIMIT 2
    """).fetchall()
    conn.close()
    if len(row) < 2:
        return None
    return row[1]  # second latest run = previous run
