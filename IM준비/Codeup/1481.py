n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

a = 1
for k in range(n + m - 1):  # 대각선 개수
    for i in range(n):
        for j in range(m):
            if i + j == k:
                arr[n-1-i][m-1-j] = a
                a += 1
for line in arr:
    print(*line)