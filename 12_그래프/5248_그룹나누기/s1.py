import sys

sys.stdin = open('sample_input.txt', encoding='utf-8')

def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


for t in range(1, int(input()) + 1):
    n, m = map(int,input().split())     # n: 출석번호, m: 신청서
    parent = list(range(n+1))
    arr = list(map(int, input().split()))
    for i in range(m):
        x, y = arr[i*2], arr[i*2+1]
        x_root, y_root = find_set(x), find_set(y)
        if x_root != y_root:
            if x_root < y_root:
                parent[y_root] = x_root
            else:
                parent[x_root] = y_root

    #print(parent)
    for i in range(1, n + 1):
        parent[i] = find_set(i)
    #print(parent)

    print(f'#{t} {len(set(parent))-1}')