import sys
import time

sys.setrecursionlimit(10 ** 6)

n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
ans = 0
diagonal = [False] * (2 * n - 1)
re_diagonal = [False] * (2 * n - 1)


def is_safe(x, y):
    return not diagonal[x + y] and not re_diagonal[y - x]


def solve(y, x, c):
    print(y, x, c)
    global ans
    if y == n:
        ans = max(ans, c)
        return
    if x == n:
        solve(y + 1, 0, c)
        return
    if chess[y][x] == 0 or not is_safe(x, y):
        solve(y, x + 1, c)
        return

    diagonal[y + x] = re_diagonal[y - x] = True
    solve(y, x + 1, c + 1)
    diagonal[y + x] = re_diagonal[y - x] = False

    return


s = time.time()
solve(0, 0, 0)
print(ans, time.time() - s)