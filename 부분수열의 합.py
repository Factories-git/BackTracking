import sys

n, s = map(int, input().split())
sequence = list(map(int, input().split()))
c = 0


def backtracking(sum_, depth):
    global c
    if depth >= n:
        return
    if sum_ == s:
        c += 1
        sum_ -= sequence[depth]
        return
    backtracking(sum_+sequence[depth], depth+1)

backtracking(0, 0)
print(c)
