#!/usr/bin/python3
"""
This script that takes in a URL and an email address,
sends a POST request to the URL
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    value = {'email': email}

    r = requests.post(url, value)

    print(r.text)
