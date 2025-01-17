n, s = map(int, input().split())
arr = sorted(map(int, input().split()))

ans = []


def backtracking(depth):
    global ans

    if len(ans) == s:
        print(*ans)
        return

    for i in range(n):
        if arr[i] in ans:
            continue

        ans.append(arr[i])
        backtracking(depth + 1)
        ans.pop()


backtracking(0)
