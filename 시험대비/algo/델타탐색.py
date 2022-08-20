dx, dy = [-1,1,0,0], [0,0,-1,1]

arr = []
x, y = 0,0
for k in range(4):
    nx, ny  = dx + x, dy + y
    if 0 <= nx < n and 0 <= ny < m:
        delta(nx, ny)