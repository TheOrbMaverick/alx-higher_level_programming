#!/bin/bash
# The script uses curl with the -s (silent) option to send the request and suppress progress/output
curl -sX DELETE "$1"
