import sqlite3

with sqlite3.connect("RevTime.db") as db:
    cursor=db.cursor()
##Names the database
cursor.execute("""
CREATE TABLE IF NOT EXISTS TimeTable(
Day text NOT NULL,
Quiz text);
""")
Days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
for i in range(0,7):
    insert=('INSERT INTO TimeTable(Day) VALUES(?)')
    cursor.execute(insert,[(Days[i])])
##Names the table in database
##Creates the column names and what data type they are
db.commit()



