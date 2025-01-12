import sys

sys.setrecursionlimit(10 ** 7)

n, s = map(int, input().split())
sequence = list(map(int, input().split()))
c = 0


def backtracking(sum_, depth):
    global c
    if depth >= n:
        return
    if sum_ == s:
        c += 1
        return
    for i in range(n):
        sum_ += sequence[i]
        backtracking(sum_, depth+ 1)
        sum_ -= sequence[i]


backtracking(0, 0)
print(c)
