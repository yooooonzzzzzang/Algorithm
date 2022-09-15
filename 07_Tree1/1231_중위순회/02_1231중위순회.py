import sys

sys.stdin = open('input (2).txt', encoding='utf-8')
def inorder(v): # L V R
    if v <= N:
        inorder(v*2)    # L
        print(tree[v], end="")  # V
        inorder(v*2+1)  # R

for t in range(1, 11):
    N = int(input())    # 정점의 수
    tree = [0]*(N + 1)
    for i in range(N):
        arr = input().split()
        tree[int(arr[0])] = arr[1]
    print(f'#{t}',end=" ")
    inorder(1)
    print()

