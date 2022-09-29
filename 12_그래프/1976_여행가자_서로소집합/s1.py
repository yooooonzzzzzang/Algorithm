'''
3
3
0 1 0
1 0 1
0 1 0
1 2 3
'''
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]

def union(x_root, y_root):
    if x_root != y_root:  # 서로소 집합인 경우만 합집합 연산
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root

n = int(input())
m = int(input())
parent = list(range(n+1))
for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] =='1':
            i_root, j_root = find_set(i+1), find_set(j+1)
            union(i_root,j_root)

plans = list(map(int, input().split()))
root = find_set(plans[0])
result = 'YES'

for i in range(i, m):
    if root != find_set(plans[i]):
        result ='NO'
        break
print(result)
