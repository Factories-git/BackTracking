n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def Solve(n):
    c = 0
    def is_safe(x, y):
        return not chess[x][y]

    def synchronize(x, y):
        global chess

        tar = x + y
        for i in range(n):
            chess[i][i] = 0
        for i in range(n):
            for j in range(n):
                if i + j == tar:
                    chess[i][j] = 0


    def arrangement(y):
        global ans

        if y == n:
            ans = max(ans, c)
            return
        for i in range(n):
            if is_safe(y, i):
                pass

def synchronize(x, y):
    ret = []

    tar = x + y
    tar2 = x - y
    for i in range(n):
        for j in range(n):
            if i + j == tar:
                if chess[i][j] == 1:
                    ret.append((i, j))
            elif i - j == tar2:
                if chess[i][j] == 1:
                    ret.append((i, j))

    return ret


print(synchronize(0, 2))