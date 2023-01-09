'''
4
1 3
2 5
3 5
6 7
'''
# 그래프 연결
n = int(input())

# 그래프 크기를 어떻게??
graph = [[] for _ in range(n+1)]
print(graph)
for _ in range(n):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
print(graph)

