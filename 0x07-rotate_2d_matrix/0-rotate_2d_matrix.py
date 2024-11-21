#!/usr/bin/python3
"""rotates an n * n 2d matrix, 90 degrees
clockwise"""


def rotate_2d_matrix(matrix):
    """args: matrix
       function"""
    leftside, rightside = 0, len(matrix) - 1

    while leftside < rightside:
        for x in range(rightside - leftside):
            up, down = leftside, rightside
            upleftside = matrix[up][leftside + x]
            matrix[up][leftside + x] = matrix[down - x][leftside]
            matrix[down - x][leftside] = matrix[down][rightside - x]
            matrix[down][rightside - x] = matrix[up + x][rightside]
            matrix[up + x][rightside] = upleftside
        rightside -= 1
        leftside += 1