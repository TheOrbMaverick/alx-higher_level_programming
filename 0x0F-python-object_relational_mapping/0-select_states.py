import MySQLdb;
import sys;

"""
Script to list all states from the hbtn_0e_0_usa database.

Usage:
./0-select_states.py <username> <password> <database>
"""

def list_states(username, password, database):
    """
    Connects to the MySQL database and lists all states in ascending order by ID.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """

    #connect to database
    db = MySQLdb.connect (host = 'localhost', port = 3306, user = username, passwd = password, database = database)
    cursor = db.cursor()

    # Execute SQL query to fetch states sorted by ID
    query = 'SELECT id, name FROM states ORDER BY id ASC'
    cursor.execute(query)

    # Fetch and display results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close()
