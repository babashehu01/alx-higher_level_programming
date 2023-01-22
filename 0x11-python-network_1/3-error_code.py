#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
(handling HTTP errors)
"""
import sys
from urllib import request, error


if __name__ == '__main__':

    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as reponse:
            print(reponse.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
