n, m = map(int, input().split())
arr = input().split()
arr.sort()
ans = []
re = set()

def backtracking(depth, idx):
    global ans
    if depth == n:
        re.add(tuple(ans))
        return
    for i in range(idx, m):
        ans.append(arr[i])
        backtracking(depth+1, i+1)
        ans.pop()


backtracking(0, 0)
vowel = {'a', 'e', 'i', 'o', 'u'}
for i in sorted(re):
    v_c = 0
    for j in i:
        if j in vowel:
            v_c += 1
    c_c = len(i) - v_c
    if v_c >= 1 and c_c >= 2:
        print(''.join(list(i)))