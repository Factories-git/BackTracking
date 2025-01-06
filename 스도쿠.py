import sys, time
from collections import Counter

input = sys.stdin.readline


def sudoku(x, y):
    global Board
    nums = get_num(x, y)
    for i in nums:
        for j in range(len(nums)):
            Board[x][y] = i
            if check(x, y):
                return

def check(x, y):
    width = []
    length = []
    range_ = []
    for i in range(BOARD_WIDTH):
        if Board[x][i] != 0:
            width.append(Board[x][i])
    for j in range(BOARD_LENGTH):
        if Board[j][y] != 0:
            length.append(Board[j][y])
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if Board[i][j] != 0:
                range_.append(Board[i][j])

    w = Counter(width)
    l = Counter(length)
    r = Counter(range_)

    if max(w.values()) > 1 or max(l.values()) > 1 or max(r.values()) > 1:
        return False
    return True


def get_num(x, y):
    empty_num = set(range(1, 10))
    empty_num_1 = set(range(1, 10))
    empty_num_2 = set(range(1, 10))

    for i in range(BOARD_LENGTH):
        if Board[x][i] != 0:
            empty_num.discard(Board[x][i])
    for i in range(BOARD_WIDTH):
        if Board[i][y] != 0:
            empty_num_1.discard(Board[i][y])
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if Board[i][j] != 0:
                empty_num_2.discard(Board[i][j])
    empty_num.intersection(empty_num_1)
    empty_num.intersection(empty_num_2)
    empty_num = list(empty_num)
    return empty_num


s = set(range(1, 9))
BOARD_WIDTH = 9
BOARD_LENGTH = 9
Board = []
for _ in range(BOARD_LENGTH):
    Board.append(list(map(int, input().split())))
for x in range(BOARD_LENGTH):
    for y in range(BOARD_WIDTH):
        if Board[x][y] == 0:
            sudoku(x, y)
for row in Board:
    print(*row)
