n, m = map(int, input().split())
arr = list(map(int, input().split()))
re = set()
ans = []
visit = [False] * (n+1)


def backtracking(depth):
    global ans
    if depth == m:
        re.add(tuple(ans))
        return

    for i in range(n):
        if visit[i]:
            continue
        if ans:
            if ans[-1] > arr[i]:
                continue
        ans.append(arr[i])
        visit[i] = True
        backtracking(depth+1)
        visit[i] = False
        ans.pop()


backtracking(0)

for i in sorted(re):
    print(*i)