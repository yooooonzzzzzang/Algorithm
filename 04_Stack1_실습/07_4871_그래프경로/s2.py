import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')


def dfs(v):                                 # 재귀 이용
    visited[v] = True                       # 방문처리
    global result
    if v == g:                              # 현재노드(v)와 도착점이 같다면
        result = 1                          # 결과값을 1로 변경 후 종료
        return result
    for next_v in graph[v]:                 # 현재 정점과 인접한 모든 정점
        if not visited[next_v]:             # 아직 방문하지 않았다면
            dfs(next_v)                     # 인접 정점 방문


for t in range(1, int(input()) + 1):
    v, e = map(int,input().split())          # v: 노드의 수 e: 간선의 수
    graph = [[] for _ in range(v+1)]         # graph 1부터 사용하므로 +1
    visited = [False] * (v+1)                # 방문처리 리스트
    result = 0                               # 결과의 기본값은 0
    for _ in range(e):
        v1, v2 = map(int,input().split())
        graph[v1].append(v2)                 # 방향 그래프
    s, g = map(int, input().split())         # s: 시작점  g: 도착점

    dfs(s)                                   # 시작점부터 dfs시작
    print(f'#{t} {result}')