#!/bin/bash
# Send the POST request with the JSON data and display the response body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
