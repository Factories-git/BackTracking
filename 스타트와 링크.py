n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]

def backtracking(start, rink, x, y):
    if x == n:
        backtracking(start, rink, 0, y+1)
    if y == n:
        print(abs(start - rink))
        return
    for i in range(n):
        if i == x:
            continue
        start += ability[i][x] + ability[x][i]