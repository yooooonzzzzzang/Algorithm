import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())    # 노드 , 간선
    result = 0
    graph = [[] for _ in range(V + 1)]   # 1번 인덱스부터 사용 1~ V+1
    print(graph)
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
    print(graph)
    Start , Finish = map(int, input().split())




    print(f'#{t} {result}')