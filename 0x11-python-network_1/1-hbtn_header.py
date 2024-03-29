#!/usr/bin/python3
"""
Script that accepts a URL, sends a request to the URL, and retrieves
the value of the X-Request-Id variable from the response header.

Usage: ./1-hbtn_header.py <URL>
"""
from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    with urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
