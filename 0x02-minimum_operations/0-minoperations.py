#!/usr/bin/python3
"""
A method that calculates the fewest number of 
operations needed to result in exactly n 'H' characters in a file.
"""


def min_operations(n):
    """
    This function calculates the fewest number of operations
    needed to get exactly n 'H' characters in a file.

    :param n: The number of 'H' characters desired.
    :return: The minimum number of operations.
    """
    if n <= 1:
        return 0  # No operations needed if n <= 1

    current_chars = 1  # Starting with 1 'H'
    last_copied = 0    # Number of characters last copied
    operations = 0     # Operation count

    while current_chars < n:
        # If the remaining characters (n - current_chars) is divisible
        # by the current number of characters, we should copy and then paste.
        if (n - current_chars) % current_chars == 0:
            last_copied = current_chars
            operations += 1  # Copy operation
        # Paste operation
        current_chars += last_copied
        operations += 1

    return operations
