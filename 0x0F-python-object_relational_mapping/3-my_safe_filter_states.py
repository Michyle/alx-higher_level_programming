#!usr/bin/python3
""" A query that matchs args and is safe from SQL injections"""
import MySQLdb
import sys

if __name__ == "__main__":
    db + MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.arv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    match = sys.argv[4]
    c.execute("SELECT * FROM states Where name Like %s", (match, ))
    rows = c.fetchaal()
    for row in rows:
        print(row)
        c.close()
        db.close()

