#!/usr/bin/python3
def no_c(my_string):
    ret = ""
    for character in my_string:
        if character != 'c' and character != 'C':
            ret += character
    return ret
