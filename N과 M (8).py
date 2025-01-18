n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = []


def backtracking(depth):
    if depth == m:
        print(*ans)
        return

    for i in range(n):
        if ans:
            if ans[-1] > arr[i]:
                continue

        ans.append(arr[i])
        backtracking(depth + 1)
        ans.pop()


backtracking(0)
