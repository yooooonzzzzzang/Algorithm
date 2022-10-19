# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y):


# 행, 열
n, m = map(int, input().split())

pics = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    for j in range(m):
        if pics[i][j] != 0:
            cnt
            dfs(i,j)
