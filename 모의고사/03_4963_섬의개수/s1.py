import sys
sys.setrecursionlimit(100000)

dx, dy = [1, -1, 0, 0, -1, -1, 1, 1],[0, 0, 1, -1, -1, 1, 1, -1]    # 상, 하, 좌, 우, ↖, ↗, ↙, ↘


def dfs(x, y):
    visited[x][y] = True
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and maps[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:   # 탈출 조건
        break

    maps = [list(map(int, input().split())) for _ in range(h)] # 지도 만들기
    visited = [[False] * w for _ in range(h)]   # dfs 가 돌 visited
    result = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j] == 1:
                result += 1
                dfs(i, j)
    print(result)