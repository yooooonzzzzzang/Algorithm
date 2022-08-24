n = int(input())
arr = [[0] * n for _ in range(n)]
a = 1

for i in range(n):
    for j in range(n):
        if not i % 2:   # 짝수
            arr[i][n-1-j] = a
        else:
            arr[i][j] = a
        a += 1


for line in arr:
    print(*line)