n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
a = 1
for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        arr[j][i] = a
        a += 1
for line in arr:
    print(*line)