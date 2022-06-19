#!/usr/bin/python3
string = ''
for index in range(122, 96, -1):
    if index % 2:
        string += chr(index - 32)
    else:
        string += chr(index)
print("{:s}".format(string), end='')
