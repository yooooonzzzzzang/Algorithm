import sys

sys.stdin = open('input (2).txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    result = 0
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N-M+1):  # 행 돌 횟수
        for j in range(N-M+1):  # 열 돌 횟수
            temp = 0
            # M x M 범위 내 원소합 저장
            for k in range(M):
                for l in range(M):
                    temp += arr[i + k][j + l]
            if result < temp:
                result = temp

    print(f'#{t} {result}')