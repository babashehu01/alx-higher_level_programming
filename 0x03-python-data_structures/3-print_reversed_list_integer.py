#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    num = len(my_list) - 1
    while num > -1:
        print("{:d}".format(my_list[num]))
        num -= 1
