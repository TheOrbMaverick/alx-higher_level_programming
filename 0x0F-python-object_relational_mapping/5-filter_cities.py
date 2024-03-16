#!/usr/bin/python3
"""
Script to list all cities of a given state from the database hbtn_0e_4_usa.

Usage: ./5-filter_cities.py <username> <password> <database> <state_name>
"""

import sys
import MySQLdb


def filter_cities(username, password, database, state_name):
    """
    Connects to a MySQL database and lists all cities of a given state.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to filter cities for.

    Returns:
        None
    """
    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        # Execute SQL query to filter cities by state
        query = """SELECT cities.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC"""
        cursor.execute(query, (state_name,))

        # Fetch and display results
        results = cursor.fetchall()
        if results:
            cities = ', '.join([row[0] for row in results])
            print(cities)
        else:
            print("No cities found for the given state.")

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
    filter_cities(username, password, database, state_name)
