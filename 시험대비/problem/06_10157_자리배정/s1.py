C, R = map(int, input().split())    #7, 6 가로 세로
K = int(input())    # 11
x, y = R-1, 0
seat = [[0] * C for _ in range(R)]

# 상 우 하 좌
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
direction = 0
# 1. 좌석 배정
for i in range(1, C*R+1):
    seat[x][y] = i
    # 다음위치로 이동
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 범위 안에 있는지 숫자 없는지 ==0?
    if 0 <= nx < R and 0 <= ny < C and seat[nx][ny] == 0:
        x, y = nx, ny
    else:    # 아니면 방향 바꾸기
        direction = (direction + 1) % 4
        x = x + dx[direction]
        y = y + dy[direction]
result = []

# 2. 자리 찾기
if 0<= K <C*R:
    for i in range(R):
        for j in range(C):
            if K == seat[i][j]:
                print(j+1, R-i)
else:
    print(0)
