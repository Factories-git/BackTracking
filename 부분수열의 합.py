n, s = map(int, input().split())
sequence = list(map(int, input().split()))
c = 0
sum_ = 0


def backtracking(depth):
    global c, sum_
    if depth == n:
        return

    sum_ += sequence[depth]

    if sum_ == s:
        c += 1

    backtracking(depth + 1)
    sum_ -= sequence[depth]
    backtracking(depth + 1)


backtracking(0)
print(c)
