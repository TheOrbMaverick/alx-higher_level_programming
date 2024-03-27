#!/bin/bash
# Only displays the body if the HTTP status code is 200
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q "200" && curl -sL "$1"
