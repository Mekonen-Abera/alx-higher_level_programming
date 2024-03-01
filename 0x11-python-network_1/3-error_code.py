#!/usr/bin/python3
"""
Script that accepts a URL, sends a request to the URL, and displays the response
body decoded in utf-8. It also handles HTTP errors.

Usage: ./3-error_code.py <URL>
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
