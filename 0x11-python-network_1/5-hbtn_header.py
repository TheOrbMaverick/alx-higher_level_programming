#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the value of the
X-Request-Id variable in the response header using the requests and sys packages.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    
    # Check if X-Request-Id exists in the response headers
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
    else:
        print("X-Request-Id not found in the response headers")
