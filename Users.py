import sqlite3

with sqlite3.connect("MathsPersonalDetails.db") as db:
    cursor=db.cursor()
##Names the database
cursor.execute("""
CREATE TABLE IF NOT EXISTS personalDetails(
userID INTEGER PRIMARY KEY,
StudentORTeacher text NOT NULL,
Surname text NOT NULL,
Forename text NOT NULL,
UserName text NOT NULL,
Password text NOT NULL);
""")
##Names the table in database
##Creates the column names and what data type they are
db.commit()
