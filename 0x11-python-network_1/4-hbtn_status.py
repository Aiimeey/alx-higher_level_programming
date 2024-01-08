#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    """response = requests.get(url)"""
    with requests.get('https://alx-intranet.hbtn.io/status') as response:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
