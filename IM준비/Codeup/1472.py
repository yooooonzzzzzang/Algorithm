n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
a = 1
for i in range(n):
    for j in range(m):
        if not i % 2:   # 짝수행
            arr[n-1-i][m-1-j] = a
        else:
            arr[n-1-i][j] = a
        a += 1

for line in arr:
    print(*line)