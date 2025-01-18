from collections import Counter
n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = []
c = [False] * (n+1)
re = set()

def backtracking(depth):
    if depth == m:
        re.add(tuple(ans))
        return

    for i in range(n):
        if not c[i]:
            c[i] = True
            ans.append(arr[i])
            backtracking(depth + 1)
            ans.pop()
            c[i] = False


backtracking(0)
re = sorted(re)
for j in re:
    print(*j)