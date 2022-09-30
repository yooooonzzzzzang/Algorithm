import sys

sys.stdin = open('sample_input.txt')
def prim(start):
    visited = [False] * (v+1)
    distance = [INF] * (v+1)
    distance[start] = 0
    cost = 0
    for _ in range(v+1):
        min_dist = INF
        for i, dist in enumerate(distance):
            if not visited[i] and dist < min_dist:
                min_node = i
                min_dist = dist
        visited[min_node] = True
        cost += min_dist

        for next_node,dist in graph[min_node]:
            if not visited[next_node] and dist < distance[next_node]:
                distance[next_node] = dist
    return cost

for t in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    INF = 99999999
    for _ in range(e):
        s, e, w = map(int, input().split())
        graph[s].append((e,w))
        graph[e].append((s,w))

    print(f'#{t} {prim(1)}')