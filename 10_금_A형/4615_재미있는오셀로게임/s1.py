import sys

sys.stdin = open('sample_input(1).txt')
    # 상 하 좌 우 왼위, 오위, 왼아, 오아
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs()

for t in range(1, int(input()) + 1):
    result = 0
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
    for i in range(m):
    # 1: 흑돌 , 2: 백돌
        x, y, color = map(int, input().split())
        for i in range(8):
            while True:




        boards[x-1][y-1] = color
    print(boards)



    # 돌 개수 세주기
    white_cnt = 0
    black_cnt =0
    for i in boards:
        if i == 1:
            black_cnt += 1
        elif i == 2:
            white_cnt += 1
    print(f'#{t} {black_cnt} {white_cnt}')