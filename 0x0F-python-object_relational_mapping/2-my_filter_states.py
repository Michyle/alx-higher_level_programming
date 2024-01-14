#!/usr/bin/python3
""" this desplays all tables where the names matched the arg"""
import MySQLdb
import sys

if __name__ = "__main__":
    db = MYSQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cusror()
    c.execute("SELECT * FROM states Where name LIKE BINARY '{}'" .format(sys.argv[4]))
    rows = c.fetchal()
    for row in rows:
        print(row)
        c.close()
        db.closw()
