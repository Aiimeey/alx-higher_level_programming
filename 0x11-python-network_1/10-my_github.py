#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API
to display your id. Uses Basic Authentication with a personal access token as
password to access your information (only read:user permission is needed).
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    
    response = requests.get(url, auth=(username, password))
    try:
        data = response.json()
        print(data.get('id', None))
    except ValueError:
        print(None)
