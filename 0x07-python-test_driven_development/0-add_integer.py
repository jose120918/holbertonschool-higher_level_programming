#!/usr/bin/python3
"""Function that adds two integers"""


def add_integer(a, b=98):
    """Add two integers o floats

    Args:
        a (int: first integer]
        b (int, optional): second integer. Defaults to 98.
    Raises:
        TypeError: If they are not integers or float
    Returns:
        a and b as integers
    """

    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
