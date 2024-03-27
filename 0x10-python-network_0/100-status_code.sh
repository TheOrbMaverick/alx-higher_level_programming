#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response
# The script uses curl with silent mode to send the request and store the output in a temporary file
# It then extracts and displays the status code from the temporary file

curl -s -o temp_file "$1"    # Send the request and save the output to a temporary file
grep -oP '(?<=HTTP/1.1 )\d+' temp_file  # Extract and display only the status code
rm temp_file  # Remove the temporary file
