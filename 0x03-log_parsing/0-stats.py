#!/usr/bin/python3

"""reads stdin by line and computes the metrics"""

import sys


def prnt(m_dict, size):
    """prints the info"""
    print("File size: {:d}".format(size))
    for x in sorted(m_dict.keys()):
        if m_dict[x] != 0:
            print("{}: {:d}".format(x, m_dict[x]))

stat_code = {"200": 0, "301": 0, "400": 0, "400":0, "403": 0,
             "404": 0, "405": 0, "500": 0}

cnt = 0
size = 0

try:
    for one_line in sys.stdin:
        if cnt != 0 and cnt % 10 == 0:
            prnt(stat_code, size)

        stlist = one_line.split()
        cnt += 1

        try:
            size += int(stlist[-1])
        except:
            pass

        try:
            if stlist[-2] in stat_code:
                stat_code[stlist[-2]] += 1
        except:
            pass
    prnt(stat_code, size)


except KeyboardInterrupt:
    prnt(stat_code, size)
    raise
