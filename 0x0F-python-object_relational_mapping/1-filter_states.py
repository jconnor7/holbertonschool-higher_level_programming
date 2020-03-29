#!/usr/bin/python3.4
"""
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute(" SELECT * FROM states\
    WHERE states.name LIKE 'N%'\
    ORDER BY states.id ASC")

    query_rows = cursor.fetchall()

    for state in query_rows:
        print(state)
    cursor.close()
    db.close()
