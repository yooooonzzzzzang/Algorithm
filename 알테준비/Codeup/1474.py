n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
a = 1

for j in range(m):
    for i in range(n):
        if not j % 2:   #  짝수 열
            arr[n-1-i][m-1-j] = a
        else:
            arr[i][m-1-j] = a
        a += 1
for line in arr:
    print(*line)


    '''
    for row in range(m-1, -1, -1):
    for col in range(n):
        if not row % 2:
            arr[col][row] = k
        else:
            arr[n-1-col][row] = k
        k += 1

for line in arr:
    print(*line)
    '''