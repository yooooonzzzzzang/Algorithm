import sys
sys.setrecursionlimit(50000000)
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y,color):
    visited[x][y] = True

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and arts[nx][ny] == color:
            dfs(nx,ny,color)


n = int(input())
arts = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt1 = 0    # 적녹색약 아닌 사람 용
cnt2 = 0    # 적녹색약 용

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt1 += 1
            dfs(i, j, arts[i][j])

# R -> G 로 바꿔서 하나로 통일, visited 도 초기화
for i in range(n):
    for j in range(n):
        if arts[i][j] == 'R':
            arts[i][j] = 'G'
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt2 += 1
            dfs(i, j, arts[i][j])

print(cnt1, cnt2)
'''
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
'''