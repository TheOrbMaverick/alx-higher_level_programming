#!/bin/bash
# The script adds a custom header X-School-User-Id with the value 98 to the request
curl -sH "X-School-User-Id: 98" "$1"