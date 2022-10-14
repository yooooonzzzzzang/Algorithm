'''
9 12
.###.#####..
#.kk#...#v#.
#..k#.#.#.#.
#..##k#...#.
#.#v#k###.#.
#..#v#....#.
#...v#v####.
.####.#vv.k#
.......####.
'''
import sys
sys.setrecursionlimit(500000000)
# 상하 좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x,y):
    global cnt_v
    global cnt_k
    visited[x][y] = True
    if fields[x][y] == 'v':
        cnt_v += 1
    elif fields[x][y] == 'k':
        cnt_k += 1

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and fields[nx][ny] != '#':
            dfs(nx, ny)

row, col = map(int, input().split())
fields = [list(input()) for _ in range(row)]
visited = [[False] * col for _ in range(row)]
real_v =0
real_k = 0

for i in range(row):
    for j in range(col):
        if not visited[i][j] and fields[i][j] != '#':
            cnt_v = 0
            cnt_k = 0
            dfs(i, j)
            # 늑대 >= 양
            if cnt_v >= cnt_k:
                cnt_k = 0
            else:
                cnt_v=0
            real_v += cnt_v
            real_k += cnt_k
print(real_k, real_v)