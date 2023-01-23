#!/usr/bin/python3
"""
Takes in a url and display X-Request-Id header
"""
import sys
import requests

url = sys.argv[1]
r = requests.get(url)
print(r.headers.get('X-Request-Id'))
