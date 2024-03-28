#!/usr/bin/python3
"""
Takes GitHub credentials (username and personal access token)
and uses the GitHub API
to display the user id.
Uses Basic Authentication with the personal access token
to access user information.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            user_data = response.json()
            print(user_data['id'])
        else:
            print("None")
    except Exception as e:
        print("None")
