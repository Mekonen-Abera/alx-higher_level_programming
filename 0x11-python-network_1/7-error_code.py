#!/usr/bin/python3
"""
Script that receives a URL, sends a request to the URL
and shows the response body.

Usage: ./7-error_code.py <URL>
 - Manages HTTP errors. 
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
