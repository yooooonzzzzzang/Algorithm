# 길찾기 문제 bfs 로 풀기
def bfs(v, N, t):   #  시작, 마지막, 찾는 정점
    visited = [0] * (N+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:      # visit(v)
            return visited[99]    # 목표 발견
        # v 에 인접하고 방문안한 w 인큐 , 표시
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1

    return 0


T = 10
for _ in range(T):
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))

    adjList = [[] for _ in range(100)]
    for i in range(E):
        a, b = arr[i*2], arr[i*2 + 1]
        adjList[a].append(b)    # 단방향

    print(bfs(0, 99, 99))  # 시작, 마지막 정점, 목표 정점번호