import sqlite3
import time
import datetime

conn = sqlite3.connect('practice.db')
c = conn.cursor()

def CreateTable():
    c.execute("CREATE TABLE Tracking (ID INT PRIMARY KEY, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

IDdb = 0
IDdb +1
keyword = 'Dynamic Insert'
value = 0
value +1



def InsertData():

    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y/%m/%d %H:%M:%S'))
    c.execute("INSERT INTO Tracking VALUES(?,?,?,?,?)",
              (IDdb, time.time(), date, keyword, value))

    conn.commit()

#CreateTable()
InsertData()
