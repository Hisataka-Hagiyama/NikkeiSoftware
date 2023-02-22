import sqlite3

conn = sqlite3.connect('memo.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE daily(
    date TEXT PRIMARY KEY,
    memo TEXT NOT NULL)""")

conn.commit()

conn.close()
