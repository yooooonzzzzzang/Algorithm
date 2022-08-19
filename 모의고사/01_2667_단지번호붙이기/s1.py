'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''


def dfs(x, y):
    visited[x][y] = True
    global total
    total += 1
    # 델타이동
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 지도의 범위 안에 있고 & 아직 방문하지 않았으며 & 집이 있다면
        if 0<= nx < n and 0<= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
            dfs(nx, ny) # 이동


# DFS 사용
n = int(input())
board = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []     # 결과값 (단지내 집의 수들의 모임)
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 1. 이차원 리스트를 행 순회
for i in range(n):
    for j in range(n):
        # 아직 방문 안한 집인 경우
        if not visited[i][j] and board[i][j] == 1:
            # 2. 1이면(집이면) DFS 시작
            total = 0
            dfs(i, j)
            result.append(total)
print(len(result))
for i in sorted(result):
    print(i)

# print(len(result), *sorted(result), sep='\n')