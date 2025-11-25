#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a number using a recursive approach.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the number n. If n is 0, the function returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Read command-line argument and compute factorial
f = factorial(int(sys.argv[1]))
print(f)
