n , m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
# 좌, 상, 우, 하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
x, y, dir = n-1, m-1, 0

for i in range(n*m, 0, -1):
    arr[x][y] = i
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x, y = nx, ny
    else:
        dir = (dir+1)% 4
        x += dx[dir]
        y += dy[dir]
for line in arr:
    print(*line)