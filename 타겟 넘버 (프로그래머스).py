def solution(numbers, target):
    sequence = numbers
    answer = 0

    def backtracking(re, depth):
        nonlocal answer
        if re == target and depth == len(numbers):
            answer += 1
        if depth == len(numbers):
            return
        re += sequence[depth]
        backtracking(re, depth + 1)
        re -= sequence[depth]
        re -= sequence[depth]
        backtracking(re, depth + 1)
        re += sequence[depth]

    backtracking(0, 0)
    return answer


print(solution(	[1, 1, 1, 1, 1], 3))
