import sqlite3

with sqlite3.connect("Homework.db") as db:
    cursor=db.cursor()
##Names the database
cursor.execute("""
CREATE TABLE IF NOT EXISTS HW(
Username text NOT NULL,
Quiz text NOT NULL,
State text NOT NULL);
""")

##Names the table in database
##Creates the column names and what data type they are
db.commit()
