#!/usr/bin/python3
"""
Solution to the N-Queens problem
"""
import sys


def backtrack(row, n, cols, pos_diag, neg_diag, board):
    """
    Backtracking function to find solutions to the N-Queens problem
    """
    if row == n:
        res = []
        for row_idx in range(len(board)):
            for col_idx in range(len(board[row_idx])):
                if board[row_idx][col_idx] == 1:
                    res.append([row_idx, col_idx])
        print(res)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
            continue

        cols.add(col)
        pos_diag.add(row + col)
        neg_diag.add(row - col)
        board[row][col] = 1

        backtrack(row + 1, n, cols, pos_diag, neg_diag, board)

        cols.remove(col)
        pos_diag.remove(row + col)
        neg_diag.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Finds solutions to the N-Queens problem
    Args:
        n (int): Number of queens. Must be >= 4
    Returns:
        List of lists representing coordinates of each queen possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(args[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
