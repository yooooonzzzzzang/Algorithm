N = int(input())
arr = [[0] * N for _ in range(N)]
a = 1
for i in range(N):
    for j in range(N):
        arr[i][j] = a
        a += 1

for line in arr:
    print(*line)