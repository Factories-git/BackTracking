n = int(input())
count = 0
chess = [[False] * n for i in range(n)]
n_ = 0
c = 0

def Queen(chess, q_c):
    global n_, c
    if n_ == n:
        return
    for i in range(n):
        if not chess[n_][i]:
            chess[n_][i] = True
            Change(chess, [n_, i])
            n_ += 1
            q_c += 1
            Queen(chess, q_c)
    if q_c == n and not all(all(r) for r in chess):
        c += 1
        return
    else:return


def Change(chess, queen):
    tar = queen[0] + queen[1]
    for i in range(n):
        chess[n_][i] = True
    for i in range(n):
        chess[i][n_] = True
    for _ in range(n):
        chess[_][_] = True
    for _ in range(n):
        for __ in range(n):
            if _ + __ == tar:
                chess[_][__] = True


Queen(chess, 0)
print(c)