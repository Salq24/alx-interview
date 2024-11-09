#!/usr/bin/python3
"""  a program that solves the N queens problem
"""
import sys


def print_solution(board):
    """Prints the board in the required format"""
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)

def is_safe(board, row, col):
    """Checks if a queen can be placed at board[row][col]"""
    for i in range(row):
        # Check the same column and both diagonals
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(N):
    """Solves the N-Queens problem using backtracking"""
    def backtrack(row, board):
        if row == N:
            print_solution(board)
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(row + 1, board)

    board = [-1] * N
    backtrack(0, board)

def main():
    """Main function to handle user input and run the solver"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solve_nqueens(N)

if __name__ == "__main__":
    main()
