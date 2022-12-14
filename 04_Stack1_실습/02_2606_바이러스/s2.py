def dfs(v):
    global total
    visited[v] = True

    for next_v in graph[v]:
        if not visited[next_v]:
            total += 1
            dfs(next_v)


n = int(input())    # 컴퓨터의 수
e = int(input())    # 연결된 컴퓨터 쌍의 수 (간선의 수)
total = 0           # 바이러스에 걸린 컴퓨터의 개수
graph = [[] for _ in range(n+1)]    # 1~ 7까지 사용
visited = [False] * (n+1)           # 1~ 7까지 사용

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)
print(total)
'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''