#!/usr/bin/python3
""" Solve N Queens problem. """


def place_Q(n, row, columns, r_diag, l_diag, res, board):
    """ Checks and recursion logic for placing the Queens. """
    if row == n:
        res.append(board[:])  # Append a copy of the current board
        return

    for col in range(n):
        if col not in columns and (row + col) not in r_diag and \
                (row - col) not in l_diag:
            # Place the queen
            columns.add(col)
            r_diag.add(row + col)
            l_diag.add(row - col)
            board.append([row, col])  # Store position as [row, col]

            # Recur for the next row
            place_Q(n, row + 1, columns, r_diag, l_diag, res, board)

            # Backtrack
            columns.remove(col)
            r_diag.remove(row + col)
            l_diag.remove(row - col)
            board.pop()


def N_Queens(n):
    """ Calling Function. """
    res = []
    place_Q(n, 0, set(), set(), set(), res, [])
    return res


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    result = N_Queens(N)
    for solution in result:
        print(solution)
