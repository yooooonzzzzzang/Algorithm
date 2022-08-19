import sys
sys.stdin = open('s_input.txt')

def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)

for t in range(1, int(input()) + 1):
    result = 0
    N, M = map(int,input().split())
    graph = [[] for _ in range(N + 1)]  # 1부터
    for _ in range(M):
        v1, v2 = map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (N + 1)

    for i in range(1, N + 1 ):
        if visited[i] == 0:
            result += 1
            dfs(i)

    print(f'#{t} {result}')
