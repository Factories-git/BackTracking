n = int(input())


def Solve(n):
    count = 0
    cols = [True] * n #행, 열 동시에 처리
    diagonal = [True] * (2 * n - 1) #대각선 처리
    re_diagonal = [True] * (2 * n - 1) #역대각선 처리

    def is_safe(row, column):
        #cols의 값과 인덱스는 다음을 의미함: 인덱스 :row, 값:column, 퀸은 룩처럼 상하좌우가 가능하기 때문에 column만 확인해도 됨
        #diagonal : 비숍처럼 퀸은 대각선이 가능, 퀸을 임의의 위치에 둬보고 위치 계산을 해보면 퀸의 공격범위 내 row + column의 값은 일정.
        #re_diagonal : 위와 반대로, 퀸의 공격범위 내 row - column의 값도 일정
        return cols[column] and diagonal[row + column] and re_diagonal[row - column]

    def Queen(y):
        nonlocal count
        if y == n: # y가 n까지 왔다면 퀸을 공격하지 못하게 배치한것
            count += 1 #카운트 올림
            return

        for i in range(n): #x에 대해 반복
            if is_safe(y, i): #이 위치가 안전한 위치 (배치 가능한 위치) 인지 살펴봄
                cols[i] = diagonal[y + i] = re_diagonal[y - i] = False #일단 둬보고
                Queen(y+1) #백트랙 들어감
                cols[i] = diagonal[y + i] = re_diagonal[y - i] = True #판 되돌리기
    Queen(0) #실행
    return count #카운트 반환

print(Solve(n))