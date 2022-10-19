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
    global cnt_v    # 울타리안의 늑대의 수
    global cnt_k    # 울타리안의 양의 수
    visited[x][y] = True        # 방문처리
    if fields[x][y] == 'v':     # 늑대면
        cnt_v += 1
    elif fields[x][y] == 'k':   # 양이면
        cnt_k += 1

    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]  # 범위안이고 아직 방문하지 않았고 울타리가 아니면
        if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and fields[nx][ny] != '#':
            dfs(nx, ny)         # 이동

row, col = map(int, input().split())
fields = [list(input()) for _ in range(row)]
visited = [[False] * col for _ in range(row)]
real_v = 0      # 총 늑대 수
real_k = 0      # 총 양 수

for i in range(row):
    for j in range(col):
        if not visited[i][j] and fields[i][j] != '#':
            cnt_v = 0   # 울타리안의 늑대수 , 울타리 바뀔때마다 초기화
            cnt_k = 0   # 울타리안의 양 수 , ''
            dfs(i, j)
            # 늑대 >= 양    -> 양의 숫자가 늑대의 숫자보다 더 많을 경우 늑대가 전부 잡아먹힌다. 물론 그 외의 경우는 양이 전부 잡아먹히겠지만 말이다.
            if cnt_v >= cnt_k:
                cnt_k = 0
            else:
                cnt_v = 0
            real_v += cnt_v
            real_k += cnt_k
print(real_k, real_v)