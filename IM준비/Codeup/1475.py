n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
a = 1
for j in range(m):
    for i in range(n):
        if not j % 2:
            arr[i][m-1-j] = a
        else:
            arr[n-1-i][m-1-j] = a
        a+=1
for line in arr:
    print(*line)