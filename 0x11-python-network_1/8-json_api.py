#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
If no argument is given, sets q=""
If the response body is properly JSON formatted and not empty, displays the id and name like this: [<id>] <name>
Otherwise:
- Displays Not a valid JSON if the JSON is invalid
- Displays No result if the JSON is empty
Uses the requests and sys packages.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post(url, data={"q": q})
        data = response.json()

        if isinstance(data, dict) and data:
            print(f"[{data['id']}] {data['name']}")
        elif isinstance(data, dict) and not data:
            print("No result")
        else:
            print("Not a valid JSON")

    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(e)
