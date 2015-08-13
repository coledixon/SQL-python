import sqlite3
import sys, traceback

conn = sqlite3.connect('test.db')

def newFriend():
    print("\nADD A FRIEND")

    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    location = input("Location: ")

    val_str = "'{}', '{}', '{}', '{}'".format(\
    name, age, gender, location)
    print(val_str)

    sql_str = "INSERT INTO Friend_Info\
(NAME, AGE, GENDER, LOCATION) VALUES\
({});".format(val_str)
    print(sql_str)

    conn.execute(sql_str)
    conn.commit()
    print("Number of changes: ", conn.total_changes)


def viewAll():
    sql_str = "SELECT * FROM Friend_Info"
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    print(rows)

def viewDetails():
    print("SEARCH FOR A FRIEND")
    name = input("Enter friend's name: ")
    print(name)
    sql_str = "SELECT * FROM Friend_info WHERE \
Name = '{}'".format(name)
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    printData(rows)
    if len(rows) == 0:
        print("NO RECORDS FOUND")
    else:
        printData(rows)
    

def printData(data):
    for row in data:
        print("ID: ", row[0])
        print("NAME: ", row[1])
        print("AGE: ", row[2])
        print("GENDER: ", row[3])
        print("LOCATION: ", row[4], "\n")


def deleteFriend():
    print("DELETE A FRIEND")
    name = input("Enter friend's name: ")
    sql_str = "SELECT * FROM Friend_Info WHERE NAME = '{}'"\
              .format(name)
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    change_id = 0
    if len(rows) == 0:
        print("NO RECORDS FOUND")
        return
    elif len(rows) == 1:
        print("ONE RECORD FOUND")
        row = rows[0]
        change_id = row[0]
        printData(rows)
    else:
        printData(rows)
        change_id = input("Enter friend ID to update: ")
        print(change_id)
    delete = input("Confirm delete: Y/N ")
    if delete == "Y":
        sql_str = "DELETE FROM Friend_Info WHERE ID = '{}'"\
                  .format(change_id)
        conn.execute(sql_str)
        conn.commit()
        print("Number of changes: ", conn.total_changes)

def printData(data):
    for row in data:
        print("ID: ", row[0])
        print("NAME: ", row[1])
        print("AGE: ", row[2])
        print("GENDER: ", row[3])
        print("LOCATION: ", row[4], "\n")

def options():
    print("\nWhat would you like to do?")
    print("1: Add a new friend")
    print("2: View all friends")
    print("3: Search for a friend")
    print("4: Update a friend")
    print("5: Delete a friend")
    print("6: EXIT")

    response = input("ENTER A NUMBER: ")

    if response == '1':
        newFriend()
    elif response == '2':
        viewAll()
    elif response == '3':
        viewDetails()
    elif response == '4':
        print('NO UPDATE FEATURE AT THIS TIME')
    elif response == '5':
        deleteFriend()
    else:
        print("EXITING PROGRAM")
        return

def mainloop():
    in_loop = True
    while in_loop == True:
        options()
        again = input('Continue?  y/n ')
    if again != 'y':
        in_loop = False
        
    
options()
mainloop()
