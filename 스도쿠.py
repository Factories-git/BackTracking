import sys

input = sys.stdin.readline


def sudoku(x, y):
    global Board
    if x == 9:
        return True
    if y == 9:
        return sudoku(x + 1, 0)
    if Board[x][y] != 0:
        return sudoku(x, y + 1)
    for i in range(1, 10):
        if check(x, y, i):
            Board[x][y] = i
            if sudoku(x, y + 1):
                return True
            Board[x][y] = 0
    return False


def check(x, y, n):
    for i in range(BOARD_WIDTH):
        if Board[x][i] == n:
            return False
    for i in range(BOARD_LENGTH):
        if Board[i][y] == n:
            return False
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if Board[i][j] == n:
                return False
    return True


s = set(range(1, 9))
BOARD_WIDTH = 9
BOARD_LENGTH = 9
Board = []
for _ in range(BOARD_LENGTH):
    Board.append(list(map(int, input().split())))
sudoku(0, 0)
for row in Board:
    print(*row)
