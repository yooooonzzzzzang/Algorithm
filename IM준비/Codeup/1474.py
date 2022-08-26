n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
a = 1
flag = False
for j in range(m-1, -1, -1):
    for i in range(n):
        if not flag:
            arr[n-i-1][j] = a
            flag = True
        else:
            arr[i][j] = a
            flag = False
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