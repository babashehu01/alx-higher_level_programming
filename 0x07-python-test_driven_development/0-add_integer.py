#!/usr/bin/python3
"""

add_integer function

adds 2 integers and return their sum

"""

def add_integer(a, b=98):
    """

    Function that adds two integers and/or float number

    Args:
        a: first number
        b: second number

    Returns:
        The sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float

    """
    if type(a) not in [int, float]:
        raise TypeError('a must be integer')
    elif type(b) not in [int, float]:
        raise TypeError('b must be integer')
    a = int(a)
    b = int(b)

    return (a + b)
