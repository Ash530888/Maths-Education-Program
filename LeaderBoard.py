import sqlite3

with sqlite3.connect("LeaderBoard.db") as db:
    cursor=db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS board(
UserName text NOT NULL,
Score text NOT NULL);
""")

db.commit()
