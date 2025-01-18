n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = []
def backtracking(depth, idx):
    global ans
    if depth == m:
        print(*ans)
        return
    for i in range(idx, n):
        ans.append(arr[i])
        backtracking(depth + 1, i+1)
        ans.pop()

backtracking(0, 0)