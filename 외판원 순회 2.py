n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')


def backtracking(start, depth, visited, weight, now):
    global answer

    if depth == n+1:
        weight += cities[now][start]
        if cities[now][start] == 0:
            return
        if weight < answer and all([i != 0 for i in visited]):
            answer = weight
        return

    for idx, isvisited in enumerate(visited):
        if isvisited or cities[now][idx] == 0:
            continue
        visited[idx] = depth
        backtracking(start, depth+1, visited, weight + cities[now][idx], idx)
        visited[idx] = 0


s = [0] * n
s[0] = 1
backtracking(0, 2, s, 0, 0)
print(answer)