'''
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 5 18
4 5 40
4 6 51
'''
v, e = map(int, input().split())
adjm = [[0] * (v+1) for _ in range(v+1)]
adjl = [[] for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    adjm[u][v] = w
    adjm[v][u] = w
    adjl[u].append((v,w))
    adjl[v].append((u,w))