import sys
sys.stdin = open("input.txt")
# 델타값을 이용해 쭉쭉 이동하다가 범위를 벗어나가나 값이 있으면 방향(인덱스) 바꾼다
# 1. 델타값 정의
dx = [0, 1, 0, -1]
#     우 하  좌  상
dy = [1, 0, -1, 0]


for t in range(1, int(input()) + 1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]
    x, y = 0, 0   # 출발 위치
    direction = 0  # 처음 출발 방향 오른쪽

    for i in range(1, n * n + 1):
        snail[x][y] = i
        # 다음 위치 이동
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 안에 있어? & 이미 숫자 없어?
        if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:
            x, y = nx, ny  # 이동
        else:   # 방향 바꿔서 다시 이동하자
            direction = (direction + 1) % 4     # 0 1 2 3 이 반복되어야함
            x += dx[direction]
            y += dy[direction]
            
    print(f'#{t}')
    for line in snail:  # line 행 한줄 출력한다는것
        print(*line)    # 언패킹 하면 [1,2,3] -> 1,2,3 근데 print 에서 , 는 space 의미


    #
    # print(f'#{t}')
    # for i in range(n):
    #     for j in range(n):
    #         print(snail[i][j], end=" ")
    #     print()