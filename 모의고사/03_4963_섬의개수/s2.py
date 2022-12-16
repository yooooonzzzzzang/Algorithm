import sys
sys.setrecursionlimit(10000000)

dx = [-1,1,0,0,-1,-1,1,1]                # 상하좌우 대각선4
dy = [0,0,-1,1,-1,1,1,-1]


def dfs(x, y):
    visited[x][y] = True
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and maps[nx][ny]:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())          # w: 가로 h: 세로
    if not w and not h:
        break
    maps = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j]:
                cnt += 1
                dfs(i, j)
    print(cnt)