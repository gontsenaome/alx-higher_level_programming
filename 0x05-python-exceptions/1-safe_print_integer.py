#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format().
    Args:
    value (int): The integer to print.
    Returns:
    if a TypeError or ValueError occurs - False.
    otherwise - true
    """
    try:
        print("{:d}".format(value))
        return (true)
    except (TypeError, ValueError):
        return (false)
