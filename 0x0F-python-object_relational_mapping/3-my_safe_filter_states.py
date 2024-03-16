#!/usr/bin/python3
"""
Script to search for a state in the states
table of hbtn_0e_0_usa (safe from MySQL injection).

Usage: ./3-my_safe_filter_states.py <username>
<password> <database> <state_name>
"""

import sys
import MySQLdb


def safe_search_states(username, password, database, state_name):
    """
    Connects to a MySQL database and searches for a state
    with the provided name (safe from MySQL injection).

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

        # Execute SQL query with parameterized query
        query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

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
    safe_search_states(username, password, database, state_name)
