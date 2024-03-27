#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response
# The JSON data is read from a file whose filename is passed as the second argument

# Check if the filename argument is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 URL JSON_FILE"
    exit 1
fi

# Check if the JSON file exists
if [ ! -f "$2" ]; then
    echo "Error: JSON file '$2' not found"
    exit 1
fi

# Send the POST request with the JSON data and display the response body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
