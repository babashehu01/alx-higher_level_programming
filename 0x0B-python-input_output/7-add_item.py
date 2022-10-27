#!/usr/bin/python3
"""
This program adds all arguments to a Python list,
and then save them to a file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    contents = load_from_json_file('add_item.json')
except FileNotFoundError:
    contents = []

for arg in sys.argv[1:]:
    contents.append(arg)

save_to_json_file(contents, 'add_item.json')
