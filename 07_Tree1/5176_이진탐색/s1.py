import sys

sys.stdin = open('sample_input.txt')
def binary_search(n):
    global number
    if n <= N:  # 배열크기안쪽으로
        binary_search(2*n)     # 왼쪽노드
        tree[n] = number       # 더이상 갈 수 없다면 값 할당
        number += 1            # 값 증가
        binary_search(2*n+1)   # 오른쪽노드
for t in range(1, int(input()) + 1):
    N = int(input())

    tree = [0] * (N + 1)
    number = 1
    binary_search(1)
    # 루트에 저장된 값과, N/2번 노드에 저장된 값을 출력
    print(f'#{t} {tree[1]} {tree[N//2]}')
