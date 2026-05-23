N = 8

def fn(board=None, row=0, prefix=""):
    if board is None:
        board = [-1] * N

    # show node
    print(prefix + f"Row {row}")

    if row == N:
        print(prefix + "✅ Solution\n")
        return

    for col in range(N):
        if is_safe(board, row, col):
            print(prefix + f"├── Try col {col} ✔")
            board[row] = col
            fn(board, row + 1, prefix + "│   ")
            board[row] = -1
        else:
            print(prefix + f"├── Try col {col} ✘")


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


fn()