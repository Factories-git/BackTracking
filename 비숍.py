import sys

sys.setrecursionlimit(10**6)

n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
ans = 0
diagonal = [False] * (2 * n - 1)
re_diagonal = [False] * (2 * n - 1)


def is_safe(x, y):
    return not diagonal[x + y] and not re_diagonal[x - y]


def solve(y, x, c):
    global ans
    if y == n:
        ans = max(ans, c)
        return
    if x == n:
        solve(y + 1, 0, c)
    if chess[x][y] == 0 and not is_safe(x, y):
        return
    for i in range(x, n):
        diagonal[y + i] = re_diagonal[y - i] = True
        solve(y, i, c + 1)
        print(y, i, c, x)
        diagonal[y + i] = re_diagonal[y - i] = False


solve(0, 0, 0)
print(ans)
