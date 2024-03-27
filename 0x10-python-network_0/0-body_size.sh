#!/bin/bash
# The script uses curl with the -s (silent) option to send the request and suppress progress/output
curl -sI "$1" | grep -i "Content-Length:" | awk '{print $2}'
