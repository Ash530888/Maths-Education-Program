import sqlite3

with sqlite3.connect("Scores.db") as db:
    cursor=db.cursor()
##Names the database
cursor.execute("""
CREATE TABLE IF NOT EXISTS ScoreTable(
UserName text NOT NULL,
Score INTEGER);
""")
##Names the table in database
##Creates the column names and what data type they are
db.commit()




