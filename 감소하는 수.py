t = int(input())
result = set()
ans = []
def backtracking(n):
    global ans, result

    for i in range(n, -1, -1):
        if i in ans:
            continue
        ans.append(i)
        backtracking(n-1)
        ans.pop()
    for i in range(len(ans)-1):
        if ans[i] < ans[i+1]:
            return
    if ans:
        result.add(''.join(map(str,ans)))
    return


backtracking(9)
result = sorted(map(int, result))
if len(result) <= t:
    print(-1)
    exit(0)
print(result[t])