t = int(input())
canvas = [[0] * 100 for _ in range(100)]
for i in range(t):
    y, x = map(int, input().split())
    for x1 in range(99-x-10, 99-x):
        for y1 in range(y, y+10):
            canvas[x1][y1] = 1
result = 0

for i in range(100):
    for j in range(100):
        if canvas[i][j] == 1:
          result += canvas[i][j]

print(result)
