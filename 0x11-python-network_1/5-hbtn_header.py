#!/usr/bin/python3
"""
Script that accepts a URL, sends a request to the URL, and shows 
the value of the X-Request-Id variable in the response header.

Usage: ./5-hbtn_header.py <URL>
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.get(url)

    print(req.headers.get("X-Request-Id"))
