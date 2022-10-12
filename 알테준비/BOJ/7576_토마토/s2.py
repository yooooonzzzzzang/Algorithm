dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs():
    global day
    day += 1
    while queue:        # 큐에 값이 있는동안
        x, y = queue.pop(0)     # 현재 방문 지점
        for k in range(4):      # 델타검색
            nx = x + dx[k]
            ny = y + dy[k]
            # 범위안에 있고
            if 0 <= nx < n and 0 <= ny < m :
                if boxes[nx][ny] == 0:


# 열 , 행
m,n = map(int,input().split())
boxes = [list(map(int,input().split())) for _ in range(n)]
day = 0
queue =[]
for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:
            queue.append((i, j))  # 시작 좌표를 넣고 큐를 초기화
bfs()