n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def solve():
    black = 0
    white = 0
    white_dia = [True] * (2 * n - 1)
    white_re_dia = [True] * (2 * n - 1)
    black_dia = [True] * (2 * n - 1)
    black_re_dia = [True] * (2 * n - 1)

    def is_safe(r, c, color):
        if color == 'W':
            return white_dia[r + c] and white_re_dia[r - c] and True if board[r][c] != 0 else False
        if color == 'B':
            return black_dia[r + c] and black_re_dia[r - c] and True if board[r][c] != 0 else False

    def bishop(r, c, count, color):
        nonlocal white, black
        if c >= n:
            r += 1
            if color == 'W':
                c = 0 if r % 2 == 0 else 1
            else:
                c = 1 if r % 2 == 0 else 0
        if r == n:
            if color == 'W':
                white = max(count, white)
            else:
                black = max(count, black)
            return
        if is_safe(r, c, color):
            if color == 'W':
                white_re_dia[r - c] = white_dia[r + c] = False
                bishop(r, c + 2, count + 1, color)
                white_dia[r + c] = white_re_dia[r - c] = True
            else:
                black_dia[r + c] = black_re_dia[r - c] = False
                bishop(r, c + 2, count + 1, color)
                black_dia[r + c] = black_re_dia[r - c] = True
        bishop(r, c + 2, count, color)

    bishop(0, 0, 0, 'W')
    bishop(0, 1, 0, 'B')
    print(white + black)


solve()