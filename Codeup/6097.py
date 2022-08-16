h, w = map(int, input().split())
n = int(input())
zeros = [[0] * w for _ in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())

    for j in range(l):
        if d == 0:  # 가로
            zeros[x - 1][y - 1 + j] = 1
        else:   # 세로
            zeros[x - 1 + j][y - 1] = 1

for i in range(h):
    for j in range(w):
        print(zeros[i][j], end=' ')
    print(end='\n')
