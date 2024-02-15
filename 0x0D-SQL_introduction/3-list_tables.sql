#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

# Assign the database name from the command-line argument
database_name="$1"

# MySQL command to list tables in the specified database
mysql -e "USE $database_name; SHOW TABLES;"
