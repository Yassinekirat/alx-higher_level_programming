#!/usr/bin/python3
"""Lists cities of a given state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    db_connection = MySQLdb.connect(user=username, passwd=password,
                                    db=database_name, host='localhost',
                                    port=3306)

    cursor = db_connection.cursor()
    query = """SELECT cities.id, cities.name
               FROM cities
               INNER JOIN states ON cities.state_id = states.id
               WHERE states.name = %s"""
    cursor.execute(query, (state_name,))
    state_cities = cursor.fetchall()

    cities_list = [city[1] for city in state_cities]

    print(', '.join(cities_list))

    db_connection.close()
