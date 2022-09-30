import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]

for t in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    graph = []
    cost = 0
    counts = 0
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        graph.append((w, n1, n2))
    graph.sort()
    parent = list(range(v+1))

    for dist, x, y in graph:
        x_root, y_root = find_set(x), find_set(y)
        if x_root != y_root:
            parent[y_root] = x_root
            print(parent)
            cost += dist
            counts += 1
            if counts >= v:     # 0~v번까지 :정점개수 = v+1
                break           # 간선의 최대개수: 정점개수 -1 = v
    print(f'#{t} {cost}')