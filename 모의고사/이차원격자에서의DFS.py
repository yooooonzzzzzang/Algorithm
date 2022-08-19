def dfs(x, y):
    visited[x][y] = True    #방문처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <=  nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 1:
            road.append((nx, ny))

            if nx == n - 1 and ny == m - 1:
                print(road)
                break
            dfs(nx, ny)
            road.pop()
    
    
    
n, m = map(int, input().split())   # 행, 열
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx, dy = [-1, 1, 0, 0],[0, 0, -1, 1]    # 상하좌우
road = [(0, 0)]

dfs(0, 0)   # 0,0 정점에서 시작