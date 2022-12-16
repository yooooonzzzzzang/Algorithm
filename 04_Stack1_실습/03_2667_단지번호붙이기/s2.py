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

dx = [-1, 1, 0, 0]                                       # 상 하 좌 우
dy = [0, 0, -1, 1]


def dfs(x, y):
    global cnt
    visited[x][y] = True                                    # 방문 처리
    cnt += 1                                                # 단지 수 증가

    for k in range(4):                                      # 델타탐색
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maps[nx][ny] == '1':     # 이어진 단지 탐색
            dfs(nx, ny)                                                                     # 이동


n = int(input())
maps = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count_list = []

for i in range(n):
    for j in range(n):                                      # 전체 maps 를 다 돌면서 아직 방문하지 않고 '1'인 곳을 찾는다
        if not visited[i][j] and maps[i][j] == '1':         # 찾았다면
            cnt = 0                                         # cnt(단지 수)를 초기화
            dfs(i,j)                                        # 델타 탐색시작
            count_list.append(cnt)                          # 델타탐색이 끝나면 단지 수를 추가

count_list.sort(reverse=True)
print(*count_list, sep='\n')