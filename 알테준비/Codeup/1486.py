n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
# 하 좌 상 우
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x, y, dir = 0, m-1, 0

for i in range(1, n * m + 1):
    arr[x][y] = i
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x, y = nx, ny
    else:
        dir = (dir + 1) % 4
        x += dx[dir]
        y += dy[dir]

for line in arr:
    print(*line)
