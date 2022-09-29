import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]
for t in range(1, int(input()) + 1):
    v, e = map(int, input().split())
    graph = []
    for _ in range(e):
        n1, n2 , w = map(int, input().split())
        graph.append((w, n1, n2))
    graph.sort()
    parent = list(range(v+1))
    print(graph)
    print(f'#{t} ')