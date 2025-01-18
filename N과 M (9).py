from collections import Counter


n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
ans = []
re = set()
c = Counter(arr)
def backtracking(depth):
    if depth == m:
        re.add(tuple(ans))
        return

    for i in range(n):
        if arr[i] in ans and c[arr[i]] <= depth:
            continue

        ans.append(arr[i])
        backtracking(depth + 1)
        ans.pop()


backtracking(0)
re = sorted(re)
for j in re:
    print(*j)