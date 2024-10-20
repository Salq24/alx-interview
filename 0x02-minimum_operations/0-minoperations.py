#!/usr/bin/python3

"""
    a method that calculates the fewest number of 
    operations needed to result in exactly n H characters in the file
"""

def minOperations(n):
    """
    This function calcs the fewest number of ops
    needed to get a result of exactly nH xters in
    a file
    """
    one = 1
    start = 0
    cnt = 0
    while one < n:
        remain = n - one
        if (remain % one == 0):
            start = one
            one += start
            cnt += 2
        else:
            one += start
            cnt += 1
    return cnt