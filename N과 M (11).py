n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
visit = [False] * (n+1)
re = set()


def backtracking(depth):
    global ans
    if depth == m:
        re.add(tuple(ans))
        return
    for i in range(n):
        ans.append(arr[i])
        backtracking(depth + 1)
        ans.pop()


backtracking(0)
for i in sorted(re):
    print(*i)