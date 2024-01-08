#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the body
of the response. Handles urllib.error.HTTPError exceptions and
prints: Error code: followed by the HTTP status code.
"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
