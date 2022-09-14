n = int(input())
arr = [[0] * n for _ in range(n)]
a = 1
for i in range(n):
    for j in range(n):
        if not i % 2:   # 짝수일때
            arr[j][i] = a
        else:
            arr[n-1-j][i] = a
        a += 1

for line in arr:
    print(*line)