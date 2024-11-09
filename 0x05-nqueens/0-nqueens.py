#!/usr/bin/python3
"""  a program that solves the N queens problem
"""
import sys


def print_usage_and_exit(message):
    """Prints an error message and exits with status 1"""
    print(message)
    sys.exit(1)


def is_valid(board, row, col):
    """Checks if placing a queen at (row, col) is valid"""
    for i in range(row):
        # Check the same column
        if board[i] == col:
            return False
        # Check the diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N):
    """Finds and prints all solutions to the N queens problem"""
    def backtrack(row):
        if row == N:
            # Found a solution, print it
            solution = [[i, board[i]] for i in range(N)]
            print(solution)
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)

    board = [-1] * N
    backtrack(0)


def main():
    # Check if the user provided the correct number of arguments
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    # Validate if the argument is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    # Ensure that N is at least 4
    if N < 4:
        print_usage_and_exit("N must be at least 4")

    # Solve the N queens problem
    solve_nqueens(N)


if __name__ == "__main__":
    main()
