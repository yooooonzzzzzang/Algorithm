import sys

sys.stdin = open('input.txt', encoding='utf-8')
def dfs(i, N, c):
    if c == 3:      # 1 : 상원이 친구 2: 상원이 친구의 친구까지만
        return
    else:
        visited[i] = 1
        for j in range(1, n+1):
            if adjm[i][j] and visited[j] == 0:
                dfs(j, n, c+1)


for t in range(1, int(input()) + 1):
    n,m = map(int, input().split())
    adjm = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(n):
        a, b = map(int, input().split())
        adjm[a][b] = 1
        adjm[b][a] = 1
    visited = [0] * (n+1)
    dfs(1, n, 0)
    print(f'#{t} {sum(visited)-1}')