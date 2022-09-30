# 크루스칼
def find_set(node):
    if parent[node] != node:
        parent[node] = find_set(parent[node])
    return parent[node]
n = int(input())
m = int(input())
network = []
for _ in range(m):
    s,e,w = map(int, input().split())
    network.append((w,s,e))
network.sort()

parent = list(range(n+1))
cost = 0
count = 0

for distance, x, y in network:
    # x와 y의 각각의 대표값 저장
    x_root, y_root = find_set(x), find_set(y)
    # 사이클이 아니면
    if x_root != y_root:
        parent[y_root] = x_root     # union 같은 집합으로
        cost += distance
        count += 1
        if count >= n-1:     # 간선의 최대 개수 = 정점 -1
            break

print(cost)
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