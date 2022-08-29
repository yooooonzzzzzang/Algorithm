n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

a = 1
for k in range(n + m - 1):  # 대각선 개수
    for j in range(m):
        for i in range(n):
            if i + j == k:
                arr[i][m-1-j] = a
                a += 1
for line in arr:
    print(*line)