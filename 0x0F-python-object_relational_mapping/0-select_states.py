#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.excecute("SELECT * FROM sates ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in uery_rows:
        print(row)
    cur.close()
    db.close()
