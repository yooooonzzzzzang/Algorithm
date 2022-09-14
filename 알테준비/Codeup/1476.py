n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
a = 1
for i in range(0, n+m-1):   # 대각선 개수
    for j in range(m):
        for k in range(n):
            if j + k == i:

                arr[k][j] = a
                a += 1
for line in arr:
    print(*line)