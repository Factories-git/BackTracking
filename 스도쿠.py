import sys

input = sys.stdin.readline


def sudoku(x, y):
    nums = check(x, y)
    print(nums)


def check(x, y):
    empty_num = set()
    empty_num_1 = set()
    empty_num_2 = set()
    for i in range(BOARD_LENGTH):
        if sudoku[x][i] == 0:
            empty_num.add((x, i))
    for i in range(BOARD_WIDTH):
        if sudoku[i][y] == 0:
            empty_num_1.add((i, y))
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if sudoku[i][j] == 0:
                empty_num_2.add((i, j))
    empty_num.intersection(empty_num_1)
    empty_num.intersection(empty_num_2)
    empty_num = list(empty_num)
    return empty_num


BOARD_WIDTH = 9
BOARD_LENGTH = 9
sudoku = []
for i in range(BOARD_LENGTH):
    sudoku.append(list(map(int, input().split())))
for i in range(BOARD_LENGTH):
    for j in range(BOARD_WIDTH):
        if sudoku[i][j] == 0:
            sudoku(i, j)
