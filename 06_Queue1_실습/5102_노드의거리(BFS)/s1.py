import sys

sys.stdin = open('sample_input.txt')
def bfs(v, N):  # 시작 정점, 마지막 정점
    q = []
    q.append(v)
    visited[v] = 1

    while q:    # 큐가 비어있지 않으면
        v = q.pop(0)
        for w in adjlist[v]:
            if w == G:
                print('ff', v)
                return visited[v]   # visitd[v] + 1 - 1
             elif visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1 # 몇번째 인지

    return 0
for t in range(1, int(input()) + 1):
    result = 0
    V, E = map(int, input().split())    # 정점개수, 간선개수
    adjlist = [[] for _ in range(V + 1)]    # 1부터 시작
    for _ in range(E):
        a, b = map(int, input().split())
        adjlist[a].append(b)
        adjlist[b].append(a)
    S, G = map(int, input().split())
    print(S, G)
    visited = [0] * (V + 1)
    #print(bfs(S, G))

    print(f'#{t} {bfs(S, G)}')