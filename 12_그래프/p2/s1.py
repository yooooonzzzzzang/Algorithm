def bfs(n):
    q = [n]
    visited[n] = 1

    while q:
        t = q.pop(0)
        answer.append(t)
        for i in adjlist[t]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)


arr = list(map(int, input().split()))
n = len(arr)//2
adjlist = [[] for _ in range(n)]
answer = []
for i in range(n):
    a, b = arr[i*2], arr[i*2+1]
    adjlist[a].append(b)
    adjlist[b].append(a)
visited = [0] * (n+1)
bfs(1)
print(*answer)
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7