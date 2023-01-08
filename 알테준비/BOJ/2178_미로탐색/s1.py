'''
4 6
110110
110110
111111
111101
'''
from collections import deque
# 최단거리 : bfs + 델타탐색
# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

n,m = map(int,input().split())
final_x, final_y = n-1, m-1
graph = [list(map(int,input())) for _ in range(n)]
bfs(0,0)
print(graph[final_x][final_y])




