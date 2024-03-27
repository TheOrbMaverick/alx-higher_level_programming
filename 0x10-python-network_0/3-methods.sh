#!/bin/bash
# The allowed methods are extracted from the Allow header in the response headers
curl -si "$1" | grep -i "Allow:" | awk '{print $2}'