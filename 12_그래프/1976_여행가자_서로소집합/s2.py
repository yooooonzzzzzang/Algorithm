# 내가 푼거
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


n = int(input())    # 전체 도시의 수
m = int(input())    # 여행가려는 도시의 수

maps = [list(map(int, input().split())) for _ in range(n)]
plans = list(map(int, input().split()))
parent = list(range(n+1))
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            i_root, j_root = find_set(i+1), find_set(j+1)
            if i_root != j_root:
                parent[j_root] = i_root
result = 'YES'
print(parent)

for plan in plans:
    if parent[plans[0]] != find_set(plan):
        result = 'NO'
        break
print(result)
'''
3
3
0 1 0
1 0 1
0 1 0
1 2 3
'''