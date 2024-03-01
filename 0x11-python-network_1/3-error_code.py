#!/usr/bin/python3
"""
Script that accepts a URL, sends a request to the URL, and displays the response
body decoded in utf-8. It also handles HTTP errors.

Usage: ./3-error_code.py <URL>
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
