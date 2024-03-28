#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
body of the response.
If the HTTP status code is greater than or equal to 400,
prints Error code: followed by the value of the HTTP status code
Uses the requests and sys packages.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./7-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    response = requests.get(url)
    print(response.text)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
