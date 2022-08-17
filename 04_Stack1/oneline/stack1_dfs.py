# A ~ G -> 0 ~ 6
# 인접리스트
# adjlist =[[1, 2],       # 0 A
#           [0, 3, 4],    # 1 B
#           [0, 4],       # 2 C
#           [1, 5],       # 3 D
#           [1, 2, 5],    # 4 E
#           [3, 4, 6],    # 5 F
#           [5]]          # 6 G

def dfs(v, N):
    top = -1
    print(v)             # 방문
    visited[v] = 1      # 시작점 방문 표시
    while True:
        for w in adjlist[v]:        # if ( v의 인접 정점 중 방문 안 한 정점 w 가 있으면)
            if visited[w] == 0:
                top += 1            # push(v)
                stack[top] = v
                v = w               # v <- W; (w 에 방문)
                print(v)            # 방문
                visited[w] = 1      # visited[w] <- true;
                break
        else:                       # w 가 없으면 -> 해당 인접 정점 다 방문
            if top != -1:           # 스택이 비어있지 않은 경우
                v = stack[top]      # pop
                top -= 1
            else:                   # 스택이 비어있으면
                break               # while 빠져나옴

V, E = map(int, input().split())
N = V + 1
adjlist = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)
visited = [0] * N   # visited 생성
stack = [0] * N     # stack 생성
dfs(1, N)
print()
