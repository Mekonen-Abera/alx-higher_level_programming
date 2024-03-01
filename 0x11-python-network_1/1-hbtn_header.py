#!/usr/bin/python3
"""
Script that accepts a URL, sends a request to the URL, 
and retrieves the value of the X-Request-Id variable from the response header.

Usage: ./1-hbtn_header.py <URL>
"""
import sys

import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
