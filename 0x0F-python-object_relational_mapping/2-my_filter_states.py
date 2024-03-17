#!/usr/bin/python3
"""Lists states starting with 'N'"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    search_name = argv[4]

    db_connection = MySQLdb.connect(user=username, passwd=password,
                                    db=database_name, host='localhost',
                                    port=3306)

    cursor = db_connection.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
    cursor.execute(query, (search_name,))
    n_starting_states = cursor.fetchall()

    for row in n_starting_states:
        print(row)

    cursor.close()
    db_connection.close()
