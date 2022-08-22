import sys

sys.stdin = open('sample_input.txt')
def dfs(v):
    visited[v] = True
    for next_v in graph[v]:     #
        if not visited[next_v]: # False 이면
            dfs(next_v)

for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())    # 노드 , 간선
    result = 0
    graph = [[] for _ in range(V + 1)]   # 1번 인덱스부터 사용 1~ V+1

    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    S, G = map(int, input().split())    # 출발 노드, 도착노드
    visited = [False] * (V + 1)
    dfs(S)
    # print(f'#{t}', end=' ')
    # if visited[g]:
    #     print(1)
    # else:
    #     print(0)


    print(f'#{t} {result}')