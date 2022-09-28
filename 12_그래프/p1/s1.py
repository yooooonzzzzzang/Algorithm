def dfs(i):
    print(i, end=' ')
    visited[i] = 1
    for j in range(1, len(arr)//2):
        if adjM[i][j] and visited[j] == 0:
            dfs(j)
#1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
arr = list(map(int, input().split()))
n = len(arr)
adjM = [[0]*(n//2) for _ in range(n//2)]
for i in range(len(arr)//2):
    a, b = arr[2*i], arr[2*i+1]
    adjM[a][b] = 1
    adjM[b][a] = 1
visited = [0] * (n//2+1)
dfs(1)


