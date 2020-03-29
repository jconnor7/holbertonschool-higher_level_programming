#!/usr/bin/python3.4
""" Lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states\
    ON states.id = cities.state_id\
    ORDER BY cities.id ASC")

    query_rows = cursor.fetchall()

    for cities_states in query_rows:
        print(cities_states)

    cursor.close()
    db.close()
