import sys

sys.stdin = open('sample_input.txt')

for t in range(1, int(input()) + 1):
    result = 0
    # N: 노드개수 M: 리프 노드 개수 L: 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for i in range(M):
        V, value = map(int, input().split())
        tree[V] = value
        while V != 0:   # 루트노드가 아닐때까지
            V //= 2     # 부모 노드로
            tree[V] += value

    print(f'#{t} {tree[L]}')
