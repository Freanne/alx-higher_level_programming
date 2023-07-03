#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if it is safe to place a queen at board[row][col]"""
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col, solutions):
    """Recursive function to solve the N-queens problem"""
    if col >= N:
        # All queens are placed, add the current solution to the list
        solution = [[r, c] for r, c in enumerate(board)]
        solutions.append(solution)
        return

    for row in range(N):
        if is_safe(board, row, col):
            # Place the queen at board[row][col]
            board[row][col] = 1

            # Recur for the next column
            solve_nqueens(board, col + 1, solutions)

            # Backtrack and remove the queen from board[row][col]
            board[row][col] = 0


def print_solutions(solutions):
    """Print the solutions in the desired format"""
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    # Read the value of N from the command-line argument
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

    # Create an empty board
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N-queens problem
    solutions = []
    solve_nqueens(board, 0, solutions)

    # Print the solutions
    print_solutions(solutions)
