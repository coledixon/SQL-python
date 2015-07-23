__author__ = 'ColeDixon'

import sqlite3 as sql
import time as t

class Flaskr_db:
    def __init__(self):
        self.db_connection()
        self.createTable()
        self.insertUsers()

    def db_connection(self):
        self.conn = sql.connect('flaskr.db')
        self.c = self.conn.cursor()

    def createTable(self):
        self.c.execute("DROP TABLE IF EXISTS entries")
        self.c.execute("DROP TABLE IF EXISTS users")
        self.c.execute("CREATE TABLE users ("
                       "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "username TEXT not null,"
                       "password not null)")

        self.c.execute("DROP TABLE IF EXISTS info")
        self.c.execute("CREATE TABLE info ("
                       "id INTEGER PRIMARY KEY,"
                       "email TEXT not null,"
                       "phone TEXT not null,"
                       "FOREIGN KEY (id) REFERENCES users(id))")

    def insertUsers(self):
        print('ENTER NEW USERNAME and PASSWORD')
        t.sleep(0.7)
        self.user = raw_input('INPUT USERNAME: ')
        self.pass_ = raw_input('INPUT PASSWORD: ')
        self.c.execute("INSERT INTO users (username, password) VALUES(?,?);",
                       (self.user, self.pass_))
        self.conn.commit()
        t.sleep(0.5)
        print('\tUSERNAME and PASSWORD SUCCESSFULLY ADDED')
        t.sleep(1)
        add = raw_input('Would you like to add another user? Y/N ')

        if add == 'Y':
            self.insertUsers()
        elif add == 'N':
            add2 = raw_input('Would you like to add an EMAIL and PHONE NUMBER? Y/N ')
            if add2 == 'Y':
                self.insertInfo()
            else:
                print('GOODBYE!')

    def insertInfo(self):
        print('ENTER EMAIL and PHONE NUMBER')
        t.sleep(0.7)
        self.email = raw_input('ENTER EMAIL: ')
        self.phone = raw_input('ENTER PHONE: ')
        self.c.execute("INSERT INTO info (email, phone) VALUES(?,?)",
                       (self.email, self.phone))
        self.conn.commit()
        t.sleep(0.5)
        print('\tEMAIL and PHONE NUMBER SUCCESSFULLY ADDED')
        t.sleep(1)

        new = raw_input('Would you like to add another user? Y/N ')

        if new == 'Y':
            self.insertInfo()
        elif new == 'N':
            print('GOODBYE')

def main():
    Flaskr_db()

if __name__ == "__main__": main()
