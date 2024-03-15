#!/usr/bin/python3
"""
Script to list all states from the hbtn_0e_0_usa database.

Usage: ./0-select_states.py <username> <password> <database>
"""

import sys
import MySQLdb


def list_states(username, password, database):

    """
    Connects to the MySQL database and lists all
    states in ascending order by ID.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host='localhost',
                             port=3306, user=username,
                             passwd=password, db=database)
        cursor = db.cursor()

        # Execute SQL query to fetch states sorted by ID
        query = 'SELECT id, name FROM states ORDER BY id ASC'
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
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]
    list_states(username, password, database)
