#!/usr/bin/python3
"""Thhis sends a POST request to the given URL with the given email"""

import sys 
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencide(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urloprn(request) as response:
        print(response.read().decode("utf-8"))
