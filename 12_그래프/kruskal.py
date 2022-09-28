def find_set(x):
    while x!=rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)


v, e = map(int, input().split())
edge = []
for _ in range(e):
    u, v, w = map(int, input().split())
    edge.append([u,v,w])
edge.sort(key=lambda x:x[2])
rep = [i for i in range(v+1)]       # 대표원소 배열

n = v+1     # 실제정점의 수
cnt = 0
total = 0
for u, v, w in edge:
    if find_set(u)!= find_set(v):
        cnt += 1
        union(u,v)
        if cnt == n-1:
            break
print(total)