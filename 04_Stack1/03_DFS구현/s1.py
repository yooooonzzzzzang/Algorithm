# 반복문 stack 을 이용한 dfs
def dfs(v):
    visited = [False] * n
    visited[v] = True # 시작 정점 방문 처리
    stack = [v]
    print(v)

    while stack:
        for next_v in graph[v]:
            if not visited[next_v]:
                v = next_v
                visited[v] = True
                stack.append(v)
                print(v)
                break
        else:
            v = stack.pop()



# 인접리스트
graph = [
    [1,2],
    [0,3,4],
    [0,4,5],
    [1],
    [1,2,6],
    [2],
    [4]
]
n = len(graph)

dfs(0)


