#!/usr/bin/python3
"""Lists states matching a given name"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    db_connection = MySQLdb.connect(user=username, passwd=password,
                                    db=database_name, host='localhost',
                                    port=3306)

    cursor = db_connection.cursor()
    query = """SELECT cities.id, cities.name, states.name
                    FROM cities INNER JOIN states
                    ON cities.state_id = states.id"""
    cursor.execute(query)
    matching_states = cursor.fetchall()

    for row in matching_states:
        print(row)

    db_connection.close()
