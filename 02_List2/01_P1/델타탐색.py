import sys

sys.stdin = open('input.txt', encoding='utf-8')

for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    total = 0
    for i in range(n):  # 델타 탐색
        for j in range(n):
            for k in range(4):  # 상하좌우탐색
                ni, nj = i + dx[k], j + dy[k]
                if 0 <= ni < n and 0 <= nj < n:  # 범위 확인
                    total += abs(arr[ni][nj]-arr[i][j])
    print(f'#{t} {total}')