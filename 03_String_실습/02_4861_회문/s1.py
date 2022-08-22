import sys

sys.stdin = open('sample_input.txt')
'''
회문 검사 - 슬라이싱을 이용
if s == s[::-1]:

1. 가로 방향으로 회문 찾기
2. 세로 방향으로 회문 찾기   
'''
for t in range(1, int(input()) + 1):
    # N: 문자판 길이 M: 회문 길이
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = ''
    col_arr = []
    for i in range(N):  # arr 의 세로 방향 2차원배열 만들기
        line = []
        for j in range(N):
            line.append(arr[j][i])
        col_arr.append(line)

    for i in range(N):
        for j in range(N-M+1):  # 비교할 횟수
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:    # 가로
                result = ''.join(arr[i][j:j+M])
            elif col_arr[i][j:j+M] == col_arr[i][j:j+M][::-1]:  # 세로
                result = ''.join(col_arr[i][j:j+M])


    print(f'#{t} {result}')
