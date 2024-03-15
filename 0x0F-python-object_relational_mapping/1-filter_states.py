#!/usr/bin/python3

"""
function that queries allll
"""

import MySQLdb
import sys


def list_states_N(username, password, database):

    """
    Query db for names
    """

    try:
        db = MySQLdb.connect( host= 'localhost',
                            port = 3306,
                            user = username,
                            psword = password,
                            databs = database)
        cursor = db.cursor()

        query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
        cursor.execute(query)

        result = cursor.fetchall()
        for row in result:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to database: {e}")
        

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]
    list_states_N(username, password, database)
