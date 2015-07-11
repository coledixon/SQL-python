import sqlite3

conn = sqlite3.connect('practice.db')
c = conn.cursor()

def CreateTable():
    c.execute("CREATE TABLE Film (FilmID INT PRIMARY KEY, Title VARCHAR(50) not null, Director VARCHAR(50) not null,"
              "Year INT) ")

def InsertData():
    c.execute("INSERT INTO Film VALUES(0001, 'Jurassic Park', 'Steven Spielberg', 1993)")
    c.execute("INSERT INTO Film VALUES(0002, '2001: A Space Odyssey', 'Stanley Kubrick', 1968)")
    c.execute("INSERT INTO Film VALUES(0003, 'The Day the Earth Stood Still', 'Robert Wise', 1951 )")
    c.execute("INSERT INTO Film VALUES(0004, 'There Will be Blood','Paul Thomas Anderson', 2007)")
    c.execute("INSERT INTO Film VALUES(0005, 'The Devils Brigade', 'Andrew V. McLaglen', 1968)")
    c.execute("INSERT INTO Film VALUES(0006, 'Brazil', 'Terry Gilliam', 1985)")
    c.execute("INSERT INTO Film VALUES(0007, 'The Life Aquatic with Steve Zissou','Wes Anderson', 2004)")
    conn.commit()

#CreateTable()
#InsertData()


