'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v):
    visited[v] = True  # 시작 정점 방문처리
    queue = [v]  # 시작 정점을 큐에 넣고 초기화
    print(v, end=' ')   # 시작 정점부터 프린트

    # 큐가 빌 때까지 반복
    while queue:
        v = queue.pop(0)  # 현재 정점
        for next_v in graph[v]:  # 현재 정점과 인접한 모든 정점에 대해
            if not visited[next_v]:  # 아직 방문하지 않았다면
                visited[next_v] = True  # 인접 정점 방문처리
                queue.append(next_v)  # 인접 정점을 큐에 삽입
                print(next_v, end=' ')


n, m = map(int, input().split())  # 정점, 간선 개수

edges = list(map(int, input().split()))  # 간선 정보
graph = [[] for _ in range(n + 1)]  # 그래프 -> n + 1인 이유는 정점 번호가 1번부터이기 때문
visited = [False] * (n + 1)  # 방문 처리 리스트 -> n + 1인 이유는 정점 번호가 1번부터이기 때문

# 인접 리스트 만들기
for i in range(0, len(edges), 2):
    v1, v2 = edges[i], edges[i + 1]  # 인접한 두 정점
    # v1, v2를 양방향으로 넣는 이유는, 화살표가 없는 무방향 그래프이기 때문
    graph[v1].append(v2)
    graph[v2].append(v1)
print(graph)
bfs(1)  # 시작 정점을 1로 탐색 시작