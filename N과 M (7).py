n,m = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = []


def backtracking(depth):
    global ans
    if depth == m:
        print(*ans)
        return
    for i in range(n):
        ans.append(arr[i])
        backtracking(depth + 1)
        ans.pop()

backtracking(0)