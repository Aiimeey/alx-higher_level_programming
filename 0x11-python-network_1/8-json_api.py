#!/usr/bin/python3
"""
Takes in a data and sends a POST request to http://0.0.0.0:5000/search_user
with the data as a parameter. Displays the id and name if the response body
is properly JSON formatted and not empty, otherwise displays appropriate messages.
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    data = argv[1] if len(argv) > 1 else ""
    
    response = requests.post(url, data={'q': data})
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
