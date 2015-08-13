import sqlite3

connection = sqlite3.connect("Roster")

c = connection.cursor()

#c.execute("CREATE TABLE Beings(Name TEXT, Species TEXT, IQ INT)")

with sqlite3.connect("Roster") as connection:
    c.execute("INSERT INTO Beings VALUES('Korben Dallas', 'Meat Popsicle', 100)")
    c.execute("INSERT INTO Beings VALUES('Ak Not', 'Mangalore', -5)")
    c.execute("INSERT INTO Beings VALUES('Jean-Baptiste Zorg', 'Human', 122)")

c.execute("UPDATE Beings SET Species = 'Human' WHERE Name = 'Korben Dallas'")

def get_IQs():
    c.execute("SELECT Name, IQ FROM Beings WHERE Species = 'Human'")
    print (c.fetchall())
    connection.commit()

get_IQs()

def get_Beings():
    c.execute("SELECT * FROM Beings")
    print (c.fetchall())
    connection.commit()

get_Beings()
