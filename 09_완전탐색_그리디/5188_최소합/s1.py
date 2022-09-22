### DP 로 풀기 - 메모이제이션
import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    n = int(input())
    maxtrix = [list(map(int, input().split())) for _ in range(n)]
    # 메모이제이션
    memo = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 1. 원래 리스트의 값을 더한다.
            memo[i][j] += maxtrix[i][j]

            if i == 0 and j == 0:
                continue

            # 2. 위, 왼쪽을 더해서 최소합으로 갱신
            if i == 0:
                memo[i][j] += memo[i][j-1]
            elif j == 0:
                memo[i][j] += memo[i-1][j]
            else:
                memo[i][j] += min(memo[i][j-1] , memo[i-1][j])



    print(f'#{t} {memo[n-1][n-1]}')