def solution(word):
    answer = 0
    vowel = 'AEIOU '
    ans = []
    def backtracking(pointer, ans, depth):
        if depth == 6:
            return
        if ans:
            data.append(ans)
        for i in range(5):
            backtracking(0, ''.join([ans, vowel[i]]), depth + 1)


    data = []
    backtracking(0, '', 0)
    return data.index(word) + 1

print(solution('AAAAE'))