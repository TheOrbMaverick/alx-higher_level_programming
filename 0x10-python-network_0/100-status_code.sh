#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response
curl -s -o temp_file "$1" | grep -oP '(?<=HTTP/1.1 )\d+' temp_file | rm temp_file
