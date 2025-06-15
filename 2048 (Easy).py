import copy


def rotate_90(game):
    row_length = n
    column_length = n

    res = [[0] * n for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = game[r][c]

    return res


def game_2048(depth, board):
    global result
    for r in board:
        for c in r:
            result = max(c, result)
    if depth == 5:
        return
    tmp = copy.deepcopy(board)
    for i in range(4):
        for _ in range(i):
            board = rotate_90(board)
        new_board = left_move(board)
        game_2048(depth + 1, new_board)

        board = copy.deepcopy(tmp)


def left_move(game):
    board = copy.deepcopy(game)
    return_board = []
    for r, row in enumerate(board):
        tmp_row = []
        merged = [False] * n
        for block in row:
            if block != 0:
                tmp_row.append(block)
        result_row = [0] * n
        idx = 0
        skip = False
        for i in range(len(tmp_row)):
            if skip:
                skip = False
                continue
            if i+1 < len(tmp_row) and tmp_row[i] == tmp_row[i+1] and not merged[idx]:
                result_row[idx] = tmp_row[i] * 2
                merged[idx] = True
                skip = True
            else:
                result_row[idx] = tmp_row[i]
            idx += 1
        return_board.append(result_row)
    return return_board


n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
result = max(max(row) for row in game)
game_2048(0, game)
print(result)