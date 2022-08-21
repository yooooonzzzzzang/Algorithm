N = int(input())
Find_n = int(input())
dx = [1, 0, -1, 0]  # 하 우 상 좌
dy = [0, 1, 0, -1]
snail = [[0] * N for i in range(N)]
x, y = 0, 0
direction = 0   # 처음 출발 방향 아래
for i in range(N*N,0,-1):
    snail[x][y] = i
    # 다음 위치 이동
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 범위 확인 & 갈 수 있는지
    if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
        x, y = nx, ny
    else:
        direction = (direction + 1) % 4     # 방향 바꾸기 중요
        x += dx[direction]
        y += dy[direction]

for line in snail:
    print(*line)

for x in range(N):
    for y in range(N):
        if snail[x][y] == Find_n:
            print(x+1, y+1)