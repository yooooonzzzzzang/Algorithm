def prim1(r, v):
    mst = [0] * (v+1)
    key = [10000] * (v+1)
    key[r] = 0
    for _ in range(v):
        u = 0
        minV = 10000
        for i in range(v+1):
            if mst[i]==0 and key[i]<minV:
                u = i
                minV = key[i]
        mst[u] = 1
        for  v in range(v+1):
            if mst[v]==0 and adjm[u][v] > 0:
                key[v] = min(key[v], adjm[u][v])
    return sum(key)

v, e = map(int, input().split())
adjm = [[0] * (v+1) for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adjm[u][v] = w
    adjm[v][u] = w

prim1(0,v)