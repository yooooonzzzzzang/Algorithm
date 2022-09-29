'''
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
'''
from heapq import heappop, heappush
def prim(start):
    visited = [False] * (n+1)
    heap = [(0, start)]
    cost = 0
    while heap:
        min_dist, min_node = heappop(heap)
        if visited[min_node]:
            continue
        visited[min_node] = True
        cost += min_dist

        # 인접 정점에 대해 가중치와 정점 정보를 힙에 삽입
        for next_node , w in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (w, next_node))
    return cost

# 프림 - 힙
n = int(input())
m = int(input())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

print(prim(1))