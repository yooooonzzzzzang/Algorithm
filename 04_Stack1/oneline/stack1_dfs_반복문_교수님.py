def dfs(v):
    print(v)
    visited = [False] * len(graph)  # 방문 처리 초기화
    visited[v] = True  # 시작 정점 방문 처리
    stack = [v]

    while stack:  # 스택이 빌 때까지 반복
        v = stack.pop()  # 현재 방문 정점 (후입선출)
        for next_v in graph[v]:  # 인접한 모든 정점에 대해
            if not visited[next_v]:  # 아직 방문하지 않았다면
                visited[next_v] = True  # 방문 처리
                stack.append(next_v)  # 스택에 넣기


graph = [
		[1, 2],
		[0, 3, 4],
		[0, 4, 5],
		[1],
		[1, 2, 6],
		[2],
		[4]
]

dfs(0)  # 0번 정점에서 시작