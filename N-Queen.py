n = int(input())


def Solve(n):
    count = 0

    def Is_safe(row, col):
        return not cols[col] and not diagonal[row + col] and not re_diagonal[row - col]

    def Queen(y):
        nonlocal count
        if y == n:
            count += 1
            return
        for i in range(n):
            if Is_safe(y, i):
                cols[i] = diagonal[y + i] = re_diagonal[y - i] = True
                Queen(y + 1)
                cols[i] = diagonal[y + i] = re_diagonal[y - i] = False

    cols = [False] * n
    diagonal = [False] * (2 * n - 1)
    re_diagonal = [False] * (2 * n - 1)
    c = 0

    Queen(0)
    return count


print(Solve(n))
