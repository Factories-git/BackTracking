n, m = map(int, input().split())
ans = []
def BackTracking(depth):
    if depth == m:
        print(*ans)
        return
    for i in range(1, n+1):
        ans.append(i)
        BackTracking(depth+1)
        ans.pop()

BackTracking(0)