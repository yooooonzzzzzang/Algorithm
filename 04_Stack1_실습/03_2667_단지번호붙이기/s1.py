# BOJ 2667. 단지번호붙이기
# https://www.acmicpc.net/problem/2667

def dfs(x, y):
    global total
    visited[x][y] = True  # 방문 처리
    total += 1  # 집이 있다는 의미이므로 단지 수 + 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        # 지도의 범위 안에 있고 & 아직 방문하지 않았으며 & 집이 있다면
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
            dfs(nx, ny)  # 이동


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
            total = 0  # 단지내 집의 수 초기화
            dfs(i, j)
            result.append(total)

print(len(result))
for i in sorted(result):
    print(i)