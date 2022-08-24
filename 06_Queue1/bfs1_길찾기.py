'''
# A ~ G -> 0 ~ 6
# 인접리스트
# adjlist =[[1, 2],       # 0 A
#           [0, 3, 4],    # 1 B
#           [0, 4],       # 2 C
#           [1, 5],       # 3 D
#           [1, 2, 5],    # 4 E
#           [3, 4, 6],    # 5 F
#           [5]]          # 6 G

6 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6

'''
def bfs(v, N):  # 시작정점, 마지막 정점
    visited = [0] * (N+1)   # visited 생성
    q = []          # queue 생성
    q.append(v)     # 시작점 인큐
    visited[v] = 1  # 시작점 방문 처리 표시
    while q:        # 큐가 비어있지 않으면
        v = q.pop(0)    # 디큐
        print(v)        # visit(v)
        for w in adjlist[v]:    # 인접하고 미방문(인큐되지 않은) 정점 w 가 있으면
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1



V, E = map(int, input().split())
N = V + 1   # N 정점개수
adjlist = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

bfs(0, V)