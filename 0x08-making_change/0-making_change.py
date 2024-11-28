#!/usr/bin/python3
"""function"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed
    to meet a given amount total.

    Parameters:
        coins (list): A list of the values of the
        coins in your possession.
        total (int): The total amount to achieve.

    Returns:
        int: Fewest number of coins needed to meet the
        total, or -1 if not possible.
    """
    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for y in coin:
            while(total >= y):
                counter += 1
                total -= y
        if total == 0:
            return counter
        return -1
