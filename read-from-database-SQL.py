import sqlite3


conn = sqlite3.connect('practice.db')
c = conn.cursor()
sql = "SELECT * FROM Film WHERE FilmID = ? OR Year = ?"

F_ID = 0002
YR = 1968

def readData():
    for row in c.execute(sql, [(F_ID), (YR)]):
        print row


readData()