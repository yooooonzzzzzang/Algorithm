import sys

sys.stdin = open('sample_input(1).txt')
    # 상 하 좌 우 왼위, 오위, 왼아, 오아
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

for t in range(1, int(input()) + 1):
    # n : 보드의 길이, m: 돌을 놓는 횟수
    n, m = map(int,input().split())
    boards = [[0] * n for _ in range(n)]
    # 시작 돌 세팅
    mid = n // 2
    boards[mid-1][mid-1] = 2
    boards[mid-1][mid] = 1
    boards[mid][mid-1] = 1
    boards[mid][mid] =2

    # 게임하기
    for _ in range(m):
    # 1: 흑돌 , 2: 백돌
        y, x, color = map(int, input().split())     # 인풋 반대로 됨
        y -= 1                                      # 좌표 1부터 시작
        x -= 1
        if not boards[x][y]:
            boards[x][y] = color
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                color_change = []
                while True:
                    #nx < 0 or n - 1 < nx or ny < 0 or n - 1 < ny:
                    if not(0<=nx<n and 0<=ny<n): # 범위 안인지
                        color_change = []
                        break
                    if boards[nx][ny] == 0:     # 공백인지 확인
                        color_change = []
                        break
                    if boards[nx][ny] == color: # 같은 색이면 멈춤
                        break
                    else:                       # 다른 색일때 좌표를 저장
                        color_change.append((nx, ny))
                        nx += dx[i]
                        ny += dy[i]
                for change_x, change_y in color_change:
                    boards[change_x][change_y] = color

    # 돌 개수 세주기
    white_cnt = 0
    black_cnt =0
    for i in range(n):
        for j in range(n):
            if boards[i][j] == 1:
                black_cnt += 1
            elif boards[i][j] == 2:
                white_cnt += 1
    print(f'#{t} {black_cnt} {white_cnt}')