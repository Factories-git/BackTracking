n = int(input()) #입력
ability = [list(map(int, input().split())) for _ in range(n)] #입력
re = 10**7 #충분히 큰 값으로 설정
def backtracking(start, depth):
    global re
    if len(start) == n//2: #만약 다 채워졌다면
        rink = [i for i in range(n) if i not in start] #링크 팀에는 스타트 팀에 없는애들 다 넣어줌

        st_sco,ri_sco = 0,0 #0으로 초기화

        for i in range(n // 2): #n/2의 팀원이 있으니 그만큼 반복
            for j in range(i+1, n // 2): #i+1 부터 시작하는 것은, 이미 탐색을 다 했다는 의미
                st_sco += ability[start[i]][start[j]] + ability[start[j]][start[i]] #스타트 팀의 능력치를 총 합에 더함
                ri_sco += ability[rink[i]][rink[j]] + ability[rink[j]][rink[i]] #링크 팀의 능력치를 총 합에 더함

        re = min(re, abs(st_sco - ri_sco)) #최솟값을 찾아야지 공평해짐
        return #함수 종료
    for i in range(depth, n): #depth부터 하는 이유는, start의 팀을 유지한채로 가기 위해서
        start.append(i) #스타트에 넣고,
        backtracking(start, i+1) #그대로 유지한채, 다음 depth(i+1) 즉, 방금 넣은 팀원의 번호
        start.pop() #백트래킹

backtracking([], 0)
print(re) #출력
