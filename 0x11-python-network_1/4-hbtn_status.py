#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package.
Displays the body of the response with specific formatting.
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    # Displaying the body of the response with specific formatting
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
