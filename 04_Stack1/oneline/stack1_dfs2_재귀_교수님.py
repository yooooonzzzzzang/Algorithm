def dfs(v):
    visited[v] = True  # 방문 처리

    for next_v in graph[v]:  # 인접한 모든 정점에 대해
        if not visited[next_v]:  # if visited[w] == 0:
            dfs(next_v)  # 방문하지 않았다면 인접 정점으로 이동


graph = [
		[1, 2],
		[0, 3, 4],
		[0, 4, 5],
		[1],
		[1, 2, 6],
		[2],
		[4]
]

visited = [False] * n  # 방문 처리 초기화
dfs(0)  # 0번 정점에서 시작