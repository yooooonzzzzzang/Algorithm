import sys

sys.setrecursionlimit(1000000000)
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
def dfs(x, y):
    visited[x][y] = True

    # 델타이동
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 밭의 범위 안에 있고 & 아직 방문하지 않았으며 & 배추 있다면
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and field[nx][ny] == 1:
            dfs(nx, ny) # 이동


for t in range(1, int(input()) + 1):
    m, n, k = map(int, input().split())     # 가로, 세로, 심은 배추 개수
    field = [[0] * m for _ in range(n)]     # 빈 밭 만들기

    for i in range(k):                      # 배추 심기
        x, y = map(int, input().split())
        field[y][x] = 1     #  X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)

    visited = [[False] * m for _ in range(n)]

    result = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and field[i][j] == 1:
                result += 1     # result 1씩 증가
                dfs(i,j)

    print(result)
