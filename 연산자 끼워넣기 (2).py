n = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_ = float('-inf')
min_ = float('inf')
oper = '+-*/'

def backtracking(depth, result):
    global max_, min_
    if depth == n:
        max_ = max(result, max_)
        min_ = min(result, min_)
        return

    for i in range(4):
        count, operation = operator[i], oper[i]
        if count > 0:
            operator[i] -= 1
            if operation == '+':
                backtracking(depth + 1, result + arr[depth])
            elif operation == '-':
                backtracking(depth + 1, result - arr[depth])
            elif operation == '*':
                backtracking(depth + 1, result * arr[depth])
            elif operation == '/':
                if result < 0:
                    backtracking(depth + 1, -(-result // arr[depth]))
                else:
                    backtracking(depth + 1, result // arr[depth])
            operator[i] += 1


backtracking(1, arr[0])
print(max_, min_, sep='\n')