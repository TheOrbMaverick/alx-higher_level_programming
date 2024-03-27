#!/bin/bash
# Send an OPTIONS request to the URL and display the Allow header
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
