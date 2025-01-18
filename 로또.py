import sys

input = sys.stdin.readline
ans = []


def backtracking(depth, idx):
    global ans

    if depth == 6:
        print(*ans)
        return
    for i in range(idx, s):
        if arr[i] in ans:
            continue
        ans.append(arr[i])
        backtracking(depth + 1, i + 1)
        ans.pop()



while True:
    ipt = list(map(int, input().split()))
    s = ipt[:1][0]
    arr = ipt[1:]
    if s == 0:
        break
    backtracking(0, 0)
    print()