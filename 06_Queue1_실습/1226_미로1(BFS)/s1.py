import sys

sys.stdin = open('input.txt')
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited[x][y] = True  # 시작 좌표 방문 처리
    queue = [(x, y)]  # 시작 좌표를 넣고 큐를 초기화
    global result   # 전역변수로 설정
    while queue:    # 큐에 값이 있는동안
        x, y = queue.pop(0)  # 현재 방문 지점

        for k in range(4):  # 델타검색으로 이동
            nx = x + dx[k]
            ny = y + dy[k]

            # 미로의 범위 안에 있고 & 아직 방문하지 않았으며 & 벽이 아니면-> 2 | 0 | 3 가능
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and maze[nx][ny] != 1:
                if maze[nx][ny] == 3:   # 도착점
                    result = 1
                    return  # 종료
                visited[nx][ny] = True  # 방문처리
                queue.append((nx, ny))  # 방문한 좌표 큐에 넣음



for t in range(1, 10 + 1):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    result = 0
    visited = [[False] * 16 for _ in range(16)]


    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:     # 시작점 찾으면 거기서 bfs 시작!
                bfs(i, j)

    print(f'#{t} {result}')