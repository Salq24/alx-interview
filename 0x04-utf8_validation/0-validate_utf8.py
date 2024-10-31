#!/usr/bin/python3
"""determines if a given data set
represents a valid UTF-8 encoding."""


def validUTF8(data):
    """utf-8 validation"""

    n_bytes = 0
    
    test_1 = 1 << 7
    test_2 = 1 << 6

    for i in data:
        mask = 1 << 7
        if n_bytes == 0:
            while mask & i :
                n_bytes += 1
                mask = mask >> 1
            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (i & test_1 and not (i & test_2)):
                return False
            
        n_bytes -= 1

    if n_bytes == 0:
        return True
    
    return False