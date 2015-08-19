import sqlite3


def GetFileTransferDate():

    db = sqlite3.connect('A_to_B.db')
    cursor = db.execute("SELECT transfer_timestamp FROM file_transfer_info ORDER BY ID DESC")
    row = cursor.fetchone()
    print(row)
    ts = '%s' % row
    db.close()
    return ts
    
def UpdateFileTransferDate(dt_time):
    #print 'in update utility - time is ', dt_time

    db = sqlite3.connect('A_to_B.db')
    sql = "UPDATE file_transfer_info SET transfer_timestamp = '%s'" % dt_time
    print( sql)
    db.execute(sql)
    db.commit()
    db.close()
    
#GetFileTransferDate()
#UpdateFileTransferDate()





        
        
