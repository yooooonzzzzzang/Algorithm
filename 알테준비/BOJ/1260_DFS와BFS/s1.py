'''
5 5 3
5 4
5 2
1 2
3 4
3 1

'''
from collections import deque

def dfs(v):
    print(v, end=" ")
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)



def bfs(v):
    visited[v] = True
    queue = deque([v])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

# 정점, 간선, 탐색시작 번호
n, m, v = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# 정렬
for i in range(n+1):
    graph[i].sort()

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
