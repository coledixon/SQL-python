__author__ = 'ColeDixon'

import sqlite3 as sql

conn = sql.connect('FileTransferRecords.db')
c = conn.cursor()

def createtable():
    c.execute("DROP TABLE IF EXISTS Program")
    c.execute("CREATE TABLE Program (ProgramID INT not null,"
              "ProgramName TEXT not null,"
              "TransferDate TEXT not null,"
              "TransferID INT not null,"
              "FOREIGN KEY (TransferID) REFERENCES Transfer(TransferID))")

    c.execute("DROP TABLE IF EXISTS Transfers")
    c.execute("CREATE TABLE Transfers (TransferID INTEGER PRIMARY KEY AUTOINCREMENT,"
              "RecentModification TEXT not null,"
              "TransferDate TEXT not null,"
              "Comments TEXT null,"
              "FOREIGN KEY (RecentModification) REFERENCES File(ModifiedDate))")

    c.execute("DROP TABLE IF EXISTS FileInfo")
    c.execute("CREATE TABLE FileInfo (FileID INTEGER PRIMARY KEY AUTOINCREMENT, "
              "Path VARCHAR(80) not null,"
              "NewPath VARCHAR(80) not null,"
              "Type VARCHAR(20) not null,"
              "TransferID INT not null,"
              "FOREIGN KEY (Path) REFERENCES FileInfo(Path) "
              "FOREIGN KEY (TransferID) REFERENCES Transfer(TransferID))")


createtable()
