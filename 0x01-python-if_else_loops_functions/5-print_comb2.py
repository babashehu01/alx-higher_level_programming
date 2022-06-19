#!/usr/bin/python3
for number in range(0, 100):
    if number != 99:
        print(str(number).rjust(2, '0'), end=', ')
    else:
        print(number)
