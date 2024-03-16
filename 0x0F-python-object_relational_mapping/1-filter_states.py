#!/usr/bin/python3
"""
Script to list all states with a name starting with
'N' from the database hbtn_0e_0_usa.

Usage:
./list_states.py <username> <password> <database>

Arguments:
- username: MySQL username.
- password: MySQL password.
- database: Database name.

Requirements:
- The script uses the MySQLdb module (import MySQLdb) to interact with MySQL.
- It connects to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by states.id.

Example:
./list_states.py root password hbtn_0e_0_usa
"""

import sys
import MySQLdb


def list_states(username, password, database):
    """
    Connects to the MySQL database and lists all states with a name starting
    with 'N' in ascending order by ID.

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
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)
        cursor = db.cursor()

        # Execute SQL query to fetch states starting with 'N' and sorted by ID
        query = """SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY id ASC"""
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
