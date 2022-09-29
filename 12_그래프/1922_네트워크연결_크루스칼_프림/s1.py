'''
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
'''
def find_set(node):
    if node != parent[node]:
        ### 이 부분이 중요!! 왜 경로 압축이 되는가?!?!?!
        parent[node] = find_set(parent[node])
    return parent[node]

n = int(input())    # 컴퓨터의 수
m = int(input())    # 간선의 개수
network = []

for _ in range(m):
    # 시작, 도착, 비용
    s, e, w = map(int, input().split())
    network.append((w,s,e))
# 비용을 기준으로 정렬(오름차)
network.sort()
# make_set
parent = list(range(n+1))
counts = 0      # 더 이상 간선을 선택하지 않아도 되는 때를 판별
cost = 0        # 총 비용(최소가 되는 걸 찾고 싶다)

for w,x,y in network:
    x_root = find_set(x)
    y_root = find_set(y)

    # union
    if x_root != y_root:    # 서로소이면
        parent[y_root] = x_root
        cost += w
        counts += 1

        if counts >= n-1:
            break

print(cost)