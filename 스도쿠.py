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

'''
동일한 풀이 방법의 코드, 시간은 전자가 더 빠름. 참고로 위의 코드는, 2580번이고 밑의 코드는 2239번임. (동일 문제)
'''

input = sys.stdin.readline

BOARD_SIZE = 9


def get_num(x: int, y: int) -> set:
    check_col = set(range(1, 10))
    for i in range(BOARD_SIZE):
        if board[x][i]:
            check_col.discard(board[x][i])

    check_row = set(range(1, 10))
    for i in range(BOARD_SIZE):
        if board[i][y]:
            check_row.discard(board[i][y])

    check_rect = set(range(1, 10))
    start_x = (x // 3) * 3
    start_y = (y // 3) * 3
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if board[i][j]:
                check_rect.discard(board[i][j])

    return check_row & check_col & check_rect


def sudoku(idx: int):
    if idx == len(blank):
        for line in board:
            for i in line:
                print(i, end='')
            print()
        exit(0)

    x, y = blank[idx]
    nums = get_num(x, y)
    for num in nums:
        board[x][y] = num
        sudoku(idx + 1)
        board[x][y] = 0


board = [list(map(int, input().strip())) for _ in range(BOARD_SIZE)]
blank = [
    (i, j)
    for i in range(BOARD_SIZE)
    for j in range(BOARD_SIZE)
    if board[i][j] == 0
]

sudoku(0)
