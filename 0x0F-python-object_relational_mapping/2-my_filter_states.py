#!/usr/bin/python3
"""
Script to search for a state in the states table of hbtn_0e_0_usa.

Usage: ./search_states.py <username> <password> <database> <state_name>
"""

import sys
import MySQLdb


def search_states(username, password, database, state_name):

    """
    Connects to a MySQL database and searches
    for a state with the provided name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to search for.

    Returns:
        None
    """

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute SQL query with user input
        query = """SELECT * FROM states WHERE name = '{}'
                    ORDER BY id ASC""".format(state_name)
        cursor.execute(query)

        # Fetch and display results
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL database: {e}")

    finally:
        # Close cursor and database connection
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == '__main__':
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print(f"""Usage: {sys.argv[0]} <username>
              <password> <database> <state_name>""")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]
    search_states(username, password, database, state_name)
