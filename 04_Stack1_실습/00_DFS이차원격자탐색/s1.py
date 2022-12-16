'''
5 5
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
1 0 0 0 0
1 1 1 1 0
'''
'''
5 5
0 0 1 1 1
1 0 1 1 1
0 0 0 1 1
1 1 0 0 1
1 1 1 0 0

'''
# 델타를 사용한 dfs
dx = [-1, 1, 0, 0]                                     # 상 하 좌 우
dy = [0, 0, -1, 1]

# dfs
def dfs(x,y):
    visited[x][y] = True                               # 방문처리
    for i in range(4):                                 # 델타 탐색
        nx = x + dx[i]
        ny = y + dy[i]
                                                       # 다음 경로가 범위안에 있고 방문한 적 없고 통로라면 루트에 추가
        if 0<= nx < n and 0 <= ny < m and not visited[nx][ny] and not maze[nx][ny]:
            route.append((nx,ny))
            if nx == n-1 and ny == m-1:
                print(route)
                return 0
            dfs(nx,ny)
            route.pop()                                  # 경로가 아닌 이전길 삭제


n, m = map(int,input().split())                          # n: 세로 , m: 가로
maze = [list(map(int,input().split())) for _ in range(n)]
route = [(0,0)]                                          # 출력할 값
visited = [[False]*m for _ in range(n)]
dfs(0,0)


