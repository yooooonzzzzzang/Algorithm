# BOJ 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667

def bfs(x, y):
    visited[x][y] = True  # 시작 좌표 방문 처리
    queue = [(x, y)]  # 시작 좌표를 넣고 큐를 초기화
    total = 1  # 단지내 집의 수 초기화

    while queue:
        x, y = queue.pop(0)  # 현재 방문 지점
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 지도의 범위 안에 있고 & 아직 방문하지 않았으며 & 집이 있다면
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True  # 방문처리
                queue.append((nx, ny))  # 방문한 좌표 큐에 넣음
                total += 1  # 집이 있을 때마다 + 1

    return total


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())  # 지도의 크기
board = [list(map(int, input())) for _ in range(n)]  # 지도
visited = [[False] * n for _ in range(n)]  # 방문 처리 리스트
result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:  # 아직 방문하지 않은 집 탐색
            result.append(bfs(i, j))

print(len(result))
for i in sorted(result):
    print(i)