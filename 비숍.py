n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
ans = 0
diagonal = [False] * (2 * n - 1)
re_diagonal = [False] * (2 * n - 1)


def solve(y, c):
    global ans

    if y == n:
        ans = max(ans, c)
        return

    def is_safe(x, y):
        return not diagonal[x + y] and not re_diagonal[x - y]

    for i in range(n):
        if is_safe(y, i):
            diagonal[y + i] = re_diagonal[y - i] = True
            solve(y + 1, c + 1)
            diagonal[y + i] = re_diagonal[y - i] = False


solve(0, 0)
print(ans)
