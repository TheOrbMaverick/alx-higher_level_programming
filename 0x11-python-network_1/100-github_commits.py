#!/usr/bin/python3
"""
This script fetches the 10 most recent commits of a GitHub repository by a specific user.
Usage: ./100-github_commits.py <repository_name> <owner_name>
Example: ./100-github_commits.py rails rails
"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://developer.github.com/{owner}/{repo}/commits/"

    try:
        response = requests.get(url)
        commits = response.json()[:10]
        for commit in commits:
            sha = commit["sha"]
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.RequestException as e:
        print(f"Error fetching comments: {e}")
