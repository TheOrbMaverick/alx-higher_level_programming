import MySQLdb;
import sys;

def listStates(username, password, dbname):

    #connect to database
    db = MySQLdb.connect (host = localhost, port = 3306, user = username, passwd = password, database = dbname)
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
    