def prim2(r,v):
    mst = [0] * (v+1)
    mst[r] = 1
    s = 0
    for _ in range(v):
        u = 0
        minV =10000
        for i in range(v+1):
            if mst[i] == 1:
                for j in range(v+1):
                    if adjm[i][j] > 0 and mst[j] == 0 and minV > adjM[i][j]:
                        u = j
                        minV = adjm[i][j]
        s += minV
        mst[u] = 1
    return s

v, e = map(int, input().split())
adjm = [[0] * (v+1) for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adjm[u][v] = w
    adjm[v][u] = w

print(prim2(0, v))