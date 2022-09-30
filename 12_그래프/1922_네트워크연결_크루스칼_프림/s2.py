# 절대 다른 사람 답 보지 않고 스스로 해결해보기
def prim(start):
    visited = [False] * (n+1)
    distance = [INF] * (n+1)
    distance[start] = 0
    cost = 0

    for _ in range(n):
        min_dist = INF
        for idx, dist in enumerate(distance):
            if not visited[idx] and dist < min_dist:
                min_node = idx
                min_dist = dist
        visited[min_node] = True
        cost += min_dist
        for next_node, dist in graph[min_node]:
            if not visited[next_node] and dist < distance[next_node]:
                distance[next_node] = dist
    return cost



n = int(input())    # 정점의 수
m = int(input())    # 간선의 수
graph =[[] for _ in range(n+1)]
INF = 9999999
for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append((e, w))     # append 주의
    graph[e].append((s, w))
print(prim(1))  # 임의 설정
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